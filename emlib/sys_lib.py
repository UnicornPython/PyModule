import sys


def main():
    # 运行脚本传入的参数, 第一个是当前脚本的路径, 再往后就是脚本传入的参数
    #  ['/home/unicorn/codelib/PythonCode/PyModule/emlib/syslib.py']
    print(sys.argv)

    # 运行 python 文件的时候会在哪些地方加载解析模块
    # 例如运行当前模块的获取到
    """
    [
        '/home/unicorn/codelib/PythonCode/PyModule/emlib',
        '/usr/lib64/python311.zip',
        '/usr/lib64/python3.11',
        '/usr/lib64/python3.11/lib-dynload',
        '/usr/local/lib64/python3.11/site-packages',
        '/usr/local/lib/python3.11/site-packages',
        '/usr/lib64/python3.11/site-packages',
        '/usr/lib/python3.11/site-packages'
    ]
    """
    print(sys.path)


if __name__ == "__main__":
    main()
