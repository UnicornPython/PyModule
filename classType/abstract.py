#!/usr/bin/env python
"""
Python 中没有接口的概念, 怎样使用类之间的继承关系，
在企业级开发的时候实现对子类的约束 (必须要实现某些方法)
-----------------------------------------------------------------
 1. 在父类中定义的方法的实现是一个抛出异常的实现，当程序在子类中
    找不到复写的方法的时候，就会找到父类，直接抛出异常告诉你需要
    实现这个方法才行
 2. 子类复写了这个方法，不会找到父类中，代码正常运行。

----------------------------------------------------------------
 现代 python 中可以使用抽象类来实现类似接口的公共

 from abc import ABC, abstractmethod
 class Message(metaclass=ABC):
    @abstractmethod
    def execute(self, message: str) -> None:
        raise Exception("这是必须要实现的发送消息的方法: ", f"execute({message})")
 

"""

from typing import override

from abc import ABC, abstractmethod

class Message:
    def execute(self, message: str) -> None:
        raise Exception("这是必须要实现的发送消息的方法: ", f"execute({message})")


class DingDing(Message):
    @override
    def execute(self, message: str) -> None:
        print(message)
        pass


class WeChat(Message):
    pass

def main():
    d = DingDing()
    d.execute("hello")

    w = WeChat()
    w.execute("world")


# 使用抽象类来限定子类必须要实现的方法
class Mock(ABC):
    # 标记抽象方法
    @abstractmethod
    def data() -> dict[str, str]:
        pass

# 继承抽象类，则必须覆写抽象方法
class DataMock(Mock):
    @override
    def data() -> dict[str, str]:
        return {"a": "b"}




if __name__ == "__main__":
    main()
