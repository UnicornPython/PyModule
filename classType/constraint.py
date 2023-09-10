#!/usr/bin/env python
"""
Python 中没有接口的概念, 怎样使用类之间的继承关系，
在企业级开发的时候实现对子类的约束 (必须要实现某些方法)
-----------------------------------------------------------------
 1. 在父类中定义的方法的实现是一个抛出异常的实现，当程序在子类中
    找不到复写的方法的时候，就会找到父类，直接抛出异常告诉你需要
    实现这个方法才行
 2. 子类复写了这个方法，不会找到父类中，代码正常运行。

"""


class Message:

    def execute(self, message):
        raise Exception("这是必须要实现的发送消息的方法: ", f"execute({message})")


class DingDing(Message):

    def execute(self, message):
        print(message)
        pass


class WeChat(Message):
    pass


def main():
    d = DingDing()
    d.execute("hello")

    w = WeChat()
    w.execute("world")


if __name__ == "__main__":
    main()
