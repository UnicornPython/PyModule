#!/usr/bin/env python

"""
Python 中的生成器, 生成器从迭代器中产生

>  __iter__

"""

def py2_range(n): 

    # range 应该返回一个 iterable 对象
    # for i in range(10):
    for i in range2(n):
        print(i)


# python 2 中的 range 确实返回了一个 list 作为结果
# 这样的设计在一些大的序列中会占用很多的计算资源和内存空间
# 实际的过程中只需要当前序列产生的那个数据而已
def range2(n) -> list:
    i = 0
    result = []
    while i < n:
        result.append(i)
        i += 1
    return result


# 需要一个可迭代对象
class Py3Range:
    def __init__(self, n) -> None:
        self.n = n

    def __iter__(self):
        return RangeIter(self.n)

class RangeIter:
    def __init__(self, n) -> None:
        self.n = n
        self.current = 0
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration()
        result = self.current
        self.current += 1
        return result

def py3_range(n):
    # range 应该返回一个 iterable 对象
    for i in Py3Range(n):
        print(i)


# 上述的 py3 实现的代码可以使用 yield 简化为如下的形式
# 代码中存在 yield 的时候得到的是一个生成器
# 
def ranger(n):
    i = 0
    while i < n:
        yield i
        i += 1

def generator():
    # ranger 就是一种使用 yield 实现的特殊的可迭代对象
    # 初次调用并不会执行, 得到的生成器就是一个可迭代对象, 
    # 内部调用 __iter__(), 返回迭代器
    it = ranger(4)

    # 调用 __next__() 可以将 yield 参数作为__next__的返回值
    print(it.__next__())

    # 在 for 循环中被当做可迭代对象使用
    for i in ranger(4):
        print(i)
        

"""
可迭代对象
> 
"""

class MyList:

    def __init__(self, list) -> None:
        self.list = list

    # 实现 __getitem__ 方法, 就将一个对象转换为 iterable 对象
    def __getitem__(self, index):

        # IndexError 就是 for 循环用来判断迭代结束的
        if index >= len(self.list):
            raise IndexError()
            
        return self.list[index]


def iterable()-> None: 
    # list 就是一个可迭代对象
    # list = [1, 2, 3]
    
    list = MyList([1,2,3])
    for i in list:
        print(i)

"""
迭代器
> 
"""

# 为对象实现可迭代能力的第二种方式就是为其实现一个迭代器, 
# 迭代器需要实现 __next__ 方法获取迭代器中的元素
# 可迭代对象需要 __iter__ 返回它自己的迭代器

class SelfList:

    def __init__(self, list) -> None:
        self.list = list

    def __iter__(self):
        return MySelfIterator(self)

class MySelfIterator:

    def __init__(self, self_list: SelfList) -> None:
        self.self_list = self_list
        self.index = 0


    def __next__(self):
        if self.index >= len(self.self_list.list):
            raise StopIteration()
        result = self.self_list.list[self.index]
        self.index += 1
        return result

    # 迭代器成为一个 iterable 对象只要返回自身即可
    def __iter__(self): 
        return self

def iterator() -> None:

    list = SelfList([1,2,3, 4, 5])
    for i in list:
        print(i)
    # it = list.__iter__()
    # iter() 函数比 __iter__() 更加通用，可以获取 __iter__ 和 __getitem__ 两种方式的可迭代对象的迭代器
    # 这里得到的 iterator 本身不是 iterable 的, 不能被 for 使用（for 只识别 iterable, 而不是 iterator)
    # 通常我们也要为 iterator 实现 __iter__ 变成一个 iterable 对象
    it = iter(list)
    for i in it:
        print(i)

def main():
    print("-------------- iterable ------------")
    iterable()
    print("-------------- iterator ------------")
    iterator()
    print("-------------- py2 ------------")
    py2_range(3)
    print("-------------- py3 ------------")
    py3_range(10)
    print("-------------- generator------------")
    generator()

if __name__ == "__main__":
    main()
