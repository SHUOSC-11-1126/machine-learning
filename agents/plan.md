# 机器学习期末复习路线

## Summary

本计划只按知识点组织，不按时间推进。

最高优先级资料是 `files-from-teacher/` 子模块。根据 `files-from-teacher/Readme.md`，final exam 约 70% 来自主 session，部分题目来自 `files-from-teacher/BagOfQuestions/`；约 30% 来自 extra sessions，题目较简单。根据 2026-06-17 老师最新透露，主线明确为 `session-0` 到 `session-7`，extra questions 只来自 `session-201`、`session-202`、`session-203`，其他 `session-*` 不考察。最新题型消息进一步说明：代码只考 logistic regression，主要题型是 concepts、mathematical derivations、drawing/sketching、formulas、hand computation。最新最高优先级划范围记录已清洗到 `review/highest-priority-exam-scope-2026-06-17.md`，复习时先读它。

所有复习产物遵循 English-first rule：考试题目、考试问法、可背答案、关键术语和公式解释先写英文，再给中文翻译或中文讲解。中文用于帮助理解，不能替代英文考试版。

复习主线：session-0 notation/basic ML framing -> 线性回归与梯度下降概念/推导/图形 -> 逻辑回归概念/数学/唯一代码题 -> 神经网络前向传播与图示 -> softmax 和多分类公式/手算 -> 反向传播概念/链式法则 -> 优化器公式与轨迹图 -> 泛化、指标、正则化 -> dropout、early stopping、batch normalization 图形与解释 -> extra questions 201/202/203。

## Source Map

- `files-from-teacher/Readme.md`：考试比例、闭卷要求、主 session 和 extra session 权重。
- `files-from-teacher/BagOfQuestions/`：最高优先级题源。
- `files-from-teacher/session-0/`：notation guideline、ML/DL basic framing、why neural networks from scratch、projection intuition。
- `files-from-teacher/session-1/`：linear regression、MSE、gradient descent、polynomial regression、train/test split。
- `files-from-teacher/session-2/`：logistic regression、sigmoid、decision boundary、feature scaling、TensorFlow Playground / feature engineering。BCE is excluded by the latest scope update.
- `files-from-teacher/session-3/`：neural network architecture、forward propagation、activation functions、softmax、one-hot、output layers。
- `files-from-teacher/session-4/`：backpropagation、chain rule、computation graph、Dense/ReLU layer、softmax cross-entropy、training step。
- `files-from-teacher/session-5/`：learning rate、mini-batch SGD、momentum、Adam、bias correction。
- `files-from-teacher/session-6/`：generalization、metrics、evaluation methods、bias-variance、L1/L2 regularization、basic distributions。
- `files-from-teacher/session-7/`：dropout、inverted dropout、early stopping、data augmentation、hyperparameter optimization、batch normalization。
- `files-from-teacher/session-201-qkv-attention-mini-series/`：QKV attention、self-attention、scaled dot-product attention、multi-head attention、self-attention vs cross-attention。
- `files-from-teacher/session-202-positional-encoding-mini-series/`：positional encoding、why order matters、sinusoidal formula、embedding plus position。
- `files-from-teacher/session-203-masking-mini-series/`：causal mask、padding mask、combining masks、masking in transformer architectures。
- `review/source-index.md`：从老师子模块生成的快速索引。
- `review/highest-priority-exam-scope-2026-06-17.md`：2026-06-17 老师最高优先级范围录音/视频和手写记录的清洗版，包含音近词纠错和优先级压缩。

## Highest-Priority Scope Compression

根据 2026-06-17 老师最高优先级范围录音/视频：

