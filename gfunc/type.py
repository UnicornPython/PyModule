#!/usr/bin/env python


def use_type():
    # type 主要用来判断变量的类型的
    print(type(10))
    print(type("hello"))
    print(type(10.0))
    print(type(("local", 10)))
    print(type(["hello", 10]))
    print(type({}))
    print(type({}) is type({}))


def main():
    use_type()


if __name__ == "__main__":
    main()
