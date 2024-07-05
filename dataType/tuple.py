#!/usr/bin/env python


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


def main():
    turple()


if __name__ == "__main__":
    main()
