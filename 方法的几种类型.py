"""
该文档讲解 关于 "方法" 容易搞混的概念

包括： 构造方法 成员/实例方法 类方法 静态方法  函数

方法: Method  方法属于某个对象或类的函数
函数: Function 函数则是独立的代码块，用来执行特定的任务，不依赖于对象或类。

类就是模版，实例相当于实际的产品。
构造方法 就是用来 初始化的。
成员方法 也叫实例方法，修改某个类属性，不会影响其他实例。
而类方法 修改某个类属性，会影响所有实例，相当于模版变了。通过 @classmethod 装饰器定义。
静态方法 相当于写在类中的函数。通过 @staticmethod 装饰器定义。

特殊方法（魔法方法）：这些是具有特殊用途的内建方法，例如 __init__()、__str__()、__repr__()、__del__() 等。
这些方法在类中用于处理特定操作（如初始化、打印、删除等），在语言层面自动触发。
"""

class CAR:
    name = "xiaomi su7"
    max_speed = 80

    def __init__(self, color: str):  # 构造方法，就是用来初始化的方法，仅用于初始化，传入参数
        self.color = color

    def __str__(self):  # 内置的一种方法，定义对象的字符串表示
        return f'{self.color} {self.name}'

    def run(self, speed: int):  # 成员方法/实例方法， 传入self表示可以使用实例属性和类属性
        print('The', self.color, self.name, 'is running on', speed, 'km/h', 'max speed is', self.max_speed, end=' ')
        if speed > self.max_speed:
            print('超速了！')
        else:
            print('没超速')

    @classmethod
    def reset_speed(cls, road):  # 类方法，第一个参数是cls，表示类本身，它可以修改类属性
        if road == '高速路':
            cls.max_speed = 140
        else:
            cls.max_speed = 60

    @staticmethod
    def plus_speed(a, b):  # 静态方法，它无需跟类相关的参数，它只跟函数本身相关
        return a + b

zhangsan_car = CAR('black')
wangge_car = CAR('white')
zhangsan_car.run(100)
wangge_car.run(200)

CAR.max_speed = 120    # 可以直接修改类属性
CAR.reset_speed('高速路')   # 如果情况复杂，则可以通过类方法修改类属性

print(zhangsan_car.max_speed)
print(wangge_car.max_speed)

bmw = CAR.plus_speed(60, 20)
print(bmw)
