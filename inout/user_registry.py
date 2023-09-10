import hashlib
import os
from datetime import datetime

MD5_SALT = "awjzkehallasrtalwthsldsdf!@@#454"


def md5(data_str):
    """md5 加密"""
    obj = hashlib.md5(MD5_SALT.encode("utf-8"))
    obj.update(data_str.encode("utf-8"))
    return obj.hexdigest()


def generate_path():
    ctime = datetime.now()
    dir_path = ctime.strftime("%Y-%m-%d")
    file_path = ctime.strftime("%H-%M")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print("存储文件夹已经存在")

    return os.path.join(dir_path, file_path)


def run():
    # 1. 获取输入
    user = input("请输入用户名: ")
    pwd = input("请输入密码: ")
    md5_pwd = md5(pwd)

    # 2. 生成存储格式
    line = f'{user}.{md5_pwd}'

    # 3. 生成存储路径
    file_path = generate_path()
    print(f'create file {file_path}')

    with open(file_path, mode="a", encoding="utf-8") as f:
        f.write(line)


def main():
    run()


if __name__ == "__main__":
    main()