- Session 1 is low priority：保留基础，不投入主要时间。
- Session 2 code target：logistic regression `def fit`、`n_features`、`linear_model = XW + b`、`sigmoid`、update sign。`dw`/`db` 精确推导有降级信号，先理解为 gradients。
- Session 2/3 softmax：公式、normalization、shift invariance、同加常数 `c` 后 `e^c` 约掉。
- TensorFlow Playground：feature engineering、`x_1^2`/`x_2^2`、圆形/曲线边界、underfitting / good fit / overfitting、high bias / high variance。
- Session 3 parameter counting：MoE / ChatGPT-style counting、embedding no bias、dense layer bias counts、FFN/MLP `d_model -> 4 d_model -> d_model` with one hidden layer。这个点不代表 `session-223` 重新进范围。
- Session 5：GD/SGD/Momentum/Adam formulas and loss-contour trajectory drawings。
- Session 6：L1/L2 penalty, lambda, L1 diamond, L2 circle, loss ellipses, first-touch geometry。
- Session 7：dropout diagram, early stopping curve, data augmentation rotation。
- Extra：must remember BagOfQuestions for `201/202/203`。
- Scope override：BCE is not tested. `BagOfQuestions-session-2-ad.md` is an older teacher question source, but the latest scope update overrides it for current exam preparation.

## Knowledge Route

0. **Session 0 Notation and Basic ML Framing**
   掌握 row-vector convention、ML/DL 基本定义、为什么从零实现 neural networks、projection intuition。
   考试重点：看懂后续 session 的 shape notation、activation/log/sigmoid 基础图像和符号。
   来源：`files-from-teacher/session-0/`

1. **Linear Regression From Scratch**
   掌握模型 `Y_hat = XW + b`、MSE、梯度、`np.dot`、`X.T`、shape 检查和参数更新。
   考试重点：概念、MSE/gradient update 推导、shape、解释 `weights` 与 `bias`、说明为什么更新要减去梯度；代码实现只作理解背景，不作为最新代码题优先级。
   来源：`files-from-teacher/session-1/`，`BagOfQuestions-session-1-*`

2. **Polynomial Regression and Feature Engineering**
   掌握 degree-2/degree-3/general degree-k model、feature map `phi(x)`、linear in parameters but nonlinear in input。
   考试重点：画 underfitting/good fit/overfitting 三种曲线，解释 polynomial regression 为什么仍是 linear regression after transformation。
   来源：`files-from-teacher/session-1/lecture-4-polynomial-linear-regression.md`，`BagOfQuestions-session-1-ah.md`

3. **Train/Test Split and Data Leakage**
   掌握 training set、test set、validation set 的用途，理解 no data leakage。
   考试重点：为什么不能用 test data 调参；训练、验证、测试三者区别。
   来源：`files-from-teacher/session-1/lecture-5-train-test-splitting.md`

4. **Logistic Regression Basics**
   掌握 `z = XW + b`、`sigmoid(z)`、probability interpretation、threshold and class label。
   考试重点：唯一代码题范围；优先准备 `def fit` 训练部分、`n_samples, n_features = X.shape`、`weights` 数量等于 `n_features`、`linear_model = np.dot(X, self.weights) + self.bias`、`y_predicted = self._sigmoid(linear_model)`、参数更新方向；`predict` 保留为 BagOfQuestions 备选；`dw`/`db` 精确推导按降级处理。
   来源：`files-from-teacher/session-2/`，`BagOfQuestions-session-2-aj.md`，`BagOfQuestions-session-2-ak.md`

5. **Decision Boundary**
   掌握 threshold 0.5 时 `sigmoid(z)>0.5` 等价于 `z>0`，二维边界是 line。
   考试重点：把 `w1*x1 + w2*x2 + b = 0` 改写成 `x2 = a*x1 + c`；数值点分类；改变 threshold 后边界仍是 line。
   来源：`files-from-teacher/session-2/lecture-3-logistic-regression-decision-boundary.md`，`BagOfQuestions-session-2-ac.md`

6. **BCE Is Out of Current Exam Scope**
   BCE / BCE vs MSE / BCE curves are not tested under the latest scope update.
   处理方式：不要按考试题准备 `BagOfQuestions-session-2-ad.md`；logistic regression 仍重点看 `def fit`、sigmoid、linear score、parameter update、decision boundary、softmax 和 TensorFlow Playground。
   来源：2026-06-17 最新范围更新覆盖旧 `BagOfQuestions-session-2-ad.md`

