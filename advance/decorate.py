#!/usr/bin/env python


"""
Python 中的装饰器
"""


def log(func):
    # 内部定义一个函数，然后返回这个函数，调用外部函数的时候得到一个函数，
    # 再次调用就是执行内部函数，这时候就可以在这个函数的前置或者后置执行
    # 一些操作，比如记录日志，计算内部函数运行耗时等
    def decoration(*args, **kwargs):
        print(f"call function with: {args}  and {kwargs}")
        result = func(*args, **kwargs)
        print(f"call function result: {result}")
        return result

    return decoration


"""
装饰器模式的使用方法

> 使用 @log 的方式将装饰器函数标注在需要使用装饰器的函数上，即可实现装饰器对函数的增强

""" 

@log
def do(name, value, time) -> str:
    print(f"{name} {value}, cost {time} minnues")
    return "ok"


def main():
    do("alex", "feed cat", time=20)


if __name__ == "__main__":
    main()
