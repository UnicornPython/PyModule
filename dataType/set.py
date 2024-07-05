# python 中的集合


from os.path import isjunction


def declare():
    # 定义一个不可重复元素的集合
    s1 = {1, 2, 3, 4, 5}

    # 添加
    s1.add(10)

    #
    s1.discard(1)

    item = s1.pop()
    print(item)

    # 清空集合
    s1.clear()


def join():
    """判断集合"""
    s1 = {"HTML", "JS", "CSS"}
    s2 = {"KOTLIN", "GROOVY", "JAVA"}


def main():
    declare()


if __name__ == "__main__":
    main()
