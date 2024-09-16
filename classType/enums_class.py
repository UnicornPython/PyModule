#!/python

from enum import Enum, Flag, auto


class Color(Enum):
    RED = "R"
    GREEN = "G"
    BLUE = "B"


def create_car(color: Color) -> None:
    match color:
        case Color.RED: 
            print(f"A smoking hot red car was created!")
        case Color.BLUE:
            print(f"a slick smooth blue car was created")
        case Color.GREEN:
            print(f"a calm and gracious green car was created")
        case _:
            print(f" we do not have the color {color} in our database")


def base() -> None:
    print(Color.BLUE)
    print(Color("B"))
    print(Color.GREEN)
    print(repr(Color.RED))
    print(Color.BLUE.name)
    print(Color.BLUE.value)


"""
#####################################################################################################
2. Flag
"""

class HLV(Flag): 
    RED = 1
    GREEN = 2
    BLUE = 4
    YELLOW = 8
    BLACK = 16
    MONTO = 10
    ALL = RED | GREEN | BLUE | YELLOW | BLACK | MONTO


def trans() -> None:
    yellow_and_red = HLV.YELLOW | HLV.RED
    print(yellow_and_red)

    for c in yellow_and_red:
        print(c)


def combine_enums() -> None:
    print(HLV.ALL)
    print(HLV.ALL.value)
    cool_colors: HLV = HLV.RED | HLV.YELLOW | HLV.BLACK
    my_color: HLV = HLV.GREEN

    if my_color in cool_colors:
        print("You have a cool car")
    else:
        print("Sorry, You car is not cool")



def comnine_value() -> None:
    color : HLV = HLV.GREEN | HLV.YELLOW
    # 如果获取 HLV 的值则是联合类型所有值的和
    print(color.value)
    # 当多个联合类型的和相加在一起有一个新的枚举与其相等，
    # 这时候获取到的就是值相等的那个枚举
    print(color)


"""
#####################################################################################################
2. auto
"""

class HSL(Flag):
    """继承自 Flag 则为 2  的指数递增幂"""
    GREY = auto()
    LIGHT = auto()
    COLOR = auto()


class HSLENUM(Enum):
    """继承自 enum 则值为递增序列"""
    GREY = auto()
    LIGHT = auto()
    COLOR = auto()

def auto_value() -> None:
    """使用 auto 自动维护值"""
    print(HSL.GREY.value)
    print(HSL.LIGHT.value)
    print(HSL.COLOR.value)
    print(HSLENUM.GREY.value)
    print(HSLENUM.LIGHT.value)
    print(HSLENUM.COLOR.value)


def main() -> None:
    base()
    create_car(Color.GREEN)
    trans()
    combine_enums()
    comnine_value()
    auto_value()


if __name__ == "__main__":
    main()
