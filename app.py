#!/usr/bin/env python

from classType import reflect

from structx import x
from structx import modulex


def main():
    reflect.reflect_use_case()

    print(x)
    print(modulex.x)


if __name__ == "__main__":
    main()
