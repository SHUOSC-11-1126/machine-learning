"""
HuggingFace 情感分析模型评估脚本
任务：在 IMDB 前 50 条评论上找到准确率 >95% 的模型
"""

import os
import pandas as pd
from transformers import pipeline

# 中国镜像
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 待评估的候选模型
CANDIDATE_MODELS = [
    # 目前最佳: siebert/sentiment-roberta-large-english (94%), lvwerra/distilbert-imdb (94%)

    # 第七轮：更强的 IMDB/SST-2 微调模型
    "textattack/roberta-base-imdb",                      # RoBERTa IMDB
    "jialicheng/roberta-base-finetuned-imdb",            # RoBERTa IMDB (另一个)
    "Kern-HW/DeBERTa-v3-base-mnli-fever-anli",          # DeBERTa NLI
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(SCRIPT_DIR, "datasets", "imdb_top_500.csv")
SUBSET_SIZE = 50


def hf_to_label(pred, id2label=None):
    """将模型输出的标签转为 0/1"""
    label = pred["label"]

    # 直接文本标签
    upper = label.upper()
    if upper in ("POSITIVE", "POS"):
        return 1
    if upper in ("NEGATIVE", "NEG"):
        return 0

    # 星级格式 "X stars"
    if "star" in label.lower():
        stars = int(label.split()[0])
        return 1 if stars >= 4 else 0

    # LABEL_0 / LABEL_1 格式
    if label == "LABEL_1":
        return 1
    if label == "LABEL_0":
        return 0

    # neutral → 视为负面（二分类场景）
    if upper == "NEUTRAL":
        return 0

    return 0


def evaluate_model(model_name, reviews, true_labels):
    """评估单个模型的准确率"""
    print(f"\n{'='*60}")
    print(f"模型: {model_name}")
    print(f"{'='*60}")

    try:
        import torch
        device = "cpu"  # 避免 MPS 内存不足
        classifier = pipeline(
            task="sentiment-analysis",
            model=model_name,
            tokenizer=model_name,
            framework="pt",
            device=device
        )
    except Exception as e:
        print(f"加载失败: {e}")
        return None

    # 预测
    try:
        predictions = classifier(reviews, truncation=True, batch_size=8)
    except Exception as e:
        print(f"预测失败: {e}")
        # 尝试逐条预测
        predictions = []
        for review in reviews:
            try:
                pred = classifier(review, truncation=True)
                predictions.append(pred[0])
            except Exception as e2:
                print(f"  单条失败: {e2}")
                predictions.append({"label": "NEGATIVE", "score": 0.0})

    # 查看模型标签格式
    print(f"模型标签: {classifier.model.config.id2label}")
    print(f"第一条预测: {predictions[0]}")

    # 转换标签
    pred_labels = [hf_to_label(pred) for pred in predictions]

    # 计算准确率
    correct = sum(p == y for p, y in zip(pred_labels, true_labels))
    accuracy = correct / len(true_labels)

    print(f"准确率: {accuracy:.2%} ({correct}/{len(true_labels)})")

    # 显示前 5 条对比
    for i in range(min(5, len(reviews))):
        match = "✓" if pred_labels[i] == true_labels[i] else "✗"
        print(f"  {match} 真实={true_labels[i]} 预测={pred_labels[i]} | {reviews[i][:80]}...")

    return accuracy


def main():
    # 加载数据
    df = pd.read_csv(DATASET_PATH)
    reviews = df["text"].iloc[:SUBSET_SIZE].tolist()
    true_labels = df["label"].iloc[:SUBSET_SIZE].tolist()

    print(f"数据集: {DATASET_PATH}")
    print(f"评估样本数: {SUBSET_SIZE}")
    print(f"待评估模型数: {len(CANDIDATE_MODELS)}")

    results = {}

    for model_name in CANDIDATE_MODELS:
        accuracy = evaluate_model(model_name, reviews, true_labels)
        if accuracy is not None:
            results[model_name] = accuracy

    # 汇总结果
    print(f"\n{'='*60}")
    print("汇总结果")
    print(f"{'='*60}")

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    for model_name, accuracy in sorted_results:
        mark = " ✓ (>95%)" if accuracy > 0.95 else ""
        print(f"  {accuracy:.2%}  {model_name}{mark}")

    # 保存结果
    results_path = os.path.join(SCRIPT_DIR, "results.txt")
    with open(results_path, "w") as f:
        f.write("模型评估结果\n")
        f.write(f"数据集: {DATASET_PATH}\n")
        f.write(f"评估样本数: {SUBSET_SIZE}\n\n")
        for model_name, accuracy in sorted_results:
            mark = " (>95%)" if accuracy > 0.95 else ""
            f.write(f"{accuracy:.2%}  {model_name}{mark}\n")
    print("\n结果已保存到 results.txt")


if __name__ == "__main__":
    main()
