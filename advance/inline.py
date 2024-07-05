#!/bin/python3

# 行内表达式
# 1.
# 2. True if expr else False


from random import randint


def first():
    phrase: str = "Hello Bob"
    print("".join(reversed(phrase)))
    print(phrase[::-1])


def second():
    a = randint(0, 10)
    # if a > 5:
    #     return "yes"
    # else:
    #     return "no"
    return "yes" if a > 5 else "no"


def three(): ...


def main():
    first()
    print(second())


if __name__ == "__main__":
    main()
