# Audit: `files-from-classmate/ml-revision-all.pdf`

## Status

This PDF is a classmate-produced revision document, created on 2026-06-18. It is useful as a practice and answer-template source, but it is not higher authority than:

1. `files-from-teacher/Readme.md`
2. `files-from-teacher/BagOfQuestions/`
3. The teacher range recordings already cleaned in `review/highest-priority-exam-scope-2026-06-17.md`

Extraction note: the PDF is text-based, 69 pages, and did not require OCR. Extracted working text was kept under `/tmp/ml-classmate-pdf/ml-revision-all.txt`.

## Overall Verdict

The document is mostly aligned with the current high-priority review direction and is useful for fast memorization. Its best value is that it already gives English exam answers plus Chinese explanations for many BagOfQuestions items.

However, it should be used as a secondary checklist, not as the source of truth. It contains one stale line saying progress is `201-205`; current extra scope remains only `201/202/203`.

## Page Map

- Page 1: overview and claimed range.
- Page 12: Session 2 not-tested list.
- Page 13: Session 3 starts.
- Page 28: Session 3 not-tested list.
- Page 29: Session 5 starts.
- Page 42: Session 6 starts.
- Page 47: Session 6 quick card.
- Page 51: Session 7 starts.
- Page 59: Session 7 quick card.
- Page 62: Extra 201 starts.
- Page 64: Extra 202 starts.
- Page 66: Extra 203 starts.

## Useful To Adopt For Practice

### Session 2: Logistic Regression Code

Use this part heavily.

English checklist:

- `return 1 / (1 + np.exp(-z))`
- `n_samples, n_features = X.shape`
- `self.weights = np.zeros(n_features)`
- `linear_model = np.dot(X, self.weights) + self.bias`
- `y_predicted = self._sigmoid(linear_model)`
- `self.weights -= self.lr * dw`
- `self.bias -= self.lr * db`

中文：这和最高优先级录音吻合。重点是 `fit`、`sigmoid`、`linear_model`、`n_features` 和 update sign。

Current exam handling:

- `dw` / `db` exact mathematical derivation is not tested.
- `dw` / `db` code lines may still be useful only because update lines refer to them.
- `predict` should be treated as understanding-only, not the main code target.

Teacher source:

- `files-from-teacher/session-2/code-my_logistic_regression.py`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-bh.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-aj.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ak.md`

### Session 2: TensorFlow Playground / Feature Engineering

Use this part heavily.

English checklist:

- Raw `x_1, x_2` logistic regression gives a linear boundary.
- Ring/circle data needs quadratic features such as `x_1^2` and `x_2^2`.
- Degree-1 boundary: underfitting / high bias.
- Smooth quadratic boundary: good fit.
- Very wiggly high-capacity boundary: overfitting / high variance.
- Adding features, neurons, and hidden layers increases model capacity.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ag.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ah.md`
- `files-from-teacher/session-6/lecture-5-model-selection-bias-variance.md`

### Session 3: Softmax And Parameter Counting

Use this part heavily.

English checklist:

- Softmax formula:

$$
\operatorname{softmax}(z)_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

- Shift invariance:

$$
\operatorname{softmax}(z+c)=\operatorname{softmax}(z)
$$

because `e^c` cancels from numerator and denominator.

- Stable softmax:

$$
p_i=\frac{e^{z_i-\max(z)}}{\sum_j e^{z_j-\max(z)}}
$$

- Dense layer parameter count: `in_features * out_features + out_features`.
- Embedding table: usually `vocab_size * embedding_dim`, no bias.
- MoE: count each expert plus the router.
- FFN / MLP: `d_model -> 4 d_model -> d_model`, one hidden expanded layer.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-af.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ag.md`

### Session 5: Optimizer Formulas And Trajectory Drawings

Use this part heavily.

English checklist:

- GD / mini-batch SGD update form.
- Momentum formula and intuition.
- Adam first moment, second moment, bias correction, and final update.
- Draw loss contours as ellipses.
- Draw GD stable path, SGD zig-zag path, Momentum smoother path, Adam adaptive path.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ad.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-af.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ag.md`

### Session 6: L1/L2 And Bias-Variance

Use this part heavily.

English checklist:

- L1:

$$
\mathcal{L}_{train}(W)+\lambda\sum_j |W_j|
$$

- L2:

$$
\mathcal{L}_{train}(W)+\lambda\sum_j W_j^2
$$

- L1 = diamond; first touch often at an axis corner; sparse solution.
- L2 = circle; smooth shrinkage.
- Bias-variance curve: training error decreases, validation error is U-shaped.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ah.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ai.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-af.md`

### Session 7: Dropout, Inverted Dropout, Early Stopping, Data Augmentation

Use this part heavily.

English checklist:

- Dropout randomly zeroes activations during training.
- Inverted dropout scales kept activations by `1 / (1-p)`.
- During inference, dropout is off.
- Early stopping: validation loss decreases then rises; stop near the best validation-loss epoch.
- Patience: wait for `k` non-improving epochs before stopping.
- Data augmentation: label-preserving transformations such as rotation, crop, flip.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-aa.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ab.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ac.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ah.md`

### Extra 201/202/203

Use this part heavily.

English checklist:

- 201: `Attention(Q,K,V)=softmax(QK^T / sqrt(d_k))V`; self-attention vs cross-attention.
- 202: sinusoidal positional encoding; `i=0` gives sine channels `0` and cosine channels `1`; combine by `z_i = x_i + PE_i`.
- 203: causal mask validity is `j <= i`; masked positions are set to `-inf` before softmax; prevents target leakage.

Teacher source:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-201-ee.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-202-ee.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-203-ee.md`

## Corrections / Warnings

### 1. `201-205` Is Stale

The PDF overview says progress is `Session 3,5,6,7,201-205`, but current extra scope is only `201/202/203`.

Action: ignore `201-205`; use only 201, 202, and 203.

### 2. BCE Is Out Of Scope

The PDF correctly says BCE / CE-vs-BCE is not tested under the latest scope. This matches the current clarification.

Action: do not use `BagOfQuestions-session-2-ad.md` for current exam-priority practice.

### 3. Session 1 / Session 4 Not-Tested Claims

The PDF says Session 1 / Session 4 are not tested. Session 1 remains low priority rather than excluded. Session 4 is now explicitly excluded by the later confirmed teacher update.

Action:

- Treat Session 1 as low priority, consistent with the teacher range recording.
- Do not prepare any Session 4 code, backpropagation, or conceptual material for the current exam.

### 4. `xlsx 总表` Is Referenced But Not Present Here

The PDF repeatedly says it is aligned to an `xlsx 总表`. That spreadsheet is not included in this repo path during this audit.

Action: treat the `xlsx`-based narrowing as useful but secondary until the actual spreadsheet is available.

## Recommended Use

Use the PDF as a fast answer-template source after studying each topic from `files-from-teacher/`.

Best workflow:

1. Start from `review/highest-priority-exam-scope-2026-06-17.md`.
2. For a topic, read the matching `files-from-teacher/BagOfQuestions/...` file.
3. Use `files-from-classmate/ml-revision-all.pdf` to compare answer wording.
4. Memorize the English answer template.
5. Use the Chinese explanation only to understand why the answer works.
