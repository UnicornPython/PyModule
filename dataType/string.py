#!/usr/bin/env python

"""
python 中的字符串

"""

from datetime import datetime


def base():
    s = " hello"
    # * 表示对字符串进行重复
    print(s * 10)


def compare(): ...


def code():
    # 获取字符的字符码表中的值
    print(ord("a"))


def slice():
    s = "abcd1234567"
    # 切片取值使用[start:end] 的方式来获取
    print(s[2:5])

    # 可以进行局部的省略, 省略前部表示从头开始取
    print(s[:5])
    # 前后都省略表示取所有
    print(s[:])
    # 可以从逆向取值
    print(s[-7:-4])


def r_mode():
    # 带了转义字符
    a = "\time\tvalue"
    print(a)
    # r 模式的含义就是表示字符原始的含义，不转义
    a = r"\time\tvalue"
    print(a)


def f_template():
    # 1.空白字符对齐
    var: str = "hello"
    # 对齐 20 个字符, 右对齐
    print(f"{var:>20}")
    # 对齐 20 个字符，左对齐
    print(f"{var:<20}")
    # 中间对齐
    print(f"{var:^20}")
    # 指定对齐的字符
    print(f"{var:#>20}")

    # 2.数字
    num: int = 100000000
    # 数字显示(指定分割符号)
    print(f"{num:_}")
    print(f"{num:,}")

    # 3. 日期
    date: datetime = datetime.now()
    print(f"{date:%c}")


def main():
    slice()
    r_mode()
    f_template()


if __name__ == "__main__":
    main()
