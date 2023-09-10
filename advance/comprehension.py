#!/usr/bin/env python

"""
Python 中的列表推导式(可以用于元组与字典)
------------------------------------------------------------------
 [表达式 if 表达式条件 else 分支 for i in 序列 if 推到条件]

 > 1. 列表中元素的转换，过滤，
 > 2. 间接将字典转换为列表进行处理
 > 3. 不要使用数据量很庞大的元组进行推导，应该使用生成器

"""

num = [2, 19, 20, 79, 10, 20, 34, 2]

dic = {
    "name": "alex", "gender": "false", "hobby": ["vallyball", "handwritter"]
}


def mapping_data():
    remaider = [x % 2 for x in num]
    print(remaider)

    power = [i*i for i in range(1, 100)]
    print(power)


def get_match_data():
    even = [x for x in num if x % 2 == 0]
    print(even)


def handler():
    # 推导字典类型
    yeal = {
        item[0]: item[1]
        for item in dic.items()
        if item[0] == "name" or item[1] == "false"
    }
    print(yeal)


def dic_sort():
    scores = {
        "linlong": 10, "windows": 85, "Linux": 120, "MacOs": 90, "chromeOs": 50
    }
    sored_scores = {
        item[0]: item[1]
        for item in sorted(scores.items(), key=lambda e: e[1], reverse=True)
    }
    print(sored_scores)


def set_earese_duplicate():
    names = [
        '麦叔', '张三', ' 麦叔 ', 'FGA ', '张小三',  'FGA', '石石', ' 莫名', '莫名'
    ]
    true_name = {n.strip() for n in names}
    print(true_name)
    ...


def main():
    get_match_data()
    mapping_data()
    handler()
    dic_sort()
    set_earese_duplicate()


if __name__ == "__main__":
    main()
