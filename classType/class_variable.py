#!/usr/bin/env python

class Config:
    MAX_TIMEOUT = 1000

    def __init__(self, timeout, logpath):
        # 类变量的使用方式，直接使用类名来引用
        if timeout > Config.MAX_TIMEOUT:
            self.timeout = Config.MAX_TIMEOUT
            self.logpath = logpath


def main():
    config = Config(2000, "./logs/")
    print(config.timeout)
    print(config.logpath)


if __name__ == "__main__":
    main()
