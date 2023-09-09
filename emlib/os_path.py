import os 
import shutil

"""
> python 中路径的处理
"""

def walk():
    # 这个 api 会自动根据文件属性，如果是文件夹再自动遍历
    # walk 会返回一个元组，
    #    > 第一项是当前遍历问价夹的 base_dir
    #    > 第二项是当前遍历文件夹内的子问价夹列表
    #    > 第三项是当前遍历文件夹内的文件列表
    # ---------------------------------------------------------------
    # 这里我们直接使用解构语法将返回的数据结构解开
    for base_dir, folder_list, file_list in  os.walk(os.path.abspath("../")):
        for name in file_list: 
            if not name.endswith(".py"):
                continue
            file_path = os.path.join(base_dir, name)
            print(file_path)




def listdir():
    # 这个 api 一般只用于获取文件夹下的一级文件列表，
    # 如果需要查找多级的目录，则需要自己根据当前节点的属性是否为文件夹递归查找
    list = os.listdir(os.path.abspath("../"))
    for item in list:
        print(item)
    


def remove_dir():
    # 删除文件夹, 已经文件夹中的内容
    shutil.rmtree(os.path.join("temp"))



def remove_file():
    # 删除文件, 无法删除文件
    os.remove(os.path.join("temp", "log.log"))



def isdir():
    # 判断是否为文件夹
    print(os.path.isdir("/usr/local/share/nginx"))


def mkdir():

    file_path = os.path.join("temp", "log.log")
    fold_path = os.path.dirname(file_path)

    if not os.path.exists(fold_path):
        os.makedirs(fold_path)
    else:
        print("directory already exists")

    with open(file_path, mode="a", encoding="utf-8") as f:
        f.write("hello world")


def exists_path():
    # 返回一个布尔值
    b = os.path.exists("/usr/opt/last")
    print(b)
    file_path = os.path.join("slogan", "log.file")
    if os.path.exists(os.path.dirname(file_path)):
        # 文件不存在会自动创建，但是文件夹不存在会报错
        with open(file_path, mode = "a", encoding="utf-8") as f:
            f.write("{user}\n")
    else: 
        print("directory is not exists")



def join_path():
    # 路径合并
    apath = os.path.join("user", "local", "share", "lua")
    print(apath)



def get_path():
    # __file__ 表示当前执行的脚本文件的路径
    # dirname() 最后一个`/`之前的内容
    print(os.path.dirname(__file__))
    print(os.path.dirname("/user/lib/share/nginx"))

    # abspath() 表示绝对路径
    print(os.path.abspath(__file__))
    print(os.path.abspath("./"))



def main():
   get_path()
   join_path()
   exists_path()
   mkdir()
   isdir()
   # remove_file()
   # remove_dir()
   listdir()
   walk()



if __name__ == "__main__":
    main()

