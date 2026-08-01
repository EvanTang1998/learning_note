MarkDown Mermaid

Mermaid 是一种文本格式，它可以把文本转换为图表
用类似 Markdown 的文字描述，自动生成流程图、时序图、类图、甘特图等。

```Mermaid
sequenceDiagram
    用户->>服务器: 登录请求
    服务器->>数据库: 查询用户
    数据库-->>服务器: 返回结果
    服务器-->>用户: 登录成功
```


Mermaid 是谁开发的？

Mermaid 是一个开源 JavaScript 项目，最早目的是：

让开发者可以像写代码一样创建图表。

它现在支持：

流程图 Flowchart
时序图 Sequence Diagram
类图 Class Diagram
状态图 State Diagram
ER 图
甘特图
Git 图
用户旅程图

Mermaid 和 Markdown 的关系
Mermaid不是 Markdown 的一部分。Markdown 只负责文字格式。Mermaid 是扩展语法。
