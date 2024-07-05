#!/usr/bin/env python


def list():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = ["java", "goland", "javascript", "kotlin"]
    print(list1 + list2)

    # 从末尾追加
    list2.append("rust")

    # 指定位置添加
    list2.insert(3, "lua")

    # 删除元素
    list2.remove("java")

    # 从列表中末尾弹出元素, 弹出元素后直接从list 删除了
    item = list2.pop()
    print(item)
    print(list2)

    # 清空列表的所有元素
    list1.clear()
    print(list1)

    #  查看元素索引位置
    print(list2.index("javascript", 1))

    # 统计元素的个数
    print(list2.count("javascript"))

    # 对元素进行排序
    list2.sort()
    print(list2)
    # 倒序
    list2.reverse()
    print(list2)


def main():
    list()


if __name__ == "__main__":
    main()
