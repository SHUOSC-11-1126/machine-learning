# Exam Disclosures From Teacher Audio/Video

## Sources

- Media source: `老师关于考试的透露/06-15.m4a`
- Media source: `老师关于考试的透露/1643_1778674198.mp4`
- Baseline exam rule source: `files-from-teacher/Readme.md`
- Review index: `review/source-index.md`

Processing note: the recording audio had classroom/microphone mixing. A direct mono ASR pass missed most content, so the audio was split into chunks and reprocessed with left/right-channel speech enhancement. Project-related and research/project discussion was filtered out. Raw transcripts were kept only as temporary working files under `/tmp/ml-exam-asr`, not committed into this review note.

## Latest Scope Update

2026-06-17 teacher update:

- Main line: `files-from-teacher/session-0` to `files-from-teacher/session-7`.
- Extra questions: only `files-from-teacher/session-201-qkv-attention-mini-series`, `files-from-teacher/session-202-positional-encoding-mini-series`, and `files-from-teacher/session-203-masking-mini-series`.
- Other `files-from-teacher/session-*` directories are not assessed unless the teacher updates the scope again.
- Latest format update: code questions only test logistic regression; the exam mainly focuses on concepts, mathematical derivations, formulas, hand computation, and drawings/sketches.

中文：

- 主线是 `session-0` 到 `session-7`。
- Extra questions 只考 `session-201`、`session-202`、`session-203`。
- 其他 session 不考察，除非老师后续再次明确更新。
- 代码题只考 logistic regression；其他主要按概念、数学推导、公式、手算和画图准备。

## Cleaned Exam-Relevant Transcript Excerpts

These excerpts are ASR-cleaned and lightly normalized for readability. Non-exam project discussion was removed.

### From `06-15.m4a`

- "You should be able to know the main idea of dropout."
- "When validation loss is going up consistently, then we should stop so that we will not be overfitting."
- "You can go with data augmentation. That can be understood as a technique of regularization as well. You feed into your system more data so that your model can be more robust."
- "Even batch normalization can be understood as a technique of regularization."
- "Now it is time to go to another session. Of course, it will not be there for our final exam, so maybe you can ignore this session. What is GAN? Let's go from the fundamental definition." This points to GAN being ignorable for the final exam.
- "For classification, also for regression, we have the data, X, the features, and then we want to derive the label with a certain probability."

### From `1643_1778674198.mp4`

- "It is not so complicated. This year things will be easier."
- "I will be giving you a list of questions ... a bag/list of questions."
- "The things for the final exam are questions on general notions and a little bit of code."
- "For the transformer, Attention Is All You Need."
- "For example, I will ask: what is self-attention? One, two, three sentences should be enough."
- "Or maybe I will ask you to write down the math formula of attention."
- "Scaled dot-product attention."
- "Now let's go back to Session 5 ... neural-network code with SGD ... Adam."

### Peer Note Provided By Classmate

Status: second-hand noisy transcript, not original audio. Use only as a supporting signal when it matches `files-from-teacher/`.

Cleaned likely topics:

- sigmoid / softmax function
- TensorFlow Playground / Session 3 neural-network topics
- MoE, Mixture of Experts
- parameter counting
- ChatGPT-style vocabulary tables and shared weights
- converting tokens and embedding
- bias formula / drawing
- L1 and L2 regularization geometry
- Lasso and Ridge
- early stopping
- data augmentation / data processing: more data makes the model more robust
- writing formulas
- FFN / MLP was mentioned in the noisy note, but related `session-223` material is now out of scope under the 2026-06-17 update.

Matched teacher source paths:

- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ag.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-an.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ap.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ag.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ah.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ai.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-aa.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ae.md`

Out-of-scope matches under the 2026-06-17 update:

- `files-from-teacher/session-212-clustering-and-embedding-mini-series/lecture-clustering-12-embedding-layer-and-unembedding-layer-in-transformers.md`
- `files-from-teacher/session-223-ffn-mini-series/lecture-1-ffn-structure-and-role.md`
- `files-from-teacher/session-223-ffn-mini-series/lecture-3-ffn-as-knowledge-memory.md`

## Baseline Rules Still Apply

English:

- Final score is `0.7 * T + 0.3 * P`.
- Final exam `T`: around 70% from main sessions; latest teacher update defines the main line as sessions 0-7.
- Some questions come from `files-from-teacher/BagOfQuestions/`.
- Around 30% are easy questions from extra sessions, now scoped to sessions 201, 202, and 203 only.
- Closed book: no books, no sheets, no anything.
- Duration: 2 hours.

中文：

- 录音/视频透露的信息是补充线索；2026-06-17 老师范围更新进一步收窄 extra sessions。
- 复习优先级现在是：Readme -> BagOfQuestions -> main sessions 0-7 -> extra sessions 201/202/203。

## Cleaned Exam Signals

### 1. BagOfQuestions / Question List Is Very Important

English signal:

The teacher said he is preparing/updating a list of questions, described as a bag/list of questions for checking or practice. The questions are meant to be based on what students have learned, not too complicated, and useful later.

中文解释：

这强化了原本 Readme 的判断：`files-from-teacher/BagOfQuestions/` 是最高优先级题源之一。后续如果老师更新子模块，应先重新生成 `review/source-index.md`，再按 BagOfQuestions 复习。

Action:

- Prioritize every `files-from-teacher/BagOfQuestions/BagOfQuestions-session-*.md`.
- Treat BagOfQuestions questions as closest to final-exam style.

### 2. Final Exam Style: Concepts, Derivations, Drawings; Code Only Logistic Regression

English signal:

Earlier audio described final-exam questions as "general notions" and "a little bit of code". The latest update narrows that code part: code questions only test logistic regression. Most questions should be prepared as concepts, mathematical derivations, formulas, hand computations, and drawings/sketches.

中文解释：

考试不再按多处代码实现准备。代码题只看 logistic regression；其他内容按概念、数学推导、公式、手算、画图准备。

- concept explanation
- formulas
- simple hand computation
- logistic-regression code fill-in/debugging only
- shapes and training/inference behavior
- drawing/sketching

This matches `files-from-teacher/Readme.md`: main sessions include lecture, code, and a little practice.

### 3. Session 7 Regularization Is a Clear Signal

English signal:

The teacher mentioned dropout, early stopping, data augmentation, and batch normalization as regularization-related ideas.

Key possible exam questions:

1. What is the main idea of dropout?
2. What should we do when validation loss keeps increasing?
3. Why can data augmentation be understood as regularization?
4. How can batch normalization act as implicit regularization?

English answers:

- Dropout randomly removes hidden activations during training, so each update trains a different sub-network. This reduces co-adaptation and can improve generalization.
- If validation loss consistently increases after some epochs, we should use early stopping to stop near the epoch with the best validation loss and avoid overfitting.
- Data augmentation increases effective training diversity by applying label-preserving transformations, forcing the model to learn robust patterns instead of memorizing the original samples.
- Batch normalization can act as implicit regularization because mini-batch statistics vary during training, injecting small noise and making the model more robust.

中文翻译：

- Dropout 在训练时随机去掉一部分隐藏层激活，相当于每次训练一个不同的子网络，减少神经元之间的 co-adaptation，提高泛化。
- 如果 validation loss 持续上升，应使用 early stopping，在验证集损失最好的 epoch 附近停止，避免继续过拟合训练集。
- Data augmentation 通过不改变标签的变换扩大有效数据多样性，让模型学习稳健模式，而不是死记原始样本。
- Batch normalization 训练时使用 mini-batch 统计量，这些统计量会有波动，相当于引入轻微噪声，因此可能降低过拟合。

Teacher source paths:

- `files-from-teacher/session-7/lecture-1-dropout.md`
- `files-from-teacher/session-7/lecture-2-dropout-1-p-multipy-or-devide.md`
- `files-from-teacher/session-7/lecture-3-early-stopping.md`
- `files-from-teacher/session-7/lecture-4-data-augmentation.md`
- `files-from-teacher/session-7/lecture-6-batch-normalization.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-aa.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ab.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ac.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ah.md`

### 4. Transformer / Attention Extra Topic: Simple, But Memorize Formula

English signal:

For advanced topics such as Transformer / Attention Is All You Need, the teacher said questions should be very simple. Example question: "What is self-attention?" One to three sentences should be enough. Another possible question: write the math formula of attention.

Possible exam question:

What is self-attention?

English answer:

Self-attention lets each token in a sequence attend to other tokens in the same sequence. It computes attention weights from query-key similarities, then uses those weights to take a weighted sum of value vectors. This gives each token a context-dependent representation.

中文翻译：

Self-attention 让一个序列中的每个 token 关注同一序列中的其他 token。它用 query 和 key 的相似度计算 attention weights，再用这些权重对 value vectors 加权求和，使每个 token 得到依赖上下文的表示。

Possible formula question:

Write the scaled dot-product attention formula.

English answer:

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

The softmax is applied row-wise over the key positions.

中文翻译：

Scaled dot-product attention 的公式是：

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

softmax 按行对 key 位置归一化。

Teacher source paths:

- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-6-self-attention-mechanism.md`
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-7-matrix-form-of-attention.md`
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-17-self-attention-vs-cross-attention.md`

