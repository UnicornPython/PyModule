#!python

"""
max / min 函数的使用

"""


def main():
    names: list[str] = [ "aliex", "Timothy", "Bob", "James", "Luigi","Amanda", "Zebra"]

    # 使用 max / min 获取一个list 中的最大最小的时候，
    # 当比较的是数字的时候，则获取到的是最大最小数
    # 当使用的是字符串的时候，则获取到的是 ascii 码值的大小比较
    # ----------------------------
    # > max 还可以传入比较的函数
    print(max(names));


    for name in names:
        print(name, name.lower().count('a'), sep=": ")


    print("Name contains most a char", max(names, key=lambda x: x.lower().count('a')))
    print("Longest name is: ", max(names, key=len))


if __name__ == "__main__":
    main()
