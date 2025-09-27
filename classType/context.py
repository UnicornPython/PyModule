

"""
> 在前面已经学到, 使用 with 语句可以自动调用 __enter__() 和 __exit__() 方法
  完成一些上下文文管理的功能。

> 如果存在一定的限制条件，类中没有实现 __enter__() 和 __exit__() 方法, 怎么
  使用 with 语句呢？

"""
from contextlib import contextmanager
from typing import ContextManager


class Database:

    def __init__(self, name: str):
        self.name = name

    def close(self):
        print(f"关闭数据库: {self.name}")

    def send(self, sql: str):
        print(sql)


# 1.方法: 使用一个类来继承原本的类, 在继承类中实现，然后使用
class DbManager(Database):

    def __init__(self, name: str):
        super().__init__(name)

    def __enter__(self):
        print("打开数据库")
        # 返回兑现
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# 2.方法，使用一个类进行组合
class AutoDatabase:

    def __init__(self, name: str) :
        self.db = Database(name)

    def __enter__(self):
        print("打开数据库")
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


# 3. 方法：使用函数来定义一个上下文管理器(推荐)
@contextmanager
def db_manager(name: str) :
    print("打开数据库")
    db = Database(name)
    try:
        # 简单来解释来说，是装饰器帮助你建立了一个结构
        # 在 __enter__ 中调用了调用了这个生成器的next()
        # 在 __exit__ 中调用了调用了这个生成器的next()
        yield db
    finally:
        db.close()
        print("close db")


def main():

    # 1 test (构建一个实例, 使用 as 启用了一个别名)
    with DbManager("user") as db:        # call __enter__()
        db.send("select * from user")     # after call __exit__()

    # 2. test (组合)
    with AutoDatabase("user") as db:
        db.send("select * from user")

    # 3. test (函数)
    with db_manager("user") as db:
        db.send("select * from user")


if __name__ == "__main__":
    main()


