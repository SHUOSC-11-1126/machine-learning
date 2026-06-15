# 机器学习期末复习路线

## Summary

本计划只按知识点组织，不按时间推进。

最高优先级资料是 `files-from-teacher/` 子模块。根据 `files-from-teacher/Readme.md`，final exam 约 70% 来自主 session 1-7，部分题目来自 `files-from-teacher/BagOfQuestions/`；约 30% 来自 extra sessions，题目较简单。

所有复习产物遵循 English-first rule：考试题目、考试问法、可背答案、关键术语和公式解释先写英文，再给中文翻译或中文讲解。中文用于帮助理解，不能替代英文考试版。

复习主线：线性回归与梯度下降 -> 逻辑回归与 BCE -> 神经网络前向传播 -> softmax 和多分类 -> 反向传播与层接口 -> 优化器 -> 泛化、指标、正则化 -> dropout、early stopping、batch normalization -> extra sessions 速记。

## Source Map

- `files-from-teacher/Readme.md`：考试比例、闭卷要求、主 session 和 extra session 权重。
- `files-from-teacher/BagOfQuestions/`：最高优先级题源。
- `files-from-teacher/session-1/`：linear regression、MSE、gradient descent、polynomial regression、train/test split。
- `files-from-teacher/session-2/`：logistic regression、sigmoid、decision boundary、BCE、feature scaling。
- `files-from-teacher/session-3/`：neural network architecture、forward propagation、activation functions、softmax、one-hot、output layers。
- `files-from-teacher/session-4/`：backpropagation、chain rule、computation graph、Dense/ReLU layer、softmax cross-entropy、training step。
- `files-from-teacher/session-5/`：learning rate、mini-batch SGD、momentum、Adam、bias correction。
- `files-from-teacher/session-6/`：generalization、metrics、evaluation methods、bias-variance、L1/L2 regularization、basic distributions。
- `files-from-teacher/session-7/`：dropout、inverted dropout、early stopping、data augmentation、hyperparameter optimization、batch normalization。
- `review/source-index.md`：从老师子模块生成的快速索引。

## Knowledge Route

1. **Linear Regression From Scratch**
   掌握模型 `Y_hat = XW + b`、MSE、梯度、`np.dot`、`X.T`、shape 检查和参数更新。
   考试重点：填空代码、解释 `weights` 与 `bias`、debug elementwise multiplication、说明为什么更新要减去梯度。
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
   考试重点：从 linear regression 改成 logistic regression 的代码填空；`linear_model`、`y_predicted`、`y_predicted_cls` 区别。
   来源：`files-from-teacher/session-2/`，`BagOfQuestions-session-2-aj.md`，`BagOfQuestions-session-2-ak.md`

5. **Decision Boundary**
   掌握 threshold 0.5 时 `sigmoid(z)>0.5` 等价于 `z>0`，二维边界是 line。
   考试重点：把 `w1*x1 + w2*x2 + b = 0` 改写成 `x2 = a*x1 + c`；数值点分类；改变 threshold 后边界仍是 line。
   来源：`files-from-teacher/session-2/lecture-3-logistic-regression-decision-boundary.md`，`BagOfQuestions-session-2-ac.md`

6. **BCE vs MSE**
   掌握 binary cross-entropy formula、confident mistake penalty、why BCE is preferred over MSE in logistic regression。
   考试重点：写 one-example / average BCE；画 y=1 和 y=0 的 loss 曲线；解释 sigmoid saturation 下 MSE gradient 弱。
   来源：`files-from-teacher/session-2/lecture-4-logistic-regression-loss-bce-gd.md`，`BagOfQuestions-session-2-ad.md`

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
    考试重点：手算 `[2,1,0]` softmax；解释 `[102,101,100]` 和 `[2,1,0]` 概率相同；写 stable softmax。
    来源：`files-from-teacher/session-3/lecture-5-*` 到 `lecture-7-*`，`BagOfQuestions-session-3-ae.md`，`BagOfQuestions-session-3-af.md`

11. **Output Layer Depends on Task**
    掌握 regression、binary classification、multi-class classification 对应输出层和 loss。
    考试重点：说明什么时候用 linear output、sigmoid、softmax。
    来源：`files-from-teacher/session-3/lecture-5-neural-networks-output-layers-and-softmax.md`，`BagOfQuestions-session-3-ah.md`

