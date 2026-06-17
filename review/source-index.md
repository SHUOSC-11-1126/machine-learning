# 机器学习复习资料索引

本索引从 `files-from-teacher/` 子模块生成，并记录 2026-06-17 老师最新口头范围更新。该子模块由老师维护，是考试复习的唯一最高优先级资料。

## Latest Scope Update

- 2026-06-17 teacher update: `files-from-teacher/session-0` to `files-from-teacher/session-7` are the main line.
- Extra questions only use `files-from-teacher/session-201-qkv-attention-mini-series`, `files-from-teacher/session-202-positional-encoding-mini-series`, and `files-from-teacher/session-203-masking-mini-series`.
- Other `files-from-teacher/session-*` directories are outside the current final-exam scope unless the teacher updates the scope again.
- Latest exam-format update: code questions only test logistic regression; most questions focus on concepts, mathematical derivations, and drawings/sketches.

## Exam Signal From Readme

- Final score = `0.7 * T + 0.3 * P`.
- Final exam: about 70% from main sessions; latest teacher update defines the main line as sessions 0-7.
- Some exam questions will come from `files-from-teacher/BagOfQuestions/`.
- About 30% from extra sessions, now scoped to sessions 201, 202, and 203 only.
- Closed-book exam: no books, sheets, or other materials.

## Priority Order

1. `files-from-teacher/Readme.md` exam rules.
2. `files-from-teacher/BagOfQuestions/` question source.
3. `files-from-teacher/session-0` to `session-7` lecture, practice, and code materials; code-question preparation only targets logistic regression.
4. Extra session materials only from `session-201`, `session-202`, and `session-203`.

## Main Sessions

### Session 0

- BagOfQuestions files: 0
- Markdown materials: 6
  - `files-from-teacher/session-0/lecture-0-notation-for-session-1-to-session-7.md` (lecture): Notation for Sessions 1–7
  - `files-from-teacher/session-0/lecture-Left-Side-vs-Right-Side-Projection.md` (lecture): 1. Left-Side vs. Right-Side Projection
  - `files-from-teacher/session-0/lecture-breaking-changes-in-NN-history.md` (lecture): Breaking Changes in Neural Network History
  - `files-from-teacher/session-0/lecture-notation-guideline.md` (lecture): lecture-notation-guideline
  - `files-from-teacher/session-0/lecture-what-is-ml-dl.md` (lecture): What is Machine Learning and Deep Learning
  - `files-from-teacher/session-0/lecture-why-nn-from-srcatch.md` (lecture): lecture-why-nn-from-srcatch

### Session 1

- BagOfQuestions files: 5
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-ae.md`: Linear Regression from Scratch
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-af.md`: Debug Linear Regression from Scratch
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-ah.md`: Polynomial Regression as Feature Engineering
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-aj.md`: GitHub Pull Request Workflow
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-ak.md`: Linear Regression Fit Method Details
- Markdown materials: 9
  - `files-from-teacher/session-1/code-my_linear_regression.md` (code): Linear Regression from Scratch
  - `files-from-teacher/session-1/lecture-1-introduction-linear-regression.md` (lecture): Linear Regression
  - `files-from-teacher/session-1/lecture-2-simple-linear-regression-gd.md` (lecture): Simple Linear Regression — Gradient Descent
  - `files-from-teacher/session-1/lecture-3-multiple-linear-regression.md` (lecture): Multiple Linear Regression
  - `files-from-teacher/session-1/lecture-4-polynomial-linear-regression.md` (lecture): Polynomial Linear Regression
  - `files-from-teacher/session-1/lecture-5-train-test-splitting.md` (lecture): Train / Test Splitting
  - `files-from-teacher/session-1/lecture-URLs.md` (lecture): lecture-URLs
  - `files-from-teacher/session-1/practice-1-basic-setup.md` (practice): Environment Setup Guide
  - `files-from-teacher/session-1/practice-2-git-github-workflow.md` (practice): Practice Git and GitHub Workflow

### Session 2

- BagOfQuestions files: 11
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-aa.md`: Logistic Regression Boundary and Losses
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ab.md`: GitHub CI/CD/Actions/Release Project
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ac.md`: Decision Boundary; Numerical Boundary
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ad.md`: Binary Cross-Entropy Loss; BCE versus MSE
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ae.md`: One Gradient Descent Step by Hand in Logistic Regression
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ag.md`: TensorFlow Playground Feature Engineering for Curved and Ring-Shaped Boundaries
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ah.md`: Two Spirals in TensorFlow Playground and Representation Learning
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ai.md`: Probability, Threshold, and Business Meaning; Link to the Decision Boundary
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-aj.md`: Compare Linear and Logistic Regression Code From Scratch
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-ak.md`: Logistic Regression Predict Method
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-2-bh.md`: Logistic Regression from Scratch
- Markdown materials: 10
  - `files-from-teacher/session-2/code-my_logistic_regression.md` (code): Logistic Regression from Scratch
  - `files-from-teacher/session-2/lecture-1-logistic-regression-from-regression-to-classification.md` (lecture): From Regression to Classification
  - `files-from-teacher/session-2/lecture-2-logistic-regression-sigmoid-model.md` (lecture): The Sigmoid Model
  - `files-from-teacher/session-2/lecture-3-logistic-regression-decision-boundary.md` (lecture): Decision Boundary
  - `files-from-teacher/session-2/lecture-4-logistic-regression-loss-bce-gd.md` (lecture): Loss Function and Gradient Descent in Logistic Regression
  - `files-from-teacher/session-2/lecture-5-feature-scaling.md` (lecture): Feature Scaling
  - `files-from-teacher/session-2/lecture-URLs.md` (lecture): lecture-URLs
  - `files-from-teacher/session-2/practice-1-github-with-ssh-instead-of-https.md` (practice): Setting Up SSH for GitHub
  - `files-from-teacher/session-2/practice-2-ci-cd-github-actions-release.md` (practice): Setting Up CI/CD with GitHub Actions and Release Functionality
  - `files-from-teacher/session-2/practice-3-cv-with-ci-cd.md` (practice): practice-3-cv-with-ci-cd

