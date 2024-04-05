#!/usr/bin/env python

"""
python 中的字符串

"""


from datetime import datetime


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
    f_template()


if __name__ == "__main__":
    main()
