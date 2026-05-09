# 机器学习课程仓库

## 工程结构

- lundechen-machine_learning_2026_spring/ 课程仓库，最高可信源
   - `./session-*`：每次课程的资料目录，例如 `./session-1/`
- wechat-session/ 课程群聊记录（MM-DD 目录）
- tasks/ 作业回答
- tasks-list.md 待完成作业

## 开发规范

1. 不确定的问题一定要向用户提问
2. 维护任务列表
   1. 从 wechat-session 或 lundechen-machine_learning_2026_spring 解析任务到 tasks-list.md ，相应的，如果需要查看后者中任务的详情可以去前者，**不需要提交到微信群的任务自动标记为已完成**
   2. 完成任务后只标 `[x]`，不删除
      ```
      ## 05-09 课程任务
      - [ ] 需要提交到微信群且未完成的任务
      - [x] 不需要提交到微信群的任务
      - [x] 需要提交到微信群且完成的任务
      ```