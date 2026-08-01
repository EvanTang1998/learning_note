# Markdown Mermaid

Mermaid 是一种文本格式，它可以将文本转换为图表。它使用类似 Markdown 的文字描述方式，自动生成流程图、时序图、类图、甘特图等图表。

Mermaid 和 Markdown 的关系：
Mermaid 不是 Markdown 的一部分。Markdown 主要负责文字格式，而 Mermaid 是 Markdown 的扩展语法，用于生成图表。

如何使用：
在 Markdown 文档中嵌入 Mermaid，需要使用 ` ```mermaid ` 开头，` ``` ` 结尾，中间放入 Mermaid 语句。
例如：

```mermaid
sequenceDiagram
    用户->>服务器: 登录请求
    服务器->>数据库: 查询用户
    数据库-->>服务器: 返回结果
    服务器-->>用户: 登录成功
```

```mermaid
sequenceDiagram
    autonumber
    title 规则配置管理（新增/删除）流程
    actor User as 用户
    participant Console as 管理平台
    participant Service as 业务服务
    participant DB as 数据库
    participant External as 外部同步服务

    User->>Console: 1.提交新增/删除申请
    Console->>Service: 2.查询当前数据
    Service->>DB: 查询数据库
    DB-->>Service: 返回查询结果
    Service-->>Console: 返回查询结果

    Note over Console: 新增：校验数据不存在<br/>删除：校验数据存在

    Console->>Console: 创建审批流程
    Console-->>User: 返回审批流程创建结果

    User->>Console: 3.提交审批流程

    Console->>Service: 4.执行数据处理
    Service->>DB: 新增/删除业务数据

    alt 需要同步外部系统
        Service->>External: 同步数据状态
        External-->>Service: 返回同步结果
    end

    Service-->>Console: 返回处理结果
    Console-->>User: 返回操作结果
```

Mermaid 是谁开发的？
Mermaid 是一个开源 JavaScript 项目，最初目的是：
> 让开发者可以像写代码一样创建图表。
它现在支持：
- 流程图（Flowchart）
- 时序图（Sequence Diagram）
- 类图（Class Diagram）
- 状态图（State Diagram）
- ER 图
- 甘特图
- Git 图
- 用户旅程图