7. **Feature Scaling**
   掌握 normalization、standardization、why scales affect gradient descent。
   考试重点：大尺度特征导致梯度和 loss surface 不均衡，训练变慢或不稳定。
   来源：`files-from-teacher/session-2/lecture-5-feature-scaling.md`

8. **From Logistic Regression to Neural Networks**
   掌握 single neuron、layer、depth/width、notation、forward recursion。
   考试重点：解释为什么多个 linear layers without activation 等价于 single linear model。
   来源：`files-from-teacher/session-3/lecture-1-*` 到 `lecture-4-*`

9. **Activation Functions**
   掌握 sigmoid、tanh、ReLU formula and output range，ReLU advantages and dead neuron issue。
   考试重点：画激活函数；解释 nonlinearity；比较 sigmoid/tanh/ReLU。
   来源：`files-from-teacher/session-3/lecture-4-neural-networks-activation-functions.md`，`BagOfQuestions-session-3-ac.md`

10. **Softmax and One-Hot**
    掌握 softmax formula、shift invariance、numerical stability、one-hot labels、argmax。
    考试重点：手算 `[2,1,0]` softmax；解释 `[102,101,100]` 和 `[2,1,0]` 概率相同；写 stable softmax；能说明同加常数 `c` 时分子分母共同出现 `e^c`，所以会约掉。
    来源：`files-from-teacher/session-3/lecture-5-*` 到 `lecture-7-*`，`BagOfQuestions-session-3-ae.md`，`BagOfQuestions-session-3-af.md`

11. **Output Layer Depends on Task**
    掌握 regression、binary classification、multi-class classification 对应输出层和 loss。
    考试重点：说明什么时候用 linear output、sigmoid、softmax。
    来源：`files-from-teacher/session-3/lecture-5-neural-networks-output-layers-and-softmax.md`，`BagOfQuestions-session-3-ah.md`

11a. **MoE / FFN / MLP Parameter Counting**
    掌握 `MoE = Mixture of Experts`、`FFN = Feed-Forward Network`、`MLP = Multi-Layer Perceptron`、dense layer 参数量、embedding table no bias、router/expert 参数统计。
    考试重点：`BagOfQuestions-session-3-ag.md` 的 DeepSeek Mini MoE 参数统计；dense layer 要加 bias，embedding 通常不加 bias；transformer FFN/MLP 形状是 `d_model -> 4 d_model -> d_model`，中间 expanded layer 是 one hidden layer。注意：这不代表 `session-223` 重新纳入范围。
    来源：`files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ag.md`

12. **Backpropagation**
   掌握 chain rule、computation graph、forward values stored for backward、gradient flow。
    考试重点：解释 backprop 从 loss 回传到 parameters、链式法则、computation graph、梯度方向和公式含义；Dense/ReLU/training step 代码填空不再作为最新代码题优先级。
    来源：`files-from-teacher/session-4/`，`BagOfQuestions-session-4-*`

13. **Layer Interface and Minimal NN Implementation**
    掌握 `forward`、`backward`、stored activations、parameter gradients、network training step。
    考试重点：概念解释和图示：为什么 forward 要保存输入/激活；layer interface 如何使 Dense、ReLU、SoftmaxCE 组合；不按代码题优先准备。
    来源：`files-from-teacher/session-4/code-my_nn.md`，`code-connections-with-lecture.md`

14. **Optimization Basics**
    掌握 gradient gives direction、learning rate controls step size、minus sign means move against gradient。
    考试重点：too small / too large learning rate；gradient to parameter update。
    来源：`files-from-teacher/session-5/lecture-1-*`，`lecture-2-*`，`BagOfQuestions-session-5-aa.md`

15. **Full-Batch GD vs Mini-Batch SGD**
    掌握 batch size trade-off、noisy descent、speed/memory/generalization。
    考试重点：比较 full-batch、SGD、mini-batch；选择 batch size 的 trade-off。
    来源：`files-from-teacher/session-5/lecture-3-from-gd-to-sgd.md`，`BagOfQuestions-session-5-ab.md`，`BagOfQuestions-session-5-ac.md`

