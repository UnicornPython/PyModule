#!/usr/bin/python3

import re


def repl_str():
    pattern = re.compile(r'^hel.*')
    flag = pattern.match("""hollo world""")
    if not flag:
        print("not find same string")
        return
    print(flag.group())


def spl_str():
    poem = "床前明月光，疑是地上霜。举头望明月，低头思故乡."
    sentence_list = re.split(r'[,.，。]', poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


def alias():
    peorm = "like"
    print(peorm)


def main():
    repl_str()
    spl_str()
    alias()


if __name__ == "__main__":
    main()