### Session 3

- BagOfQuestions files: 9
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ac.md`: Activation Functions
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ae.md`: Softmax Calculation and Probability Interpretation
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-af.md`: Softmax Shift Invariance and Numerical Stability
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ag.md`: DeepSeek Mini Mixture-of-Experts
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ah.md`: Output Layers Depend on the Task
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-aj.md`: One-Hot Labels for Multiclass Classification
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-an.md`: ChatGPT-Style Tiny Language Model Parameter Counting
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-ap.md`: ChatGPT Vocabulary Table and Shared Weights
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-3-bm.md`: DeepSeek-Style Model Size Comparison
- Markdown materials: 12
  - `files-from-teacher/session-3/code-linear-regression-and-logistic-regression-with-pytorch.md` (code): Linear & Logistic Regression with PyTorch
  - `files-from-teacher/session-3/lecture-1-neural-networks-from-logistic-regression-to-nn.md` (lecture): Neural Networks — From Logistic Regression to Deep Models
  - `files-from-teacher/session-3/lecture-2-neural-networks-architecture-and-notation.md` (lecture): Neural Networks — Architecture and Notation
  - `files-from-teacher/session-3/lecture-3-neural-networks-forward-propagation.md` (lecture): Neural Networks — Forward Propagation
  - `files-from-teacher/session-3/lecture-4-neural-networks-activation-functions.md` (lecture): Neural Networks — Activation Functions
  - `files-from-teacher/session-3/lecture-5-neural-networks-output-layers-and-softmax.md` (lecture): Neural Networks — Output Layers and Softmax
  - `files-from-teacher/session-3/lecture-6-softmax-deep-dive.md` (lecture): Deep Dive into Softmax
  - `files-from-teacher/session-3/lecture-7-one-hot-encoding-deep-dive.md` (lecture): One-Hot Encoding Deep Dive
  - `files-from-teacher/session-3/lecture-URL.md` (lecture): lecture-URL
  - `files-from-teacher/session-3/practice-huggingface-with-github-ci-cd.md` (practice): ML Project: GitHub CI/CD → Hugging Face
  - `files-from-teacher/session-3/practice-pickling-of-a-model.md` (practice): Pickling in Python: Saving and Loading Data and Models
  - `files-from-teacher/session-3/practice-tensorflow-playground.md` (practice): Spiral Classification in TensorFlow Playground

### Session 4

- BagOfQuestions files: 11
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-aa.md`: MNIST Network Architecture and Parameter Counting
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-ac.md`: Numerically Stable Softmax
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-ad.md`: Categorical Cross-Entropy Formula
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-ae.md`: ReLU Layer Fill-in-the-Blank
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-af.md`: Debug the Dense Layer
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-ah.md`: Alternative Activation Layers
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-ai.md`: The Layer Interface
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-au.md`: Activation Layer Variants
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-bb.md`: Why Sigmoid Plus Binary Cross-Entropy Simplifies
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-be.md`: Forward Function and Stored Activations
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-4-bf.md`: Training Step Fill-in-the-Blank
- Markdown materials: 14
  - `files-from-teacher/session-4/code-connections-with-lecture.md` (code): Code Connections: How Math Becomes Python Implementation
  - `files-from-teacher/session-4/code-my_nn-softmax_crossentropy_with_logits.md` (code): Softmax Cross-Entropy with Logits: Full Batch Gradient Descent
  - `files-from-teacher/session-4/code-my_nn.md` (code): Neural Networks from Scratch (Baseline)
  - `files-from-teacher/session-4/code-my_nn_design_philosophy.md` (code): Design and Implementation of a Minimal Neural Network for MNIST
  - `files-from-teacher/session-4/lecture-1-backprop-from-forward-to-gradient.md` (lecture): Backpropagation — From Forward Computation to Gradients
  - `files-from-teacher/session-4/lecture-2-backprop-chain-rule.md` (lecture): Backpropagation — The Core: Chain Rule
  - `files-from-teacher/session-4/lecture-3-backprop-on-computation-graph.md` (lecture): Backpropagation on Computation Graphs
  - `files-from-teacher/session-4/lecture-4-backprop-in-linear-regression-and-logistic-regression.md` (lecture): Backpropagation in Linear Regression and Logistic Regression
  - `files-from-teacher/session-4/lecture-5-backprop-in-neural-networks.md` (lecture): Backpropagation in Neural Networks
  - `files-from-teacher/session-4/lecture-6-key-terminology-of-machine-learning.md` (lecture): Core Terminology of Machine Learning
  - `files-from-teacher/session-4/practice-pytest-TDD-1.md` (practice): PyTest & TDD
  - `files-from-teacher/session-4/practice-pytest-TDD-2.md` (practice): Linear Regression from Scratch using TDD & PyTest
  - `files-from-teacher/session-4/practice-pytest-TDD-3.md` (practice): Logistic Regression from Scratch using TDD & PyTest
  - `files-from-teacher/session-4/reading-material-metaphor-nn-and-politics.md` (reading): Neural Networks Explained Through Democratic Politics

