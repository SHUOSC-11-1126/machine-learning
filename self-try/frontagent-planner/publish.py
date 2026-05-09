"""
FrontAgent Planner — HuggingFace 发布脚本

将 LoRA adapter 合并到基座模型并推送到 HuggingFace Hub
"""

import argparse
import json
from pathlib import Path

import torch
from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
from huggingface_hub import HfApi, login


BASE_MODEL = "Qwen/Qwen2.5-Coder-1.5B"
REPO_ID = "ceilf6/frontagent-planner-1.5B"

MODEL_CARD = """---
language:
- zh
- en
license: apache-2.0
base_model: Qwen/Qwen2.5-Coder-1.5B
tags:
- frontend
- agent
- planner
- code-generation
- lora
- sft
- unsloth
datasets:
- synthetic
model_type: qwen2
pipeline_tag: text-generation
---

# FrontAgent Planner 1.5B

基于 [Qwen2.5-Coder-1.5B](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B) 微调的前端任务规划模型。

## 模型介绍

该模型从 [FrontAgent-app](https://github.com) 的 Planner 阶段蒸馏而来，
能够根据自然语言的任务描述和项目上下文，生成结构化的前端开发执行计划。

### 能力

- 将前端开发任务分解为 7 个阶段（分析 → 创建 → 安装 → 验证 → 启动 → 浏览器验证 → 仓库管理）
- 每个步骤包含 description、action、phase 字段
- 支持 12 种动作类型: read_file, list_directory, create_file, apply_patch, search_code, get_ast, run_command, browser_navigate, browser_screenshot, get_page_structure, browser_click, browser_type
- 输出风险分析和备选方案

### 训练方法

- 基座模型: Qwen/Qwen2.5-Coder-1.5B
- 微调方式: SFT + LoRA (rank=16, alpha=32)
- 训练框架: Unsloth
- 训练数据: 由 Claude API 合成的 ~1000 条前端任务规划数据 (Alpaca 格式)

## 使用方法

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

model_name = "ceilf6/frontagent-planner-1.5B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

messages = [
    {"role": "system", "content": "你是一个资深前端工程师和项目规划专家。请根据以下任务描述和项目上下文，生成一个结构化的执行计划。计划应按阶段组织（阶段1-分析、阶段2-创建、阶段3-安装、阶段4-验证、阶段5-启动、阶段6-浏览器验证、阶段7-仓库管理），每个步骤包含 description（描述）、action（动作类型）、phase（所属阶段）。同时提供 risks（潜在风险）和 alternatives（备选方案）。\\n\\n可用的动作类型: read_file, list_directory, create_file, apply_patch, search_code, get_ast, run_command, browser_navigate, browser_screenshot, get_page_structure, browser_click, browser_type"},
    {"role": "user", "content": "任务：创建一个用户登录页面，包含邮箱和密码输入框，支持表单验证\\n\\n项目上下文：\\nReact 18 + TypeScript + Ant Design 5"},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=1536, temperature=0.7, top_p=0.9)
response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
print(response)
```

## 输出格式

模型输出 JSON 格式的执行计划:

```json
{
  "phases": [
    {
      "name": "阶段1-分析",
      "steps": [
        {
          "description": "检查项目现有路由和页面结构",
          "action": "read_file",
          "phase": "阶段1-分析"
        }
      ]
    }
  ],
  "risks": ["表单验证逻辑可能与后端校验冲突"],
  "alternatives": ["可考虑使用 Formik 替代 Ant Design Form"]
}
```

## 局限性

- 模型参数量较小 (1.5B)，复杂任务的计划质量可能有限
- 训练数据为合成数据，可能无法覆盖所有真实场景
- 建议作为辅助工具使用，生成的计划需人工审核
"""


def main():
    parser = argparse.ArgumentParser(description="发布模型到 HuggingFace")
    parser.add_argument("--base-model", default=BASE_MODEL)
    parser.add_argument("--adapter", default="output/lora_adapter", help="LoRA adapter 路径")
    parser.add_argument("--repo-id", default=REPO_ID, help="HuggingFace 仓库 ID")
    parser.add_argument("--max-seq-len", type=int, default=2048)
    parser.add_argument("--hf-token", default=None, help="HuggingFace token (也可用 HF_TOKEN 环境变量)")
    parser.add_argument("--private", action="store_true", help="创建私有仓库")
    parser.add_argument("--skip-push", action="store_true", help="只合并不推送 (本地测试)")
    args = parser.parse_args()

    # ── 1. 登录 HuggingFace ─────────────────────────────
    token = args.hf_token or os.environ.get("HF_TOKEN")
    if not args.skip_push:
        if token:
            login(token=token)
        else:
            print("提示: 使用 huggingface-cli login 或设置 HF_TOKEN 环境变量")
            login()  # 交互式登录

    # ── 2. 加载模型 + 合并 LoRA ─────────────────────────
    print(f"加载基座模型: {args.base_model}")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=args.base_model,
        max_seq_length=args.max_seq_len,
        dtype=None,
        load_in_4bit=False,  # 合并时需要完整精度
    )

    print(f"加载 LoRA adapter: {args.adapter}")
    from peft import PeftModel
    model = PeftModel.from_pretrained(model, args.adapter)
    model = model.merge_and_unload()
    print("LoRA 权重已合并到基座模型")

    tokenizer = get_chat_template(tokenizer, chat_template="chatml")

    # ── 3. 保存合并后的模型 ─────────────────────────────
    merged_path = Path("output/merged_model")
    merged_path.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(str(merged_path))
    tokenizer.save_pretrained(str(merged_path))
    print(f"合并模型已保存到: {merged_path}")

    # ── 4. 写入 Model Card ──────────────────────────────
    readme_path = merged_path / "README.md"
    readme_path.write_text(MODEL_CARD, encoding="utf-8")

    # ── 5. 推送到 HuggingFace ──────────────────────────
    if not args.skip_push:
        print(f"推送到 HuggingFace: {args.repo_id}")
        api = HfApi()
        api.create_repo(repo_id=args.repo_id, private=args.private, exist_ok=True)
        api.upload_folder(
            folder_path=str(merged_path),
            repo_id=args.repo_id,
            commit_message="Upload FrontAgent Planner 1.5B (Qwen2.5-Coder-1.5B + LoRA SFT)",
        )
        print(f"发布成功! https://huggingface.co/{args.repo_id}")
    else:
        print(f"跳过推送。本地合并模型在: {merged_path}")
        print(f"如需推送，去掉 --skip-push 参数重新运行")


if __name__ == "__main__":
    import os
    main()
