
# 该文件作为 package 的入口，当 package 被导入时，__init__.py 文件会被执行
# 主要有以下作用
# 1. 为 package 初始化(设置环境变量，初始化日志等)
# 2. 为 package 指定哪些部分可以被导入
# 3. 包的信息 __version__, __author__
# -------------------------------------------------------------
# python 3.3+ 之后可以没有 __init__.py 文件, 
#      会自动组合为一个 namespace package, 这在差分大型项目时很有用
# 但建议仍然保留__init__.py 文件，即使是空文件


__version__ = "1.0.0"
__author__ = "unicorn"


# 当外部使用例如 from struct import * 时，
# __all__ 中的变量会被导入

from .modulex import x
from . import modulex

__all__ = ["x", "modulex"]

# 导入模块时的五个步骤
# 1.搜寻模块
# 2.执行代码
# 3.封装模块
# 4.缓存模块
# 5.绑定变量
