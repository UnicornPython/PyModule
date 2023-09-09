
"""
python 中的 super 函数, 用于向上查找对应的父类的属性或者方法

"""


class Base:
    
    def f1(self):
        print("Base f1")


    def f2(self):
        print("Base f2")


class Bar:
    def f1(self):
        print("Bar f1")
        # 虽然当前类中没有 f2() 方法，但是这个 f2 方法取决于是什么样的对象来调用
        # 子类调用到这个 f1, 那么这个 super() 指代的就是子类的父级，
        # 当子类不仅仅只有当前类一个父级的时候，可能在其他父类找到 f2, 
        # 比如 foo 的另一个父类 Base 类,

        # 但是这样写的代码稳定性不好，假如当前调用类的所有父类都没有找到这个 f2
        # 就会报错了.
        super().f2()



class Foo(Bar, Base):
    """同时继承了 Base 和 Bar""" 
    def run(self):
        # Base 和 Bar 中都有 f1 方法应该执行哪一个
        super().f1()




def main():
    foo = Foo()
    foo.run()   # Bar f1
    # 按照 __mro__ 算法算出的属性来查找对应的方法，先找到哪一个就执行哪一个
    # 通常是 继承关系约靠前，查找关系就越靠前
    print(Foo.__mro__)



if __name__ == "__main__":
    main()



