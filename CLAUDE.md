# 机器学习期末复习仓库

## 项目目标

本仓库现在用于期末复习，不再用于作业提交、微信群任务跟踪、项目交付或课程任务管理。

复习目标是从 `files-from-teacher/` 老师维护的课程子模块出发，按考试优先级梳理知识点、题型、代码填空、公式推导、概念解释和易错点。

## 资料优先级

`files-from-teacher/` 是唯一最高可信源。它是老师维护的子模块，所有复习判断必须从这里出发。

优先级固定为：

1. `files-from-teacher/Readme.md`：考试规则与范围说明。
2. `files-from-teacher/BagOfQuestions/`：题目来源，优先级极高。
3. `files-from-teacher/session-1` 到 `files-from-teacher/session-7`：主 session 课件、代码和 practice，约占 final exam 的 70%。
4. `files-from-teacher/session-*` 中的 extra sessions：约占 final exam 的 30%，按 Readme 描述通常更简单。
5. 本仓库历史作业经验：只能作为个人练习痕迹和低优先级辅助，不能决定考试范围，不能覆盖老师资料。

如果本仓库历史内容与 `files-from-teacher/` 冲突，直接以 `files-from-teacher/` 为准。

## 已清理噪音

以下任务期材料已从仓库移除并备份到仓库外：

- `tasks/`
- `tasks-list.md`
- `notes/`
- `.github/workflows/ci-cd.yml`

这些材料包含提交、微信群、URL、CV、CI/CD、任务状态、截图和历史实验中间文件，不再留在复习仓库中。

任务期材料已推送到独立归档仓库：`https://github.com/ceilf6/machine-learning-tasks`。

如需查看备份原件，必须先向用户确认；不要自行把备份复制回仓库。

## 当前复习索引

优先读取：

- `review/source-index.md`
- `review/homework-assets-low-priority.md`
- `agents/plan.md`

`review/source-index.md` 由 `scripts/build_review_index.py` 从 `files-from-teacher/` 生成，用于快速定位老师资料、BagOfQuestions 和 session 主线。

## 考试信息

根据 `files-from-teacher/Readme.md`：

1. Final score = `0.7 * T + 0.3 * P`。
2. Final exam `T` 中，约 70% 来自主 session 1-7：linear regression、logistic regression、neural networks、model selection 等。
3. 部分题目会来自 `files-from-teacher/BagOfQuestions/`。
4. 约 30% 来自 extra sessions，题目较简单。
5. Final exam 闭卷：no books, no sheets, no anything。
6. Duration: 2 hours。

课程 Readme 写明 English for everything；因此考试答案、术语、公式解释中的关键表述应优先使用英文。面向用户讲解时可以用中文解释思路，但最终可背答案应给英文版本。

## 回答结构

讲知识点时默认结构：

1. 来源：标注 `files-from-teacher/...` 文件路径；如果来自 BagOfQuestions，必须写出题目文件。
2. 前置概念：补齐理解该点所需基础。
3. 核心知识：定义、公式、代码结构或图形含义。
4. 考试问法：优先从 BagOfQuestions 提炼。
5. 英文答题版：给出适合闭卷书写的简洁答案。
6. 易错点：形状、符号、梯度方向、训练/测试泄漏、概率解释等。
7. 小练习：给一道同类型题检查掌握。

遇到题目时默认结构：

1. 题目：引用或概括老师原题。
2. 解析：用中文讲思路、公式来源、代码空格、shape、易错点。
3. Answer：英文完整考试版。
4. 来源：`files-from-teacher/...`

## 主 session 复习重点

1. Session 1：linear regression、MSE、gradient descent、matrix shapes、polynomial regression、train/test split。
2. Session 2：logistic regression、sigmoid、decision boundary、BCE vs MSE、feature scaling、threshold。
3. Session 3：neural network notation、forward propagation、activation functions、softmax、one-hot、output layer depends on task。
4. Session 4：backpropagation、chain rule、computation graph、Dense/ReLU/softmax cross-entropy、layer interface、training step。
5. Session 5：gradient update、learning rate、full-batch vs mini-batch SGD、momentum、Adam、bias correction。
6. Session 6：generalization、classification/regression metrics、validation/test split、bias-variance、L1/L2 regularization、Gaussian/Bernoulli basics。
7. Session 7：dropout、inverted dropout、early stopping、data augmentation、hyperparameter optimization、batch normalization。

## 不确定情况

遇到以下情况必须向用户提问，不要自行决定：

1. `files-from-teacher/` 内资料之间存在冲突。
2. 需要更新子模块、切换分支或修改子模块内容。
3. 需要从仓库外备份中恢复历史任务文件。
4. 用户问题可能是在问项目/作业而不是期末复习。
5. 需要使用非老师资料判断考试重点。

## 仓库维护

1. 不修改 `files-from-teacher/` 子模块内容，除非用户明确要求。
2. 生成的复习资料放在 `review/` 或 `agents/`。
3. 本仓库只保留复习相关材料；任务完成噪音应备份到仓库外或删除。
4. 更新复习索引后运行：
   ```bash
   python3 scripts/build_review_index.py
   ```
