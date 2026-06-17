# Highest-Priority Exam Scope From 2026-06-17 Range Recording

## Sources

- Audio: `老师关于考试的透露/最高优先级！考试范围划定.m4a`
- Video: `老师关于考试的透露/最高优先级！考试范围的划定.mp4`
- User-provided noisy note from the same range discussion.
- User-provided screenshots:
  - High bias / underfitting figure.
  - Dropout neural-network diagram.
  - Early stopping validation-loss diagram.
- Cross-checked teacher files:
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ag.md`
  - `files-from-teacher/session-6/lecture-5-model-selection-bias-variance.md`
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ag.md`
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-201-ee.md`
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-202-ee.md`
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-203-ee.md`

Processing note: the two media files were transcribed with ASR after extracting/compressing audio. Raw ASR text was kept as temporary working material under `/tmp/ml-exam-scope-asr`, not committed here.

## Scope Rule

This recording is the highest-priority spoken scope update currently available. It does not replace the structural rule that main sessions are `session-0` to `session-7` and extra questions are `session-201`, `session-202`, and `session-203`.

Important nuance:

- The recording makes some topics much higher priority.
- It does not make `session-204`, `session-205`, or `session-223` part of the current exam scope.
- FFN/MLP parameter counting is in scope only because it was mentioned in the range recording and matches Session 3 / MoE / ChatGPT-style parameter-counting questions, not because `session-223` is re-added.

## Cleaned Phonetic Terms

| Noisy phrase | Clean term | Meaning for review |
| --- | --- | --- |
| `sql`, `signal`, `sigmoid function` variants | `sigmoid` | Logistic-regression activation. Know formula if provided, and draw S-shaped curve from 0 to 1 with value 0.5 at input 0. |
| `stopmax` | `softmax` | Multi-class normalization: exponentiate logits and divide by the sum. |
| `dotf fit`, `dumpfit`, `database this system` | `def fit` | The logistic-regression training method. |
| `gtensor features`, `n_features` | `n_features` | Number of weights equals number of features, not number of samples. |
| `1 的多少次方`, `c 约分` | `e^z`, softmax shift cancellation | Adding the same constant `c` to all logits does not change softmax because the factor `e^c` cancels. |
| `tesla flow playground` | `TensorFlow Playground` | Feature engineering and decision-boundary drawings. |
| `underlieing`, `underline` | `underlying model/function` | The model behind the decision boundary, such as linear or polynomial features. |
| `beating layer`, `hindnear`, `hllownear` | `hidden layer` | The internal layer between input and output. |
| `mob` | `MoE` / `Mixture of Experts` | Expert networks plus router; parameter-counting topic. |
| `FNN` in the note | usually `FFN` | Feed-forward network inside a transformer block. |
| `mps`, `nlp` in ASR context | `MLP` | Multi-layer perceptron; in this context paired with FFN. |
| `dmodel`, `demodel` | `d_model` | Transformer hidden/model dimension. |
| `std` in optimizer context | `SGD` | Stochastic gradient descent, described as zig-zag/noisy. |
| `item` in optimizer context | `Adam` | Adaptive optimizer; prepare formulas with momentum. |
| `munition` | `momentum` | Momentum optimizer / velocity smoothing. |
| `lar`, `lr` around regularization | `L1` / `L2` | L1 absolute-value penalty; L2 squared penalty. |
| `job hop` near regularization diagram | likely `dropout` | Dropout network diagram. |
| `dataup rotation` | `data augmentation: rotation` | Label-preserving transformation. |
| `erly stoping` | `early stopping` | Stop when validation loss stops improving / begins rising. |
| `qkb` | `QKV` | Query, Key, Value in attention. |
| `wdk` | unresolved noisy fragment | Do not convert into an exam topic without more context. |

## Highest-Priority Topics

### 1. Session 1 Is Low Priority

English exam signal:

Session 1 is not the main target in this latest range recording.

中文：

第一章/Session 1 不是现在的第一优先级。不要删掉，但只保留基础理解：linear model、MSE、gradient update、polynomial feature idea。

### 2. Session 2 Logistic Regression Is The Main Code Target

English checklist:

- Know `def fit` in logistic regression.
- Know `n_samples, n_features = X.shape`.
- Know why `self.weights` has `n_features` entries.
- Know `linear_model = np.dot(X, self.weights) + self.bias`.
- Know `y_predicted = self._sigmoid(linear_model)`.
- Know parameter update form: old value minus learning rate times gradient.
- Know sigmoid shape: S curve, output in `(0, 1)`, value `0.5` at input `0`.

中文：

代码题集中在 logistic regression 的训练结构，尤其是 `def fit`、`sigmoid`、`linear_model`、`n_features` 和更新方向。老师口述里对 `dw`、`db` 的精确公式有降级信号；先会解释它们是 gradients，不要把主要时间花在推导它们。

Teacher source:

- `files-from-teacher/session-2/code-my_logistic_regression.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-aj.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ak.md`

### 3. Session 2 Softmax May Be Asked Together With Logistic Regression

English checklist:

- Write softmax:

$$
\operatorname{softmax}(z)_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

- Explain it normalizes logits into probabilities that sum to 1.
- Explain shift invariance:

$$
\operatorname{softmax}(z+c)=\operatorname{softmax}(z)
$$

because `e^c` appears in both numerator and denominator and cancels.

中文：

老师特别提到 softmax 的分子分母、求和、normalization，以及为什么给每个 logit 加同一个常数 `c` 后结果不变。例子可以准备：`[10001, 10002, 10003]` 和 `[-2, -1, 0]` 的 softmax 相同，因为前者整体减去 `10003`。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-af.md`

