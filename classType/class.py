class Pilot:
    # 实例构造方法
    def __init__(self, name="Pilot", usage="property"):
         self.name = name
         self.usage = usage
         self.id = 1131324

    def greet(self):
        print(f"Hello {self.name}")


    # 实例方法, 没构建一个实例都会存在这样的方法，每个实例中的方法签名相同
    # 运行时不同, 这些实例方法的第一个参数就是这个实例本身
    def present_id(self):
        print(f"My present_id is {self.id}")


    def set_ship(self, ship):
        self.ship = ship


    # 类方法, 类似于 java 里面的 static 方法，属于类的方法，第一个参数就是类实例
    @classmethod
    def check_value(cls):
        print(cls)


    # 静态方法，类似于函数, 使用类名调用
    @staticmethod
    def static_method():
        print("hello")


def main():
    # 构建类的实例, 
    # 可以使用如下的几个方法来判断类的实例中的属性
    # hasattr : 是否具有某个属性, 
    # getattr : 获取指定属性的值, 对应的是类中的 __getattribute__() 魔术方法
    # setattr : 为对象添加某个属性的值, 对应的是类中的 __setattr__() 魔术方法
    pilot = Pilot();
    if hasattr(pilot, "ship"):
        print(getattr(pilot, "ship"))
    else:
        setattr(pilot, "ship", "show")
        print(getattr(pilot, "ship"))

    print(pilot.__getattribute__("ship"))


if __name__ == "__main__":
    main()

