#!/python

"""
Python 中实现单例 

> 单例模式是一种常见的设计模式，它保证一个类在程序的生命周期内只会初始化一次，
  并提供了全局唯一访问点来获取这个唯一的实例。
"""


"""
1. 使用模块实现单例 (借助模块在程序中的唯一性)

class Singleton(object):
    def foo(self):
        pass

singleton = Singleton()
-----------------------------------------------
其他的模块直接通过导入模块的方式获取这个类的实例

from xxxx import singleton

a = singleton
b = singleton 
print(id(a))
print(id(b))

"""

"""
2. 通过装饰器实现
   通过在装饰器中维护一个字段。判断字典是否有键值对，如果有，则不添加，最后返回字典中的类的实例
   可以保证每次返回的都是同一个实例，要使用这个单例装饰器，只要将其装饰到需要实现单例的类上即可

"""

def singleton_func(cls):
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton


@singleton_func
class Phone(object):
    def phone_id(self):
        return id(self)

def test_decoration_singleton():
    p1 = Phone()
    p2 = Phone()
    print(id(p1)==id(p2))


"""
3. 使用实例化的方式实现单例 (通过 __call__() 方法实现单例)
   先重写 __call__ 方法，在 __call__ 方法中返回自己，先实例化一个类的对象，后面所有
   需要使用这个类的地方，都调用这个实例对象，这样每次调用都是同一个实例，所以也能实现单例。
"""

class SingletonInstance():

    def __call__(self, *args, **kwargs):
        return self

def test_call_singleton():
    singletonInstance = SingletonInstance()
    s1 = singletonInstance()
    s2 = singletonInstance()
    print(id(s1) == id(s2))


"""
4. 使用类装饰器实现单例
   _var : 命名约定，仅供内部使用，通常不会由 Python 解释器强制执行(私有变量)
   var_ : 按约定使用，避免与 Python 关键字冲突
   __var : 在类上下文中使用时，触发 "名称修饰", 由 Python 解释器强制执行
   __var__ : 表示 Python 语言定义的特殊方法，避免在你自己的属性中使用这种命名方案

""

class SingletonDecorator(object):
    _instance = None
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@SingletonDecorator
class TelePhone(object):
    def phone(self):
        return id(self)

def test_singleton_call_with_decorator():
    p1 = TelePhone()
    p2 = TelePhone()
    print(p1.phone() == p2.phone())


"""
5.
"""



def main():
    test_decoration_singleton()
    test_call_singleton()
    test_singleton_call_with_decorator()


if __name__ == "__main__":
    main()