### 4. TensorFlow Playground / Feature Engineering / Fitting Level

English checklist:

- Raw logistic regression with only `x_1, x_2` gives a linear boundary.
- Ring or circle patterns need engineered quadratic features such as `x_1^2` and `x_2^2`.
- Degree-1 / too simple boundary means underfitting / high bias.
- Too wiggly or overly complex boundary means overfitting / high variance.
- A smooth curved boundary can be a good fit.
- Adding features, neurons, or hidden layers increases model capacity.

中文：

这对应你截图里的 high bias / underfitting 图，以及 `BagOfQuestions-session-2-ag.md`。要会画三张：underfitting 直线、good fitting 平滑曲线/圆形边界、overfitting 扭来扭去的复杂边界。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ag.md`
- `files-from-teacher/session-6/lecture-5-model-selection-bias-variance.md`

### 5. Session 3 MoE / ChatGPT / Parameter Counting

English checklist:

- Know `MoE = Mixture of Experts`.
- Know `FFN = Feed-Forward Network`.
- Know `MLP = Multi-Layer Perceptron`.
- For dense layers, count both weights and bias unless the question explicitly says no bias.
- For an embedding table, there is usually no bias term; count `vocab_size * embedding_dim`.
- In a transformer-style FFN/MLP block, the shape is usually `d_model -> 4 d_model -> d_model`.
- This FFN/MLP has one hidden layer: the expanded `4 d_model` layer.

中文：

老师强调“有没有动脑”比极细小数字更重要。正确原则是：dense layer 参数量 = `in_features * out_features + out_features`；embedding 表通常没有 bias。FFN/MLP 的核心图是先扩展到 `4 d_model`，再收缩回 `d_model`。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ag.md`

### 6. Session 5 Optimizers: Draw The Loss Contours And Write Formulas

English checklist:

- Draw loss contours as ellipses.
- GD is more stable/smooth.
- SGD is noisy and can zig-zag.
- Momentum smooths oscillation like accumulating velocity.
- Adam uses first moment, second moment, bias correction, and adaptive scaling.
- Write a generic update:

$$
W \leftarrow W - \eta g
$$

where `g` can mean the gradient / partial derivative. If time is short, writing one parameter update is acceptable; `W` and `b` do not need completely separate explanations unless asked.

中文：

第 5 章最重要的是“公式 + 图”。图画等高线椭圆，从高 loss 走向低 loss；SGD 之字形，GD 平稳，Momentum/Adam 更 smooth。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ad.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-af.md`

### 7. Session 6 L1/L2 Regularization Geometry

English checklist:

- L1 penalty:

$$
\lambda \sum_i |w_i|
$$

- L2 penalty:

$$
\lambda \sum_i w_i^2
$$

- L1 constraint shape is a diamond.
- L2 constraint shape is a circle.
- Draw data-loss contours as ellipses.
- The solution is where the lowest tolerable loss contour first touches the constraint region.
- L1 often touches at a corner, producing sparse / zero weights.

中文：

老师用“慢慢放低标准”解释：一开始想要很低的 loss，但正则约束做不到，于是放到第一个能碰到约束区域的等高线；这个 first-touch point 就是正则化下能容忍的最低 loss。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ah.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ai.md`

### 8. Session 7 Regularization Diagrams

English checklist:

- Draw dropout as randomly removing neurons/activations during training.
- Explain dropout reduces reliance on particular neurons and helps reduce overfitting.
- Draw early stopping with training loss decreasing and validation loss first decreasing then rising.
- Stop near the best validation-loss point; patience may allow a few epochs.
- Data augmentation can be shown by image transformations such as rotation.

中文：

你给的 dropout 图和 early stopping 图都应直接纳入画图题准备。Early stopping 的关键句：do not continue training after validation loss starts increasing, because the model is entering overfitting.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-aa.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ab.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ae.md`

### 9. Extra Questions: Memorize 201 / 202 / 203

English checklist:

- Session 201: write scaled dot-product attention and explain self-attention vs cross-attention.
- Session 202: know sinusoidal positional encoding and the `i=0` calculation.
- Session 203: know causal mask, `j <= i`, and `-inf` before softmax.

中文：

老师最新范围仍然是 201/202/203。`qkb` 应清洗为 `QKV`。不要把 204/205/223 因为同学资料或旧笔记重新加回考试范围。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-201-ee.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-202-ee.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-203-ee.md`

## Conflicts / Do Not Decide Silently

### BCE Is Not Tested

BCE is not tested under the latest scope clarification. Teacher-maintained `BagOfQuestions-session-2-ad.md` still explicitly asks BCE and BCE vs MSE, but it is overridden for current exam preparation.

Current handling:

- Do not prepare BCE / BCE vs MSE / BCE curves as exam topics.
- Do not use `BagOfQuestions-session-2-ad.md` for current exam-priority practice.
- For Session 2, prioritize logistic-regression code, sigmoid, softmax, TensorFlow Playground, feature engineering, and decision-boundary reasoning.

### Predict Method

The latest ASR strongly emphasizes `def fit` / training. It also contains noise around whether `predict` is tested.

Current handling:

- Prioritize `def fit`.
- Keep `predict` as backup because `BagOfQuestions-session-2-ak.md` exists.

### `wdk`

This fragment is unresolved. Do not convert it into a topic unless more context appears.
