
"""
callable()

> 函数，
> 类，
> 实现了__call__的类的实例

可以让 callable() 函数判断为 true

"""


class Foo:
    def __call__(self, *args, **kwargs):
        pass


class Bar:
    pass


def func():
    pass


def main():

    print(callable(func))
    print(callable(Foo))
    foo = Foo()
    print(callable(foo))
    bar = Bar()
    print(callable(bar))


if __name__ == "__main__":
    main()