16. **Momentum and Adam**
    掌握 momentum velocity、Adam first moment、second moment、bias correction、default intuition。
    考试重点：写 Adam formulas；解释 bias correction；比较 SGD、Momentum、Adam；画 optimizer 更新轨迹，说明 SGD 的 noisy/zig-zag path、Momentum 如何平滑振荡、Adam 如何用自适应步长。
    来源：`files-from-teacher/session-5/lecture-4-momentum.md`，`lecture-5-adam.md`，`BagOfQuestions-session-5-ad.md` 到 `session-5-ag.md`

17. **Generalization and Metrics**
    掌握 training error、true error、confusion matrix、accuracy、precision、recall、F1、MSE、MAE、R2。
    考试重点：class imbalance 下为什么 accuracy 可能误导；precision/recall trade-off。
    来源：`files-from-teacher/session-6/lecture-1-*` 到 `lecture-4-*`，`BagOfQuestions-session-6-aa.md`，`session-6-ab.md`

18. **Bias-Variance and Model Selection**
    掌握 high bias/underfitting、high variance/overfitting、validation workflow、K-fold basics。
    考试重点：画 bias-variance tradeoff；识别训练/验证误差曲线。
    来源：`files-from-teacher/session-6/lecture-5-model-selection-bias-variance.md`，`BagOfQuestions-session-6-af.md`

19. **L1/L2 Regularization**
    掌握 regularized objective、L2 weight decay、L1 sparsity、gradient/update rule、geometry of norm balls。
    考试重点：公式、几何解释、L1/Lasso 为什么促稀疏、L2/Ridge 为什么平滑缩小权重；画 data-loss ellipses 与 L1 diamond / L2 circle，并标出 first-touch point。
    来源：`files-from-teacher/session-6/lecture-6-*` 到 `lecture-9-*`，`BagOfQuestions-session-6-ag.md` 到 `session-6-ai.md`

20. **Probability Distributions in ML**
    掌握 normal distribution、bivariate normal、covariance/correlation、Bernoulli/binomial、CLT、dropout as Bernoulli process。
    考试重点：解释 covariance matrix、correlation effect、CLT 与 mini-batch gradient noise。
    来源：`files-from-teacher/session-6/code-stats-distributions-*-math.md`，`BagOfQuestions-session-6-ak.md`

21. **Dropout**
    掌握 training-time random mask、inverted dropout scaling by `1/(1-p)`、eval mode no-op、implicit ensemble。
    考试重点：画 dropout 前后网络图、期望值计算、解释 inverted dropout 为什么除以 `1-p`、为什么 train/eval mode 必须分开；代码填空不再作为最新代码题优先级。
    来源：`files-from-teacher/session-7/lecture-1-dropout.md`，`lecture-2-dropout-1-p-multipy-or-devide.md`，`BagOfQuestions-session-7-ab.md`，`session-7-ac.md`，`session-7-ah.md`

22. **Other Regularization and Model Selection Tools**
    掌握 early stopping、data augmentation、hyperparameter optimization、batch normalization。
    考试重点：validation loss 上升时 early stopping；画 train/validation loss curves 和 train/validation accuracy curves，标出 best validation epoch / stop point / patience；label-preserving transformation；grid search vs random search；BN train/inference behavior。
    来源：`files-from-teacher/session-7/lecture-3-*` 到 `lecture-6-*`，`BagOfQuestions-session-7-aa.md`，`session-7-ae.md`，`session-7-af.md`

23. **Extra Question 201: QKV Attention**
    按 Readme 约 30% easy questions 处理，但范围只看老师最新指定的 extra question sessions。Session 201 重点掌握 Q/K/V、self-attention、scaled dot-product attention、row-wise softmax、multi-head attention、self-attention vs cross-attention。
    考试重点：1-3 句解释 self-attention；写 `softmax(QK^T / sqrt(d_k))V`；说明 row-wise softmax；区分 self-attention 和 cross-attention。
    来源：`files-from-teacher/session-201-qkv-attention-mini-series/`，`BagOfQuestions-session-201-ee.md`

