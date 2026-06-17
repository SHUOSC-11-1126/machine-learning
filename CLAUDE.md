# 机器学习期末复习仓库

## 项目目标

复习目标是从 `files-from-teacher/` 老师维护的课程子模块出发，按考试优先级梳理知识点、题型、代码填空（目前只考 logistic regression）、公式推导、概念解释、画图题和易错点。

## 资料优先级

`files-from-teacher/` 是唯一最高可信源。它是老师维护的子模块，所有复习判断必须从这里出发。

优先级固定为：

1. `files-from-teacher/Readme.md`：考试规则与范围说明。
2. `files-from-teacher/BagOfQuestions/`：题目来源，优先级极高。
3. `files-from-teacher/session-0` 到 `files-from-teacher/session-7`：主线 session 课件、代码和 practice，约占 final exam 的 70%；其中代码题准备只针对 logistic regression。
4. Extra questions 只来自 `files-from-teacher/session-201-qkv-attention-mini-series/`、`files-from-teacher/session-202-positional-encoding-mini-series/`、`files-from-teacher/session-203-masking-mini-series/`，约占 final exam 的 30%，按 Readme 描述通常更简单。
5. 其他 `files-from-teacher/session-*` 当前不考察，除非老师后续再次明确更新范围。

如果其他资料与 `files-from-teacher/` 冲突，直接以 `files-from-teacher/` 为准。

## 当前复习索引

优先读取：

- `review/source-index.md`
- `agents/plan.md`

`review/source-index.md` 由 `scripts/build_review_index.py` 从 `files-from-teacher/` 生成，用于快速定位老师资料、BagOfQuestions 和 session 主线。

## 考试信息

根据 `files-from-teacher/Readme.md`：

1. Final score = `0.7 * T + 0.3 * P`。
2. Final exam `T` 中，约 70% 来自主线 session 0-7：notation/basic ML setup、linear regression、logistic regression、neural networks、model selection 等。
3. 部分题目会来自 `files-from-teacher/BagOfQuestions/`。
4. 约 30% 来自 extra questions，目前只考 `session-201`、`session-202`、`session-203`，题目较简单。
5. Final exam 闭卷：no books, no sheets, no anything。
6. Duration: 2 hours。

## 最新考试范围更新

根据 2026-06-17 老师最新透露：

1. `files-from-teacher/session-0` 到 `files-from-teacher/session-7` 是主线。
2. `files-from-teacher/session-201-qkv-attention-mini-series/`、`files-from-teacher/session-202-positional-encoding-mini-series/`、`files-from-teacher/session-203-masking-mini-series/` 作为 extra questions。
3. 其他 `files-from-teacher/session-*` 不考察，除非老师后续再次明确更新。
4. 代码题只考 logistic regression；其他内容主要考概念、数学推导、公式解释、手算和画图。

## 最新考试题型更新

根据 2026-06-17 最新消息：

1. Code question scope: logistic regression only。
2. Main question types: concepts, mathematical derivations, drawing/sketching, formulas, and hand computation。
3. Linear regression、neural network layer、optimizer、dropout 等代码实现不再作为代码题优先准备；这些内容仍按概念、公式、推导和图形理解准备。

课程 Readme 写明 English for everything；因此考试题目、考试问法、答案、术语、公式解释中的关键表述必须优先使用英文。面向用户讲解时可以用中文解释思路，但题目与可背答案必须固定为 English first, then Chinese translation。

## Teach 技能默认使用

帮助用户复习时，必须直接使用 Teach 技能提高教学质量和复习效率。Teach 是教学方法要求，不替代本课程的 `files-from-teacher/` 最高可信源、考试范围、英文答题要求、来源标注和题目讲解格式。

默认行为：

