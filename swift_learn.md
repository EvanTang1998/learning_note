

在SwiftUI中，使用点（`.`）语法来调用方法或访问属性是一种常见的编程习惯，这种写法在SwiftUI的声明式UI框架中非常普遍。

```swift
Text("Hello, world!")
    .font(.largeTitle)
```

这里使用了SwiftUI的修饰符（Modifier）模式。让我们分解一下这段代码来理解其逻辑和写法：
1. `Text("Hello, world!")` 创建了一个文本视图（View），显示内容为"Hello, world!"。
2. `.font(.largeTitle)` 是一个修饰符（Modifier），它作用于前面的`Text`视图。这个修饰符的作用是设置文本的字体为大标题（`largeTitle`）样式。
在SwiftUI中，`.` 表示我们要访问一个类型（如`Font`）的静态属性（如`.largeTitle`）或者调用类型的静态方法。在这个例子中，`.font(.largeTitle)`实际上是调用了`font`方法并传入了`Font.largeTitle`作为参数。SwiftUI的`font`方法期望接收一个`Font`类型的参数来指定文本的字体样式，而`.largeTitle`是`Font`类型的一个静态属性，表示一种特定的字体样式。

之所以在`font`和`largeTitle`前面加`.`，是因为这是Swift语言中访问类型成员（例如静态属性或静态方法）的语法。在SwiftUI中，这种点语法和修饰符模式的使用，使得UI代码非常简洁和易读，允许开发者通过链式调用的方式，方便地组合和配置UI组件的属性。

## swift 传递参数使用冒号 : python 使用的是等于号 =

## _表示可以省略这个参数
swift 和 python 不同的是 swift 默认传参需要指明参数名称，
若想实现类似python的通过位置传输，则可以在参数前面加 _  此时不再需要参数名
如：
Text("Hello World!")
    .underline(_ isactive: bool=True, color: Color?=nil)
    故 underline 的第一个参数可以直接写true 或false 
    .underline(true, color: .red)