### Session 5

- BagOfQuestions files: 7
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-aa.md`: From Gradient to Parameter Update
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ab.md`: Batch Size Trade-Off
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ac.md`: Full-Batch Gradient Descent versus Mini-Batch SGD
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ad.md`: Bias Correction in Adam
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ae.md`: Momentum
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-af.md`: Adam Formulas — First Moment, Second Moment, Update
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-5-ag.md`: Comparison of Gradient Optimization Algorithms
- Markdown materials: 7
  - `files-from-teacher/session-5/code-my_nn-sgd-momentum-adam.md` (code): Neural Networks from Scratch — Session 5 (SGD + Momentum + Adam)
  - `files-from-teacher/session-5/lecture-1-optimization-from-gradient-to-update.md` (lecture): Optimization — From Gradient to Parameter Update
  - `files-from-teacher/session-5/lecture-2-learning-rate.md` (lecture): Optimization — Learning Rate
  - `files-from-teacher/session-5/lecture-3-from-gd-to-sgd.md` (lecture): Optimization — From Gradient Descent to Mini-Batch SGD
  - `files-from-teacher/session-5/lecture-4-momentum.md` (lecture): Optimization — Momentum
  - `files-from-teacher/session-5/lecture-5-adam.md` (lecture): Optimization — Adam (Adaptive Moment Estimation)
  - `files-from-teacher/session-5/practice-debugging-my-nn.md` (practice): Python Debugging: `practice-my_nn_with_bugs.py`

### Session 6

- BagOfQuestions files: 6
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-aa.md`: Generalization, Overfitting, and Data Splits
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ab.md`: Metrics Under Class Imbalance and Task-Dependent Trade-offs
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-af.md`: Bias–Variance Tradeoff Drawing
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ah.md`: L1 and L2 Regularization — Formula, Geometry, and Intuition
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ai.md`: L1 and L2 Regularization Formulas
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-6-ak.md`: Visualizing and Analyzing a Bivariate Normal Distribution
- Markdown materials: 17
  - `files-from-teacher/session-6/README.md` (other): Simple Neural Network UTSEUS (simple_nn_utseus)
  - `files-from-teacher/session-6/code-stats-distributions-1-math.md` (code): Normal Distribution and Bivariate Normal Distribution
  - `files-from-teacher/session-6/code-stats-distributions-1.md` (code): Normal Distributions and Bivariate Normal Distributions
  - `files-from-teacher/session-6/code-stats-distributions-2-math.md` (code): Bernoulli Distribution and Binomial Distribution
  - `files-from-teacher/session-6/code-stats-distributions-2.md` (code): Binomial Distribution, Central Limit Theorem, and Bernoulli Processes
  - `files-from-teacher/session-6/lecture-1-model-selection-generalization.md` (lecture): Generalization
  - `files-from-teacher/session-6/lecture-2-model-selection-classification-metrics.md` (lecture): Confusion Matrix and Classification Metrics
  - `files-from-teacher/session-6/lecture-3-model-selection-regression-metrics.md` (lecture): Regression Metrics
  - `files-from-teacher/session-6/lecture-4-model-selection-evaluation-methods.md` (lecture): Evaluation Methods
  - `files-from-teacher/session-6/lecture-5-model-selection-bias-variance.md` (lecture): Bias–Variance Tradeoff
  - `files-from-teacher/session-6/lecture-6-L1-L2-regularization-formulation.md` (lecture): L1/L2 Regularization — Formulation
  - `files-from-teacher/session-6/lecture-7-L1-L2-regularization-optimization-view.md` (lecture): L1/L2 Regularization — Optimization View
  - `files-from-teacher/session-6/lecture-8-L1-L2-regularization-geometry-and-effect.md` (lecture): L1/L2 Regularization — Geometry and Effect
  - `files-from-teacher/session-6/lecture-9-L1-L2-first-touch-geometry.md` (lecture): L1 vs L2 Regularization — Geometry of Norm Balls and the First-Touch Principle
  - `files-from-teacher/session-6/practice-python-packaging.md` (practice): Converting a Neural Network Script into a Python Package
  - `files-from-teacher/session-6/practice-why-python-packaging.md` (practice): Why Python Packaging Is Useful — 15 Practical Reasons
  - `files-from-teacher/session-6/reading-material-why-we-do-not-want-large-weights.md` (reading): Why We Don’t Want Large Weights (Optional)

### Session 7

- BagOfQuestions files: 6
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-aa.md`: A Neural Network That Memorizes Too Well; Early Stopping with Validation Loss
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ab.md`: Dropout as Training Many Sub-Networks
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ac.md`: Inverted Dropout Formula and Expectation
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ae.md`: Data Augmentation as Label-Preserving Transformation
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-af.md`: Hyperparameter Configurations and Failure Modes
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-7-ah.md`: Dropout Fill-in-the-Blank
- Markdown materials: 9
  - `files-from-teacher/session-7/code-my_nn-dropout-L1-L2.md` (code): Neural Networks from Scratch — Session 7 (Dropout, L1/L2)
  - `files-from-teacher/session-7/lecture-1-dropout.md` (lecture): Dropout
  - `files-from-teacher/session-7/lecture-2-dropout-1-p-multipy-or-devide.md` (lecture): Why Inverted Dropout Divides by $1-p$
  - `files-from-teacher/session-7/lecture-3-early-stopping.md` (lecture): Early Stopping
  - `files-from-teacher/session-7/lecture-4-data-augmentation.md` (lecture): Data Augmentation
  - `files-from-teacher/session-7/lecture-5-hyperparameter-optimization.md` (lecture): Hyperparameter Optimization
  - `files-from-teacher/session-7/lecture-6-batch-normalization.md` (lecture): Batch Normalization
  - `files-from-teacher/session-7/practice-dropout-relu-elu-leaky_relu.md` (practice): ReLU, Dropout, and the "Dead Neuron" Problem
  - `files-from-teacher/session-7/reading-material-why-random-search-works-well.md` (reading): reading-material-why-random-search-works-well

## Extra Sessions

### session-201-qkv-attention-mini-series

- BagOfQuestions files: 1
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-201-ee.md`: Self-Attention vs Cross-Attention

- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-0-notation-guideline-for-qkv-mini-series.md`: Notation Guideline for the QKV Attention Mini-Series (Exhaustive Edition)
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-1-from-static-to-dynamic-weights.md`: From Static to Dynamic Weights
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-10-dot-product-as-similarity.md`: Dot Product as Similarity
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-11-softmax-as-normalized-selection.md`: Softmax as Multi-Dimensional Sigmoid
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-12-log-sum-exp-trick.md`: Log-Sum-Exp Trick in Softmax
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-13-multi-head-attention.md`: Multi-Head Attention
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-14-mha-in-transformer-2017.md`: Multi-Head Attention in the Original Transformer (2017)
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-15-encoder-decoder-architecture.md`: Encoder-Decoder Architecture
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-16-cross-attention.md`: Cross-Attention
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-17-self-attention-vs-cross-attention.md`: Self-Attention vs Cross-Attention
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-18-how-a-transformer-translates.md`: How a Transformer Translates
- `files-from-teacher/session-201-qkv-attention-mini-series/lecture-19-the-many-names-of-encoder-output.md`: The Many Names of Encoder Output
- ... 12 more markdown files

### session-202-positional-encoding-mini-series

- BagOfQuestions files: 1
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-202-ee.md`: Sinusoidal Positional Encoding and the Attention Pipeline

- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-0-notation-guideline-for-pe-mini-series.md`: Notation Guideline for the Positional Encoding Mini-Series
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-1-why-order-matters.md`: Positional Encoding: Why Order Matters
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-2-order-in-rnn-and-cnn.md`: Positional Encoding: How RNN and CNN Encode Order Implicitly
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-3-add-position-signal.md`: Positional Encoding: Add Position as an Input Signal
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-4-what-is-a-good-position-representation.md`: What Is a Good Position Representation?
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-5-sine-and-cosine-as-position.md`: Positional Encoding: Sine and Cosine as Position Signals
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-6-multi-frequency-encoding.md`: Positional Encoding: Multi-Frequency Construction
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-7-sinusoidal-formulation.md`: Positional Encoding: Standard Sinusoidal Formula
- `files-from-teacher/session-202-positional-encoding-mini-series/lecture-pe-8-why-addition-works.md`: Positional Encoding: Why Addition Works

### session-203-masking-mini-series

- BagOfQuestions files: 1
  - `files-from-teacher/BagOfQuestions/BagOfQuestions-session-203-ee.md`: Causal Mask for Autoregressive Decoding

- `files-from-teacher/session-203-masking-mini-series/code-networkx-1.md`: NetworkX & Graph Theory
- `files-from-teacher/session-203-masking-mini-series/lecture-0-notation-guideline-for-masking-mini-series.md`: Notation Guideline for the Masking Mini-Series
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-1-why-attention-needs-constraints.md`: Why Attention Needs Constraints
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-2-attention-as-a-graph.md`: Attention as a Graph
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-3-causal-mask-autoregressive.md`: Causal Mask and Autoregressive Modeling
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-4-padding-mask-variable-length.md`: Padding Mask and Variable-Length Sequences
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-5-combining-masks.md`: Combining Masks in Attention
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-6-cross-attention.md`: Cross-Attention Masking
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-7-masking-in-transformers.md`: Masking in Transformer Architectures
- `files-from-teacher/session-203-masking-mini-series/lecture-mask-8-information-flow-view.md`: Masking as Information Flow Control

## Out Of Current Exam Scope

Latest teacher update says these other `session-*` directories are not assessed in the final exam:

- `files-from-teacher/session-102-autoencoder-mini-series`
- `files-from-teacher/session-104-resnet-and-skip-connections-mini-series`
- `files-from-teacher/session-105-gan-and-adversarial-robustness-mini-series`
- `files-from-teacher/session-200-welcome-to-attention-transformer`
- `files-from-teacher/session-204-loss-function-mini-series`
- `files-from-teacher/session-205-transformer-advanced-topics`
- `files-from-teacher/session-208-rnn-seq2seq-mini-series`
- `files-from-teacher/session-211-tokenization-mini-series`
- `files-from-teacher/session-212-clustering-and-embedding-mini-series`
- `files-from-teacher/session-223-ffn-mini-series`
- `files-from-teacher/session-400`
- `files-from-teacher/session-402-audio-whisper-tts`
- `files-from-teacher/session-403-quantization-1`
- `files-from-teacher/session-404-quantization-2`
- `files-from-teacher/session-405-quantization-3`
- `files-from-teacher/session-406-ml-app`
- `files-from-teacher/session-407-l1-l2-revisited`
- `files-from-teacher/session-408-ga-logistic-regression`
- `files-from-teacher/session-501-linear-regression-logistic-regression-revisit`
