#!/usr/bin/env python


from collections import namedtuple
from typing import NamedTuple


def turple():
    """元组"""

    # 是不可变的数据类型, 不可修改，新增，删除
    t1 = (1, 2, 4)
    print(len(t1))

    t2 = ("java", "javascript")

    list2 = ["hello", "world"]

    # 可以进行相加
    print(t1 + t2)

    # 不同类型之间是不可相加的
    # print(t1 + list2)

    # 只有二元组，三元组，没有一元组，一元组直接退化为具体的数据，即使被括号包裹
    t3 = "yes"
    print(type(t3))

    # 可以使用`,` 来使得一个元素变成一个元组
    t4 = ("no",)
    print(type(t4))



##########################################################
# 命名元组
##########################################################
# > 具备了元组的不可变性和字典的可读性
# 
# collections 中提供了 namedtuple, 但是这种使用方式会丢失类型信息
# typing 中提供了 namedTuple, 可以保留类型信息

class Point(NamedTuple):
    x: float
    y: float


def nameturple():
    """命名元组"""


    # 1.collections 中的命令元组使用方式
    Point = namedtuple("Point", ['x', 'y'])
    px = Point(1, 2)
    print(px.x)
    print(px[1])


    # 2. typing 中的命名元组可以保留类型信息
    p = Point(1.2, 2.0)
    # 支持多种方式的访问
    print(p.x)
    print(p[0])





def main():
    turple()
    nameturple()


if __name__ == "__main__":
    main()
