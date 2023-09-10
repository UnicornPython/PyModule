#!/usr/bin/env python

"""
Python 的类中有一系列的魔术方法
---------------------------------------------------------
__init__() : 对象实例化的时候会被调用(对象的初始化)
__new__()  : 创建对象之前，为类实例分配内存空间的时候会调用
__del__()  : 对象销毁的时候会自动调用
__str__()  : 决定怎样用字符串的形式来展示一个类
__repr__() : 调用 repr 函数的时候怎样显示一个类

# 这个方法会产生一个新的对象
################################################################
__add__()  : 对应算数运算(+)决定了两个对象之间相加的行为
__sub__()  : 对应算数运算(-)决定了两个对象之间的相减行为
__multiplication__()  : 对应算数运(*)决定了两个对象之间的相乘行为
__truediv__()  : 对应算数运算(/)决定了两个对象之间的相除行为
__floordiv__()  : 对应算数运算(//)决定了两个对象之间的取余行为

# 这个方法会改变当前调用方法对象，
################################################################
__iadd__()  : 对应算数运算(+=)决定了两个对象之间相加的行为
__isub__()  : 对应算数运算(-=)决定了两个对象之间的相减行为
__imultiplication__()  : 对应算数运(*=)决定了两个对象之间的相乘行为
__itruediv__()  : 对应算数运算(/=)决定了两个对象之间的相除行为
__ifloordiv__()  : 对应算数运算(//=)决定了两个对象之间的取余行为

# 对象比较方法
################################################################
__lt__() : 对应算数运行中 (<), 决定两个对象怎么比较大小
__tt__() : 对应算数运行中 (>), 决定两个对象怎么比较大小
__le__() : 对应算数运行中 (<=), 决定两个对象怎么比较大小
__ge__() : 对应算数运行中 (>=), 决定两个对象怎么比较大小
__eq__() : 对应算数运行中 (=), 决定两个对象怎么比较大小
__ne__() : 对应算数运算中 (!=), 决定两个对象怎么比较大小


# 想要像操作数组一样操作对象需要实现的方法
################################################################
__setItem__() : 支持以对象名的 student["name"] = 'alex' 这样的操作
__getItem__() : 支持以对象名取值的 student['name']
__delItem__() : 支持 del student['name']


# 想要实现上下文功能
################################################################
用于实现上下文功能，例如 with 语法,
__enter__() : 用于实现上下文管理的功能, 进入上下文时调用
__exit__()  : 用于实现上下文管理的功能，离开上下文时调用


# 将对象升级为可执行
################################################################
__call__() : 使得一个类创建的对象具有可执行性, 函数参数设计
             既可以是一个函数，同时也可以是一个实现了这个方法
             的对象(鸭子类型)


# 将对象转化为字典样式
################################################################
__dict__ : 实现这个方法就可以返回一个字典, 注意，这不是方法


"""

from io import TextIOWrapper


class Config:

    instance = None

    def __new__(cls, *args, **kwargs): 
        if Config.instance is None:
            cls.instance = super(Config, cls).__new__(cls)
        else:
            print("singleton instance already exists")
        return cls.instance

    def __init__(self, log_path, verbose, other_settings):
        self.log_path = log_path
        self.verbose = verbose
        self.other_settings = other_settings

    def __del__(self):
        Config.instance = None
        print("del was used")

    def __str__(self):
        return f"|{self.log_path}|{self.verbose}|"

    def __repr__(self) -> str:
        return f'Config({self.log_path}, {self.verbose}, {self.other_settings})'


class Matrix:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, m2):
        temp = Matrix(0, 0, 0, 0)
        temp.a = self.a + m2.a
        temp.b = self.b + m2.b
        temp.c = self.c + m2.c
        temp.d = self.d + m2.d
        return temp

    def __iadd__(self, m2):
        temp = Matrix(0, 0, 0, 0)
        temp.a = self.a + m2.a
        temp.b = self.b + m2.b
        temp.c = self.c + m2.c
        temp.d = self.d + m2.d
        return temp

    def __str__(self):
        return f'|{self.a}  {self.b} |\n|{self.c} {self.d}|'


class File:

    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.encoding = "utf-8"
        self.fd = None

    def __enter__(self): 
        self.fd = open(self.file_path, mode = self.mode, encoding=self.encoding)
        print("打开文件")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        if type(self.fd) is TextIOWrapper:
            self.fd.close()

    def send(self, message):
        if type(self.fd) is TextIOWrapper:
            self.fd.write(message)

    def read(self):
        if type(self.fd) is TextIOWrapper:
            self.fd.write("读消息\n")


def test_del():
    a = Config("./logs/", True, {"more_settings": "yes"})
    b = a
    print("Delete a")
    del a 
    print(b)


def test_singleton():
    a = Config("./logs/", True, {"more_settings": "yes"})
    print("a -------------- object")
    print(a.log_path)
    print(a.verbose)
    print(a.other_settings)
    b = Config("./data/", False, {"more_settings": "no"})
    print("b -------------- object")
    print(b.log_path)
    print(b.verbose)
    print(b.other_settings)


def test_str_repr():
    b = Config("./data/", False, {"more_settings": "no"})
    print(b)
    print(repr(b))


def test_dict():
    config = Config("./data", "peek", "full")
    print(config.__dict__)


def test_add():
    a = Matrix(1, 3, 5, 7)
    b = Matrix(2, 4, 6, 8) 
    c = a + b
    print(c)
    print(a)

    a += b
    print(a)


def test_with():
    # File 类中实现了 __enter__, 返回的值会赋值给 f
    # with 上下文退出的时候自动执行__exit__()
    with File("./files/console.log", "a") as f:
        f.send("hello")


def main():
    # test_del()
    # test_singleton()
    # test_str_repr()
    # test_add()
    # test_dict()
    test_with()


if __name__ == "__main__":
    main()
