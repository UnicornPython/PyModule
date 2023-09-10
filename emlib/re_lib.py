import re

document = r"""
\d : 数字
\D : 非数字
\w : 数字字母(下划线，中划线)
\W : 非数字字母(下划线，中划线),没限定模式的时候包括汉字
\s : 空白字符
\S : 非空白字符

[] : 原子表
() : 原子组
.  : 非换行符的任意字符
*  : 表示匹配次数(0-n)
?  : 表示匹配次数(0-1)
+  : 表示匹配次数(1-n)
|  : 表示匹配的时候的或者关系
^  : 表示匹配边界的起始
$  : 表示匹配边界的结束
\  : 转义符号，为了还原字符本身的含义

{m,n} : 表示匹配的次数 (m,n)
{m}: 表示匹配次数 m
{m,} : 表示匹配次数 >= m

"""


def findall():
    text = "楼主太牛逼了,想要 s3435353535@qq.com 和 xxxx@live.com谢谢,手机号也可12314234242,搞起"
    # 提起文本中的内容
    mobile = re.findall(r'\d{11}', text)
    print(mobile)

    # 提取邮箱(最后一个参数可以传入匹配的模式)
    email = re.findall(r'\w+@\w+.\w+', text, re.ASCII)
    print(email)

    ####################################################
    # findall() : 当使用的表达式是原子表显示的，就只会获取原子表中的内容
    sufix = re.findall(r"\w+(@\w+.\w+)", text, re.ASCII)
    print(sufix)

    identifyId = "账号的长度是多少 351818199607081239, 谁的身份证号是340806188901209187X阿里斯巴达"
    # 原子组提取的时候，出现多个原子组的时候，
    # 计算取出的原子组的值时 从左开始计算括号的位置来得到获取值的下表索引
    # 例如下面的示例中获取年份的提取下标应为 1(左起计算的排序为 2)
    res = re.findall(r"(\d{6}(\d{4})(\d{2})(\d{2})\d{3}[\dX])", identifyId)
    print(res)
    for item in res:
        print(item[1])


def format_match():
    email = input("输入邮箱校验格式: ")

    # 返回 一个 Match 对象, group()可以获取匹配文本，start,end 获取匹配项在文本中的位置),
    # 如果有多个匹配的时候也只会返回匹配的第一个, 如果没有匹配返回 None
    # 做格式校验的时候，通常需要添加起止符(^$) 表示文本与规则完整匹配，不是其中一部分满足规则

    # match 匹配的时候直接从起始位置进行匹配，如果不匹配直接返回返回 None, 不会继续往后匹配
    # 通常用于格式校验的场景 
    result = re.match(r'^\w+@\w+.\w+$', email)
    print(result)
    if result:
        print("格式合法")
        print(result.group())
    else:
        print("格式错误")


def search():
    """
    search 用于搜索文本中满足条件的内容，返回一个 Match 对象
    search 会进行全文匹配查找，返回第一个满足匹配条件的文本(不会继续往后搜索)
        > group() 方法可以获取到匹配的文本
        > start() 方法获取匹配时在文本中的起始位置
        > end() 方法获取匹配内容在原始文本的结束位置
    """
    identifyId = "身份证账号长度是多少 351818199607081239, 谁身份证号是340806188901209187X阿里斯巴"
    mathc_obj = re.search(r"\d{17}[\dX]", identifyId)
    if mathc_obj:
        print(mathc_obj.group())
        print(mathc_obj.start())
        print(mathc_obj.end())
    else:
        print("未找到匹配内容")


def split():
    content = "alex,123-3553"
    # split 支持以正则表达式切割
    res = re.split('[,-]', content)
    print(res)


def main():
    findall()
    format_match()
    search()
    split()


if __name__ == "__main__":
    main()
