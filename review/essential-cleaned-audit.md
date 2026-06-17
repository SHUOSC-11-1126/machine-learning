# Audit: `老师关于考试的透露/essential-cleaned.txt`

## Status

This file is a second-hand cleaned note from classmate material. It is useful as a checklist, but it is not a higher-priority source than `files-from-teacher/` or the 2026-06-17 teacher scope update.

Current scope remains:

- Main line: `files-from-teacher/session-0` to `files-from-teacher/session-7`.
- Extra questions: only `files-from-teacher/session-201-qkv-attention-mini-series/`, `files-from-teacher/session-202-positional-encoding-mini-series/`, and `files-from-teacher/session-203-masking-mini-series/`.
- Code questions: logistic regression only.

中文：这份同学资料只能当查漏补缺线索，不能用来扩大考试范围。

## Useful Gaps To Add To Review

### 1. Early Stopping Drawing Is High Priority

Use this as a drawing-practice item, not only a concept item.

English checklist:

- Draw training and validation loss curves.
- Mark the epoch with the best validation loss.
- Explain patience.
- Explain why stopping at the lowest training loss is a bad idea.
- Explain why early stopping is a regularization method.

中文：early stopping 不只是会解释，还要会画图：train loss 持续下降，validation loss 先降后升，在 validation loss 最低处标出 best epoch / stop point。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-aa.md`
- `files-from-teacher/session-7/lecture-3-early-stopping.md`

### 2. L1/L2 Need Formula Plus Geometry

The classmate note correctly reinforces that L1/L2 should be prepared as formula + drawing.

English checklist:

- Write L1 objective: data loss plus `lambda * ||W||_1`.
- Write L2 objective: data loss plus `lambda * ||W||_2^2`.
- Know names: L1 = Lasso, L2 = Ridge.
- Draw data-loss ellipses with L1 diamond and L2 circle.
- Mark where an ellipse first touches the constraint region.
- Explain why L1 can produce sparse weights and L2 usually shrinks weights smoothly.

中文：L1/L2 要按“公式、图、直觉”三件套准备。图里重点是 first touch：L1 的菱形角点更容易碰到坐标轴，所以容易得到 0 权重。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ah.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ai.md`
- `files-from-teacher/session-6/lecture-6-*`
- `files-from-teacher/session-6/lecture-7-*`
- `files-from-teacher/session-6/lecture-8-*`
- `files-from-teacher/session-6/lecture-9-*`

### 3. Logistic Regression Is Still The Only Code Target

The note's Session 2 points match the latest format update: logistic regression code is the only code target.

English checklist:

- `linear_model = np.dot(X, self.weights) + self.bias`
- `y_predicted = sigmoid(linear_model)`
- `dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))`
- `db = (1 / n_samples) * np.sum(y_predicted - y)`
- update with minus gradient
- prediction threshold, especially strict `> 0.5`
- BCE formula and BCE curves for `y=1` and `y=0`
- CE vs BCE at the conceptual level

中文：代码复习只把 logistic regression 做熟；其他 session 的代码只作为理解概念，不按代码填空准备。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ad.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-aj.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ak.md`
- `files-from-teacher/session-2/`

### 4. Optimizer Drawings And Formulas Should Be Practiced

Session 5 should be reviewed as formulas, concepts, comparisons, and sketches, not as code.

English checklist:

- Compare full-batch GD, SGD, mini-batch SGD.
- Write momentum update idea.
- Write Adam first moment, second moment, bias correction, and update rule.
- Draw optimizer trajectories: SGD zig-zag/noise, momentum smoothing, Adam adaptive movement.
- Explain too-small and too-large learning rates.

中文：同学资料里提到 optimizer zig-zag 图，这个值得补进复习。AdamW 属于 `session-205`，按当前范围不作为考试必备。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-aa.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ab.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ac.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ad.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-af.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ag.md`

### 5. Extra 202 Includes A Small Calculation

The useful correction is not just "know positional encoding"; prepare the specific `i = 0` computation from BagOfQuestions.

English checklist:

- Write the sinusoidal positional encoding formulas.
- For position `i = 0`, sine channels are `sin(0) = 0`; cosine channels are `cos(0) = 1`.
- Explain why this does not depend on `d_model`.
- Write the combination formula: `h_i = x_i + p_i`.
- Explain why the same word at different positions can have different combined vectors.

中文：PE 的计算题大概率很小，重点是 `i=0` 时偶数维是 0、奇数维是 1，以及 embedding 和 positional vector 是相加。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-202-ee.md`
- `files-from-teacher/session-202-positional-encoding-mini-series/`

### 6. Extra 203 Causal Mask Needs Matrix-Level Detail

The classmate note correctly points to the `-inf` mask detail, but use the teacher BagOfQuestions notation as the source of truth.

English checklist:

- Causally valid attention requires `j <= i`.
- For `i = 2` and `n = 4`, valid key positions are `j = 0, 1, 2`.
- Masked future positions are set to `-inf` before softmax.
- Since `exp(-inf) = 0`, masked attention weights become zero.
- Causal masking prevents target leakage during training and is required even when full sequences are available.

中文：矩阵图要画成下三角可见、上三角屏蔽。实现上是把 mask 加到 attention logits，再做 softmax。

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-203-ee.md`
- `files-from-teacher/session-203-masking-mini-series/`

## Incorrect Or Out-Of-Scope Items

- The note says it was organized by `session 1-7 + 201-205`; this is outdated/wrong for current scope. Correct extra scope is `201/202/203` only.
- `session-204` loss-function material is out of scope unless the teacher updates the range. CE/BCE should be reviewed through main `session-2`, not as extra 204.
- `session-205` AdamW, MoE, fast/linear attention, and large-model training details are out of scope unless the teacher updates the range.
- `session-223` FFN/MLP and parameter counting are out of scope unless the teacher updates the range.
- The note's "session4 not tested" line conflicts with the current main-line scope `session-0` to `session-7`. Do not remove backpropagation from review unless the teacher confirms it directly.
- The note's "session1 almost not tested" can justify lower time allocation, but not deletion. Session 1 remains in the main line.
- Old claims that dropout is not tested should be treated as obsolete. Current usable signal is that dropout and early stopping should be reviewed, with early stopping drawing especially important.

## Action

Use this audit to strengthen the review plan, but keep the source hierarchy unchanged:

`files-from-teacher/Readme.md` -> `files-from-teacher/BagOfQuestions/` -> main sessions `0-7` -> extra sessions `201/202/203` -> cleaned audio/video notes -> classmate notes.
