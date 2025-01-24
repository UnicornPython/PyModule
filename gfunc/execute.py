
from functools import partial
from random import choice, choices, sample
from itertools import permutations, combinations_with_replacement
from tkinter import filedialog as fd

# =====================================
# 5 with tkinter open filedialog
# =====================================

def open_file_dialog():
    file_path = fd.askopenfilename(
        title='选择一个文件', 
        initialdir='/home/unicorn/codelib/PyCode', 
        filetypes=(("PNG", "*.png"), ("Python", "*.py"))
    )
    print(file_path)

# =====================================
# 4.随机抽样
# =====================================
def choice_sample():
    # 随机抽取样本
    list = [ '❌', '⭕', '🆗', '💿', '👍', '👎']
    # 随机抽取三个不重复的元素
    sam = sample(list, 3)
    print(sam)
    # 随机抽取一个
    select = choice(list)
    print(select)
    # 随机抽取，元素不保证不重复
    cho = choices(list, k=3)
    print(cho)


# =====================================
# 3.组合元素
# =====================================

def permu_combine():
    # 元素的排列组合(permutations 进行元素的排列组合)
    # 返回所有可能的组合元组
    per = permutations(['A', 'B', 'C', 'A'])
    for (a, b, c, d) in per:
        print(a, b, c, d)

    # 数组中随机选择指定数量的元素的组合
    combine= combinations_with_replacement([1, 2, 3], 2)
    # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# =====================================
# 2.curry 函数
# =====================================
def partials():
    with_rgb = partial(color_alpha, a=1.0)
    with_rgb(255, 0, 0)
    with_alpha = partial(color_alpha, r=255, g=255, b=0)
    with_alpha(a=0.6)


def color_alpha(r: int, g: int, b: int, a: float) -> None:
    print(f"rbga({r}, {g}, {b}, {a})")

    
# =====================================
# 1.执行代码字符串
# =====================================
def execute():
    text = """
print("this is a  long text")
for i in range(3):
    print(i)

print('I am code being execute from a string')
print("Never execute exec() with file you don't trust")
    """
    exec(text)

def main(): 
    # 可以将文本作为代码执行
    execute()

    # 帮助完成函数柯里化的工具
    partials()

    # 元素的排列组合
    permu_combine()

    # 随机样本
    choice_sample()

    #打开文件选择对话框
    open_file_dialog()

if __name__ == "__main__":
    main()