1. 讲知识点、讲题、讲公式、讲代码、讲 shape、讲画图题、讲答题模板时，都按 Teach 的思路组织教学。
2. 默认用户是小白，先补必要前置概念，再进入机器学习术语、英文题干、数学符号、代码结构、tensor shape 或考试答案。
3. 每次只推进一个最小知识点，或一道题中的一个关键步骤；不要一次铺开太多。
4. 不使用“显然”“易得”“可知”等跳步表达代替解释。公式变形、梯度方向、shape 推导、画图依据、代码空格和英文术语都要说明理由。
5. 必须把知识点连接到 `files-from-teacher/Readme.md`、`BagOfQuestions/`、主 session 或 extra session：说明它为什么重要、可能怎么考、常见陷阱是什么。
6. 给出英文考试可写的答题模板，并给中文翻译，但不能只给模板而不解释。
7. 通过一个小练习、追问或自测点检查用户是否真的理解；用户答错时，回退到缺失的前置概念继续教。
8. 只有用户明确说“只要答案”“只要模板”“不要展开”时，才压缩教学过程。

## 回答结构

讲知识点时默认结构：

1. 来源：标注 `files-from-teacher/...` 文件路径；如果来自 BagOfQuestions，必须写出题目文件。
2. 前置概念：补齐理解该点所需基础。
3. 核心知识：定义、公式、图形含义；只有 logistic regression 需要按代码题准备代码结构。
4. Exam question：优先从 BagOfQuestions 提炼，先给英文题目/问法，再给中文翻译。
5. Answer：先给适合闭卷书写的英文答案，再给中文翻译。
6. 易错点：形状、符号、梯度方向、训练/测试泄漏、概率解释等。
7. 小练习：给一道同类型题检查掌握；小练习也必须像 Exam question 一样先给英文题目/问法，再给中文翻译。

遇到题目时默认结构：

1. Question：先引用或概括老师英文原题，再给中文翻译。
2. 解析：用中文讲思路、公式来源、图形/曲线依据、shape、易错点；只有 logistic regression 题需要重点讲代码空格。
3. Answer：先给英文完整考试版，再给中文翻译。
4. 来源：`files-from-teacher/...`

## 主 session 复习重点

0. Session 0：notation guideline、what is ML/DL、why neural networks from scratch、projection intuition、basic activation/log/sigmoid support。
1. Session 1：linear regression、MSE、gradient descent、matrix shapes、polynomial regression、train/test split。
2. Session 2：logistic regression、sigmoid、decision boundary、BCE vs MSE、feature scaling、threshold。
3. Session 3：neural network notation、forward propagation、activation functions、softmax、one-hot、output layer depends on task。
4. Session 4：backpropagation、chain rule、computation graph、Dense/ReLU/softmax cross-entropy、layer interface、training step。
5. Session 5：gradient update、learning rate、full-batch vs mini-batch SGD、momentum、Adam、bias correction。
6. Session 6：generalization、classification/regression metrics、validation/test split、bias-variance、L1/L2 regularization、Gaussian/Bernoulli basics。
7. Session 7：dropout、inverted dropout、early stopping、data augmentation、hyperparameter optimization、batch normalization。

## Extra question 复习重点

1. Session 201：QKV attention、self-attention、scaled dot-product attention、row-wise softmax、multi-head attention、self-attention vs cross-attention。
2. Session 202：positional encoding、why order matters、sinusoidal positional encoding、adding token embedding and positional vector。
3. Session 203：attention masks、causal mask、padding mask、combining masks、masking in transformers。

## 不确定情况

遇到以下情况必须向用户提问，不要自行决定：

1. `files-from-teacher/` 内资料之间存在冲突。
2. 需要更新子模块、切换分支或修改子模块内容。
3. 用户问题可能是在问非复习内容。
4. 需要使用非老师资料判断考试重点。

## 仓库维护

1. 不修改 `files-from-teacher/` 子模块内容，除非用户明确要求。
2. 生成的复习资料放在 `review/` 或 `agents/`。
3. 更新复习索引后运行：
   ```bash
   python3 scripts/build_review_index.py
   ```