24. **Extra Question 202: Positional Encoding**
    掌握为什么 Transformer 需要位置信息、sinusoidal positional encoding 的基本形式、token embedding 加 positional vector。
    考试重点：解释 self-attention 本身不包含顺序；写 embedding + positional encoding 的组合公式 `h_i = x_i + p_i`；识别 sine/cosine position signal；会做 `i=0` 的小计算：sine channels are `0` and cosine channels are `1`。
    来源：`files-from-teacher/session-202-positional-encoding-mini-series/`，`BagOfQuestions-session-202-ee.md`

25. **Extra Question 203: Masking**
    掌握 causal mask、padding mask、combining masks，以及 mask 如何限制 attention 信息流。
    考试重点：说明 autoregressive decoder 为什么不能看 future tokens；写 causal validity relationship `j <= i`；画 lower-triangular causal mask；说明 masked positions are set to `-inf` before softmax, so `exp(-inf)=0` and the attention weight becomes zero；说明 padding mask 为什么需要；写 masked attention 的核心想法。
    来源：`files-from-teacher/session-203-masking-mini-series/`，`BagOfQuestions-session-203-ee.md`

Out of scope：`session-102`、`session-104`、`session-105`、`session-200`、`session-204`、`session-205`、`session-208`、`session-211`、`session-212`、`session-223`、`session-400+`、`session-501` 等其他 `session-*` 目录当前不考察，除非老师后续再次明确更新范围。

## High-Priority Exam Patterns

- Code blanks: logistic regression only, especially `def fit`, `n_features`, `linear_model`, `_sigmoid(linear_model)`, and parameter update sign. `predict` is a backup BagOfQuestions item; BCE is not treated as a code-blank priority.
- Highest-priority code focus from the latest range recording: logistic regression `def fit`, `n_features`, `linear_model`, `_sigmoid(linear_model)`, and update sign; exact `dw`/`db` derivation is lower priority unless the final question follows BagOfQuestions literally.
- Shape questions: `X`, `W`, `y_predicted`, `dw`, logits, softmax probabilities, but answer as shape reasoning unless it is logistic-regression code.
- Formula writing and derivation: MSE, sigmoid, softmax, cross-entropy except BCE, gradient update, Momentum, Adam, L1/L2, dropout expectation, attention formula. BCE is out of current exam scope.
- Hand computation: logistic one-step gradient descent, softmax probabilities, decision boundary classification, parameter count.
- Concept explanation: feature scaling, nonlinearity, backprop, mini-batch trade-off, bias-variance, regularization, dropout expectation, early stopping. BCE vs MSE is out of current exam scope.
- Drawing/sketching: polynomial underfit/good/overfit, decision boundary, activation curves, softmax bar chart, optimization paths, bias-variance curve, L1/L2 geometry, dropout subnetworks, early-stopping curves. Do not prepare BCE curves for the current exam.
- Second-hand checklist audit: `review/essential-cleaned-audit.md` records which classmate-note items are useful, wrong, or out of scope. Do not use it to expand scope beyond `session-201`/`202`/`203`.

## Review Method

每次只学一个小知识点，固定流程：

1. Read `review/source-index.md` to locate teacher materials.
2. Read the matching BagOfQuestions file first if available.
3. Read the matching session lecture file first; read code files mainly for logistic regression code questions or for conceptual support.
4. Extract or write the exam question in English first, then add a Chinese translation.
5. Produce an English exam-ready answer first, then add a Chinese translation.
6. Add a short Chinese explanation for understanding.
7. Do one similar practice question, also English first with Chinese translation.

## Assumptions

- 当前复习范围以 `files-from-teacher/Readme.md` 加 2026-06-17 老师最新口头范围更新为准：main = session-0 到 session-7；extra = session-201、session-202、session-203；其他 session 不考察。代码题只考 logistic regression，主要题型为概念、数学推导、画图、公式和手算。
- 如果老师子模块更新，应重新生成 `review/source-index.md`。
