


class CAR:
    name = "xiaomi su7"
    max_speed = 80
    battery = 80

    def __init__(self, color: str):  # 特殊方法，仅用于初始化，传入参数
        self.color = color

    def __str__(self):  # 定义对象的字符串表示
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

CAR.reset_speed('高速路')
print(zhangsan_car.max_speed)
print(wangge_car.max_speed)
p = CAR.plus_speed(1, 2)
print(p)
print(type(zhangsan_car))
