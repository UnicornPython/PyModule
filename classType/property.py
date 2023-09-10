"""
    python 中的 属性
> --------------------------------
   属性的作用就是在类中封装一些功能
   向外提供某种以属性一样的简单访问

"""


class Info:
    # 字段私有不对外开放
    def __init__(self, name):
        self.__name = name

    # 将方法转换为一个类的属性
    @property
    def alias(self):
        return self.__name

    # 为属性添加 setter 方法
    @alias.setter
    def alias(self, name):
        self.__name = name

    # 为属性添加 deleter 方法
    @alias.deleter
    def alias(self):
        pass


class Point:

    def __init__(self):
        self.position = 0

    def getx(self):
        return self.position

    def setx(self, value):
        self.position = value

    def delx(self):
        del self.position

    # 使用的这样的方法，虚构一个 x 的属性，
    # 同时这个 x 属性封装了访问与修改的方法
    x = property(getx, setx, delx)


class Pagination: 
    def __init__(self, total, page_count, page_num):
        self.total = total
        self.page_count = page_count
        self.page_num = page_num

    @property
    def start(self):
        return (self.page_num - 1) * self.page_count
    
    @property
    def end(self):
        return self.page_num * self.page_count


def main():
    info = Info("alex")
    # 自动调用 setter 方法
    info.alias = "maria"
    # 自动执行 alias 方法
    print(info.alias)
    # 自动执行 deleter 方法
    del info.alias

    ##################################

    point = Point()
    point.x = 234
    print(point.x)
    del point.x

    ##################################

    page = Pagination(10, 4, 2)
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 这里就是直接使用 start, end 属性实现了分页的功能
    result = data_list[page.start: page.end]
    print(result)


if __name__ == "__main__":
    main()
