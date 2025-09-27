
# python 11 引入的标准库，用于解析 toml 格式的配置文件
# 如果是之前的版本，需要安装 toml

import tomllib
from pprint import pp


def main():
    with open("./emlib/conf/cofig.toml", "br") as f:
        content = tomllib.load(f)
    pp(content)


if __name__ == "__main__":
    main()
