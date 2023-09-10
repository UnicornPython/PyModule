from xml.etree import ElementTree


def parse_base():
    text = """
    <data>
        <country name="Liechtenstein">
            <rank update="yes">2</rank>
            <year>2023</year>
            <gdppc>14110</gdppc>
            <neighbor direction="E" name="Austria" />
            <neighbor direction="W" name="Switzerland" />
        </country>
        <country name="Panama">
            <rank update="yes">69</rank>
            <year>2026</year>
            <gdppc>13600</gdppc>
            <neighbor direction="W" name="Costa Rica" />
            <neighbor direction="E" name="Colobia"/>
        </country>
    </data>

    """

    # 加载 xml
    root = ElementTree.XML(text)

    # 找到第一个
    node = root.find("country")
    if not node:
        return

    print(node)
    # 返回某个节点的 tag 值
    print(node.tag)
    # 返回某个节点的所有属性，是一个 key=value 字典
    print(node.attrib)

    # 找到所有的标签
    node_list = root.findall("country")
    for node in node_list:
        print(node.tag, node.attrib)

        # 继续遍历内部的标签节点
        for child in node:
            print(child.tag, child.text, child.attrib)


def parse_demo():

    text = """
        <xml>
            <ToUserName>Alex</ToUserName>
            <FromUserName>root</FromUserName>
            <CreateTime><12345677</CreateTime>
            <MsgType>Text</MsgType>
            <Content>upline</Content>
            <MsgId></1233453546467577</MsgId>
            <MsgDataId>xxxxx</MsgDataId>
            <Idx>11</Idx>
        </xml>
    """

    # 解析数据，构建成为字典
    data = {}
    root = ElementTree.XML(text)
    for node in root:
        data[node.tag] = node.text


def main():
    parse_base()
    parse_demo()


if __name__ == "__main__":
    main()
