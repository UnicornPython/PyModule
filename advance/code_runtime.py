import inspect
import re


def getnumber(n: int):
    for i in range(n):
        # 函数在执行过程中，会又栈帧信息，
        # 生成器中的栈帧对象比较特别，在函数对象中保留了一份栈帧对象的引用
        # 这个引用记录了函数的执行状态，每次yield 后栈帧对象记录状态，
        # 下次 next() 执行的时候，从栈帧中取出信息，然后继续执行
        print(inspect.currentframe())
        yield i


def test_code():
    print(type(getnumber))
    # 函数对象中通过__code__对象来存储代码相关的信息
    # 这些信息的属性都以 co_ 开头
    print(getnumber.__code__)
    list(getnumber(10))
    #  for i in getnumber(10):
    #      print(i)


def handle_log():
    repx = re.compile(r'{"rspCode".*}}')
    with open("result.log", "a") as out:
        with open("response.log", 'r', encoding="utf-8") as f:
            for line in f:
                x = repx.search(line)
                if x is not None:
                    out.write(x.group())
                    out.write("\n")


def main():
    # test_code()
    handle_log()


if __name__ == "__main__":
    main()
