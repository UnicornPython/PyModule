#!/usr/bin/env python

"""
python 中的 json 库
-----------------------------------------
 json 就是特殊格式的字符串
-----------------------------------------
python 数据类型于json 中数据的对应关系
 str   ""
 int   number
 float number
 list  []
 tuple []
 None  null
 False false

python 中不支持的格式
 - datetime
------------------------------------------

 >

"""

import json
from datetime import datetime
from json import JSONEncoder

data_list = [
    {"name": "alex", "age": 19, "ctime": datetime.now()},
    {"name": "alex", "age": 19, "ctime": datetime.now()}
]


# json 内部进行 json 序列化的时候，
# 会调用 JSONEncoder default 方法
# 我们继承这个类，然后重写 default 方法，将时间处理成字符串
class DateEncode(json.JSONEncoder):
    def default(self, o):
        # 需要序列化的对象每一个字段都会调用这个方法
        if type(o) is datetime:
            return o.strftime("%Y-%m-%d")
        
        # 然后再调用对应的父类中的default方法，继续处理，这样就不会出错了
        return super().default(o)


def json_loads():
    data = '{ "name": "alex", "age": 18 }'
    dict = json.loads(data)
    print(dict['name'])


def json_dumps():
    """序列化 字典为一个 json 对象"""
    dict = {}
    dict['title'] = "Hello you new pilot"
    dict['hubby'] = ['vollyball', 'pingpong', 'movive']
    res = json.dumps(dict)
    print(res)


def json_convert():
    """
    当我们使用的的字典格式中出现了json 库不支持的数据类型
     - 例如 datetime
    """

    # 解决方案 1, 将不支持的类型想自动转化为字符串的序列化格式
    new_list = [
        {
            k: v.strftime("%Y-%m-%d") if k == "ctime" else v
            for k, v in e.items()
        }
        for e in data_list
    ]
    res = json.dumps(new_list)
    print(res)

    # 解决方案 2. 自定义类型转换器, 通过 cls 参数传入
    result = json.dumps(data_list, cls=DateEncode)
    print(result)


def json_eval():
    """
    现实场景中, 再处理一些外部数据的时候，遇到非标准格式的 json
    可以尝试先使用 eval 进行处理
    """

    data = """
        {
            "content": "this is a test demo",
            "name": "alex",
            "genger": False,
            "sort": (145,675,857,678)
        }
    """
    resolved = eval(data)
    print(resolved)
    print(resolved['sort'])


def main():
    json_dumps()
    json_loads()
    json_convert()
    json_eval()


if __name__ == "__main__":
    main()
