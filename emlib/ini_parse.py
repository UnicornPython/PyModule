
import configparser

"""
> 专用于 *.ini 文件(软件的配置文件)的解析
----------------------------------------------
[server]
v1=123
v2=234

[client]
v5=111
----------------------------------------------
"""

def main():

    config = configparser.ConfigParser()

    # 1.加载文件
    config.read("./conf/app.ini", encoding="utf-8") 
    print(config)

    # 2. 读取节点
    v1 = config.sections()
    print(v1)


    # 3.判断节点是否存在
    b = config.has_section("server")
    if not b:
        return

    # 4.键值对
    v2 = config.items("server")
    for k, v in v2:
        print(k, v)


    # 判断某个 key 是否存在
    if not config.has_option("client", "v5"):
        return


    # 获取某个单独的值
    print(config.get("client", "v5")) 


    # 添加节点
    config.add_section('group')
    config.set("group","name", "alex")
    config.set("group","age", "18")


    # 删除节点
    config.remove_section("client")


    # 默认的操作都是在内存中操作，如果操作后需要写入到文件中
    with open("./conf/app.ini", mode='w', encoding="utf-8") as f:
        config.write(f)


if __name__ == "__main__":
    main()

