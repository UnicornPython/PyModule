
"""
判断类与对象之间的关系

"""


class Base:
    pass


class Bar(Base):
    pass


class Foo(Bar):
    pass


def main():
    foo = Foo()
    # 不严格限定类型，只要是当前类或者当前类的父类，都可以满足 True
    print(isinstance(foo, Base))

    # 如果严格限定类型完全相同, 使用 type 来判断
    print(type(foo) is Base)
    print(type(foo) is Foo)


if __name__ == "__main__":
    main()
