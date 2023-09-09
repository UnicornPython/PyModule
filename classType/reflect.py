
"""
python 中的反射
>-------------------------------------------------------------

 getattr()
 setattr()
 hasattr()

"""
import importlib
import sys

class Pilot:

    def __init__(self, name = "alex"):
        self.name = name


    def find(self, name):
        return name


def reflect_method():
    # 构建类的实例, 
    # 可以使用如下的几个方法来判断类的实例中的属性
    # hasattr : 是否具有某个属性, 
    # getattr : 获取指定属性的值, 对应的是类中的 __getattribute__() 魔术方法
    # setattr : 为对象添加某个属性的值, 对应的是类中的 __setattr__() 魔术方法
    pilot = Pilot();
    if hasattr(pilot, "ship"):
        print(getattr(pilot, "ship"))
    else:
        setattr(pilot, "ship", "show")
        print(getattr(pilot, "ship"))

    print(pilot.__getattribute__("ship"))

    print(hasattr(pilot, "find"))


    # 获取方法执行
    if hasattr(pilot, "find"):
        func = getattr(pilot, "find");
        result = func("hello")
        print(result)


def reflect_use_case():
    """
    在一些框架里面,在开发的时候通常是不知道后续使用框架的人
    具体使用的情况, 就需要写一些比较灵活的，通用性的逻辑。
    ----------------------
    以一个发送消息场景，当前需要发送消息，
    但是写框架的人知道发送消息，但是不知道你要使用什么平台，
    这时候你可能需要在配置文件中将你要发送消息的平台，方法等
    放入一个列表中，由框架加载执行

    ------------------------------------------------------------
    """
    PlatFormList = [
        "msgsender.WeChat.delivery",
        "msgsender.DingDing.send"
    ]

    for path_str in PlatFormList:
        # 这里涉及到模块的导入，因此放到了外层 app.py 中测试了
        module_path, func_name = path_str.rsplit(".", maxsplit=1) # 从右边查找第一个`.`切分
        md = importlib.import_module(module_path)
        func = getattr(md, func_name)

        func("CPU 干烧了")



def main():
    reflect_method()



if __name__ == "__main__":
    main()
