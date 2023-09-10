#!/usr/bin/env python

"""
Python 中的 bool 类型(值为大写首字符，这与大部分的编程语言是不同的)
> False
> True

"""


def bool_case():

    print("False is None? => : ", False is None)

    # 需要注意的是在使用 if 等判断bool 逻辑的地方，会做一些隐式的 bool 逻辑
    # 转换, 其他类型可以转换为 bool 值进行比较, 典型就是 None
    if None:
        print("None to be False")
    elif not None:
        print("not None to be True")

    list = []
    if list:
        print("empty list is True")
    else:
        print("empty list is False")

    tuple = ()
    if tuple:
        print("empty tuple is True")
    else:
        print("empty tuple is False")

    dict = {}
    if dict:
        print("empty dict is True")
    else:
        print("empty dict is False")

    if 0:
        print("zero is True")
    else:
        print("zero is False")

    ...


def bool_type():
    # Python 中与其他很多编程语言一样，是有 boolean类型的
    # bool 类型总共两个值 False, True
    print(type(False))
    print(not True)
    print(type(None))


def main():
    bool_type()
    bool_case()


if __name__ == "__main__":
    main()
