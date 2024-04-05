#!/usr/bin/env python

import re


def dict():
    exp = re.compile("[A-Za-z0-9_]+")
    val = exp.findall("hello 324234")
    print(val)


def main():
    dict()


if __name__ == "__main__":
    main()

