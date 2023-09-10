#!/usr/bin/env python

"""
zip 函数的用法
--------------------------------------------------------
> 对多个列表按照索引组合为一个个的元组
> 当两个列表长度不同的时候按照索引小的进行输出
"""


def use_zip():

    a = [1, 2, 3, 4, 5, 6]
    b = [6, 5, 4, 3, 2, 1]

    for item in zip(a, b):
        print(item)


def main():
    use_zip()


if __name__ == "__main__":
    main()
