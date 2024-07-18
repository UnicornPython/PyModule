#!/usr/bin/env python

import re

"""
Python 中字典类型，相当于其他语言中的 hashmap / hashTable


"""



def mergeDict():
    a = { "A": 1, "B": 2}
    b = { "B": 3, "S": 10}

    # 将 b 合并到 a, 当 a 中存在与 b 中 key 相同的时候，b 会覆盖 a 中的内容
    print(a|b)

    # 与上面的内容是同样的含义
    a |= b
    print(f"{a}")


def dict():
    exp = re.compile("[A-Za-z0-9_]+")
    val = exp.findall("hello 324234")
    print(val)


def main():
    dict()
    mergeDict()


if __name__ == "__main__":
    main()

