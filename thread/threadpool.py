#!/usr/bin/python3

from concurrent.futures import ThreadPoolExecutor


def printer(content):
    print(content)


def main():
    with ThreadPoolExecutor(20) as t:
        for _ in range(20):
            t.submit(printer, "main")
        t.shutdown()


if __name__ == "__main__":
    main()
