
"""
判断类之间的继承关系
"""


class Base:
    pass


class Bar(Base):
    pass


class Foo(Bar):
    pass


def main():
    # 只要是基于类的派生类，派生多级同样判断还是 true
    print(issubclass(Foo, Base))
    print(issubclass(Foo, Bar))


if __name__ == "__main__":
    main()

