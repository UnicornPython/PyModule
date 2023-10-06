
from random import random
from itertools import count


# 1 import
def test_import():
    from numbers import Number as nb1
    nb2 = __import__("numbers").Number

    print(nb1 == nb2)


# 2. while
def test_while():

    while True:
        r = random()  # [0, 1]
        if r < 0.8:
            print(r)
        else:
            break

    # for 操作
    for _ in count():
        r = random()
        if r < 0.8:
            print(r)
        else:
            break


# 3.pass 可与 ... 表示空的代码块
def test_pass():
    def dot():
        ...

    dot()
    pass


# 4. if ... else 与 match case 等价
def test_branch(word):
    if word == "branch":
        print("ok")
    elif word == "match":
        print("ok")
    else:
        print("not ok")
    # ----------------------

    match word:
        case "branch":
            print("ok")
        case "match":
            print("ok")
        case _:
            print("not ok")


# 5. class
class Cls:
    def printf(self):
        print(self)


def test_class():
    c = Cls()
    c.printf()
    # 测试用 type 模拟的类的效果
    test_type()


def test_type():
    def printf(self):
        print(self)

    # 使用 type 的实例化来模拟一个类的初始化
    # 第一个参数是 类名
    # 第二个参数是 父类
    # 第三个参数是 参数集合
    Cla = type("Cla", (), {"printf": printf})
    c = Cla()
    print(c)


# 6. with
def test_with():
    with open("./regex.py") as f:
        data = f.read()
    print(data)


# 7.列表推导式, 同样适用于集合与字典
def list_express():
    a = [1, 2, 3, 5, 6]
    b = [e+233 for e in a]
    print(b)


def main():
    test_import()
    test_while()
    test_branch("ok")
    test_class()
    test_with()
    list_express()


if __name__ == "__main__":
    main()
