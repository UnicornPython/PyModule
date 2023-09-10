#!/usr/bin/env python


def add(x, y):
    return x + y


# lambda 表达式就是一个匿名函数，无法显示调用
# 表达式就是 lambda args: express
lambda x, y: x + y 


# 如果想要显示调用可以赋值给变量，这就与普通函数没有什么差异了
addfunc = lambda x, y: x + y


def lambda_test():
    print(add(4, 5))
    print(addfunc(3, 7))
    # 当然我们可以直接调用
    print((lambda x, y: x + y)(10, 5))


def func_map(fmap, iter):
    """
    lambda 表达式最常见的用法还是作为其他函数的参数，实现一些高阶函数
    
    """
    result = []
    for item in iter:
        new = fmap(item)
        result.append(new)
    return result


def test_map():
    nums = [2, 3, 4, 6]
    result = func_map(lambda x: x**3, nums)
    print(result)


def main():
    lambda_test()
    test_map()


if __name__ == "__main__":
    main()
