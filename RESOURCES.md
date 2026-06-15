# Machine Learning Final Exam Review Resources

## Knowledge

- [Teacher README](files-from-teacher/Readme.md)
  Defines exam language, score weighting, closed-book rule, main session weight, extra session weight, and BagOfQuestions relevance. Use for: exam scope and priority.
- [Session 1 linear regression code](files-from-teacher/session-1/code-my_linear_regression.md)
  Shows the teacher's `MyOwnLinearRegression` implementation with `np.dot(X, self.weights)`, MSE gradients, and gradient descent updates. Use for: code blanks and linear regression implementation details.
- [Session 1 multiple linear regression lecture](files-from-teacher/session-1/lecture-3-multiple-linear-regression.md)
  Explains matrix form, row-vector convention, `X`, `W`, `Y`, and batch prediction `Y_hat = XW + 1b`. Use for: matrix shapes and why `np.dot` is used.
- [BagOfQuestions Session 1 AE](files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-ae.md)
  Teacher question for filling in linear regression from scratch. Use for: expected exam-style blanks and short answers.
- [BagOfQuestions Session 1 AF](files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-af.md)
  Teacher debug question contrasting incorrect `X * self.weights` with correct `np.dot(X, self.weights)`. Use for: common mistakes and shape reasoning.
- [BagOfQuestions Session 1 AK](files-from-teacher/BagOfQuestions/BagOfQuestions-session-1-ak.md)
  Teacher question focused on `fit` method details, gradients, shapes, and why gradient descent subtracts the gradient. Use for: exam-ready implementation details.

## Wisdom (Communities)

- Course-approved question channels from `files-from-teacher/Readme.md`
  The teacher recommends professional public question channels before private chats. Use for: unresolved course-scope questions that require teacher/community confirmation.