12. **Backpropagation**
    掌握 chain rule、computation graph、forward values stored for backward、gradient flow。
    考试重点：解释 backprop 从 loss 回传到 parameters；Dense layer debug；ReLU backward；training step fill-in-the-blank。
    来源：`files-from-teacher/session-4/`，`BagOfQuestions-session-4-*`

13. **Layer Interface and Minimal NN Implementation**
    掌握 `forward`、`backward`、stored activations、parameter gradients、network training step。
    考试重点：为什么 forward 要保存输入/激活；layer interface 如何使 Dense、ReLU、SoftmaxCE 组合。
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
    考试重点：写 Adam formulas；解释 bias correction；比较 SGD、Momentum、Adam。
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
    考试重点：公式、几何解释、L1 为什么促稀疏、L2 为什么缩小权重。
    来源：`files-from-teacher/session-6/lecture-6-*` 到 `lecture-9-*`，`BagOfQuestions-session-6-ag.md` 到 `session-6-ai.md`

20. **Probability Distributions in ML**
    掌握 normal distribution、bivariate normal、covariance/correlation、Bernoulli/binomial、CLT、dropout as Bernoulli process。
    考试重点：解释 covariance matrix、correlation effect、CLT 与 mini-batch gradient noise。
    来源：`files-from-teacher/session-6/code-stats-distributions-*-math.md`，`BagOfQuestions-session-6-ak.md`

21. **Dropout**
    掌握 training-time random mask、inverted dropout scaling by `1/(1-p)`、eval mode no-op、implicit ensemble。
    考试重点：dropout fill-in-the-blank；期望值计算；为什么 train/eval mode 必须分开。
    来源：`files-from-teacher/session-7/lecture-1-dropout.md`，`lecture-2-dropout-1-p-multipy-or-devide.md`，`BagOfQuestions-session-7-ab.md`，`session-7-ac.md`，`session-7-ah.md`

22. **Other Regularization and Model Selection Tools**
    掌握 early stopping、data augmentation、hyperparameter optimization、batch normalization。
    考试重点：validation loss 上升时 early stopping；label-preserving transformation；grid search vs random search；BN train/inference behavior。
    来源：`files-from-teacher/session-7/lecture-3-*` 到 `lecture-6-*`，`BagOfQuestions-session-7-aa.md`，`session-7-ae.md`，`session-7-af.md`

23. **Extra Sessions Quick Review**
    按 Readme 约 30% easy questions 处理。重点掌握每个 extra topic 的 high-level definition、core mechanism、one simple example。
    包括 transformer/attention、QKV、positional encoding、masking、loss functions、RNN/seq2seq、tokenization、clustering/embeddings、autoencoder、ResNet/skip connections、GAN/adversarial robustness、quantization、ML app。
    来源：`files-from-teacher/session-*` extra materials，详见 `review/source-index.md`

## High-Priority Exam Patterns

- Code blanks: linear/logistic regression from scratch, sigmoid, predict threshold, Dense/ReLU/dropout/training step.
- Shape questions: `X`, `W`, `y_predicted`, `dw`, logits, softmax probabilities.
- Formula writing: MSE, BCE, softmax, cross-entropy, gradient update, Momentum, Adam, L1/L2.
- Hand computation: logistic one-step gradient descent, softmax probabilities, decision boundary classification, parameter count.
- Concept explanation: BCE vs MSE, feature scaling, nonlinearity, backprop, mini-batch trade-off, bias-variance, dropout expectation.
- Drawing/sketching: polynomial underfit/good/overfit, decision boundary, activation curves, softmax bar chart, bias-variance curve, L1/L2 geometry, dropout subnetworks.

## Review Method

每次只学一个小知识点，固定流程：

1. Read `review/source-index.md` to locate teacher materials.
2. Read the matching BagOfQuestions file first if available.
3. Read the matching session lecture/code file.
4. Extract or write the exam question in English first, then add a Chinese translation.
5. Produce an English exam-ready answer first, then add a Chinese translation.
6. Add a short Chinese explanation for understanding.
7. Do one similar practice question, also English first with Chinese translation.

## Assumptions

- 当前复习范围以 `files-from-teacher/Readme.md` 为准。
- 如果老师子模块更新，应重新生成 `review/source-index.md`。
