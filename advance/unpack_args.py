#!/usr/bin/env python

"""
python 中存在的两个魔法参数, 这样的参数存在于函数定义中
    > *args : 表示传递了多个(不定长)的参数列表
    > **kwargs : 表示可以传递多个(不定长)的 key=value 参数对
"""

def order_pizza(size, *args, **kwargs):
    """this is a order pizza menu"""
    # recognize first args is the specify size
    print(f"order a {size} pizza")

    # use tuple revice the *args 
    # ("apple", "banana")
    for arg in args:
        print(f"- {arg}")
    
    # use dict receive **kwargs 
    for key, value in kwargs.items():
        print(f"- {key}={value}")


def main():
    order_pizza("large", "apple", "banana", appitile="pungent", taste="savory")



if __name__ == "__main__":
    main()