### 5. Session 5 Optimizers: Formulas and Concepts, Not Code Questions

English signal:

The video returned to Session 5 and mentioned neural-network code with SGD / Adam. This is now superseded by the latest update that code questions only test logistic regression. Session 5 is still worth reviewing for optimizer formulas, concepts, comparisons, and trajectory drawings, but not as code-fill material.

Review targets:

- full-batch GD vs mini-batch SGD
- momentum update
- Adam first moment, second moment, bias correction, and update rule
- optimization path drawings: GD vs SGD vs Momentum vs Adam
- learning-rate failure modes: too small vs too large

Teacher source paths:

- `files-from-teacher/session-5/code-my_nn-sgd-momentum-adam.md`
- `files-from-teacher/session-5/code-my_nn-sgd-momentum-adam.py`
- `files-from-teacher/session-5/lecture-3-from-gd-to-sgd.md`
- `files-from-teacher/session-5/lecture-4-momentum.md`
- `files-from-teacher/session-5/lecture-5-adam.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-aa.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ab.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ac.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ad.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ae.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-af.md`
- `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ag.md`

### 6. GAN: Oral Disclosure Says Ignore For Final

English signal:

In the recording, immediately before discussing GAN from a fundamental definition, the teacher said that this session would not be in the final exam and could be ignored. This is stronger than "low priority": for final-exam review, GAN should be treated as not required unless a later teacher update explicitly brings it back.

Important boundary: the 2026-06-17 teacher update now explicitly says only sessions 201, 202, and 203 are extra-question scope. GAN / session-105 is therefore out of scope, along with the other non-201/202/203 extra sessions.

中文解释：

更准确的结论不是“GAN 降低优先级”，而是：按这段老师口头透露和 2026-06-17 最新范围，GAN / session-105 不考察。Extra 只保留 session-201、session-202、session-203。

## Filtered Out

The following content was removed from the review summary:

- project integration discussion
- teacher research interests unrelated to the final exam
- unclear/noisy ASR fragments that could not be cross-confirmed
- generic classroom management comments

Uncertain ASR fragments such as unclear architecture terms were not used as exam priorities.

## Practical Review Order After This Disclosure

1. Review `files-from-teacher/BagOfQuestions/` first.
2. For main sessions, keep the updated route: sessions 0-7 are the core.
3. Add special attention to Session 7 regularization answers: dropout, early stopping, data augmentation, batch normalization.
4. Review Session 5 optimizer formulas and concepts: SGD, Momentum, Adam; do not prioritize Session 5 code blanks.
5. For extra questions, review only sessions 201, 202, and 203.
6. Do not spend final-review time on GAN or other out-of-scope sessions unless a later teacher update explicitly brings them back.
