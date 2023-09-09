class Info:

    def __init__(self, name ,age):
        # python 中属性, 方法默认是公开的
        self.name = name
        # 双划线开头的属性或者方法就是私有的，对外不可见
        self.__age = age


    def show(self):
        # 内部可以访问
        return f"{self.name}:{self.__age}"



def main():
    info = Info("alex", 18)
    print(info.name)
    print(info.show())

    # 外部强行访问格式(obj._ClassName__field)
    print(info._Info__age)



if __name__ == "__main__":
    main()
