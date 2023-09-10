#!/usr/bin/env python


"""
Python 中的装饰器
"""


def log():
    # 内部定义一个函数，然后返回这个函数，调用外部函数的时候得到一个函数，
    # 再次调用就是执行内部函数，这时候就可以在这个函数的前置或者后置执行
    # 一些操作，比如记录日志，计算内部函数运行耗时等
    def hello():
        ...

    return hello


def decoration():
    ...


def main():
    ...


if __name__ == "__main__":
    main()      
