# ################################################
# python 3.10 中引入的模式匹配功能
# ################################################

# 匹配字典
def match_dict() :

    ...


# 匹配守卫
def match_protect():
    ...



def match_list():

    #pick = ["go", "lock"]
    pick = ["go", "run"]

    match(pick):
        # 可以进行完整的匹配, 当元素数量不匹配的时候不会进入该 case
        case ["go", "mod"]:
            print("init project")
        # 可以在匹配的时候，完成变量的自动解构,分支中可以使用这些变量
        case ["go", command]:
            print(f"go {command}")
        # 默认分支，其他分支不匹配的时候会进入默认分支
        case _:
            print("other")



def main() -> None:
    match_list()


if __name__ == "__main__":
    main()
