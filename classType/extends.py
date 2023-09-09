
text = r"""
Python 中类的继承关系
> ------------------------------------------------------
    1. python 是支持多继承的
    2. python 的多继承是有先后顺序的, __mro__
> ------------------------------------------------------

python2 和 python3 之间继承的差异

   > python2 中没有显式继承 object 的类叫做经典类
     显式继承了 object 的类叫做新式类，与 python3 相同
   > python3 中所有的类都继承了object 类，不需要显式声明


   新式类与经典类在一些特殊的场景查找某个方法在多继承父类
   的顺序不同( __mro__ 返回的结果不同)

> ------------------------------------------------------


                      ###############
                      # BaseServer  #
                      ###############
                            |
                            |
#########             ##############
# Mixin #             #   Server   #
#########             ##############
     \                 /
      \               /
    ####################
    # ThreadingServer  #
    ####################

"""

class BaseServer:

    def run_server(self):
        self.handler();


    def handler(self):
        pass


class Server(BaseServer):

    def handler(self):
        self.process()
        

    def process(self):
        print(123)


class Mixin:
    def process(self):
        print("999")


class ThreadingServer(Mixin, Server):
    pass


def main():

    # 下面这段内容中的执行过程 (类的继承图见文件首)
    #  > 1.run_server() 方法会现在 Mixin 中查找,找不到找它的父类.
    #      找不到则查找 Server类, Server 找不到，继续查找它的父类
    #  > 2.运行 BaseServer 中的 run_server(),调用这个方法的对象
    #      是 ThreadingServer, self 就是 ThreadingServer,
    #  > 3.查找 self.handler 方法，ThreadingServer 没有，则继续
    #      查找 Mixin 类以及它的父类，找不到则查找 Server 类中找到了
    #  > 4.运行时传入的 self 还是 Threading 类型，继续查找要执行的
    #      process() 方法，
    #  > 5.ThreadingServer 没有 process 方法，则查找 Minix 中是否有
    #      process() 方法，找打则执行，
    #  > 6.输出 999
    obj = ThreadingServer()
    obj.run_server() # 999


if __name__ == "__main__":
    main()
