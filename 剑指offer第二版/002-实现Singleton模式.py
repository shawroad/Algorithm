"""

@file  : 002-实现Singleton模式.py

@author: xiaolu

@time  : 2019-09-18

"""
class Singleton:
    # 单例类
    __instance = False

    def __new__(cls, *args, **kwargs):
        # python中创建对象过的第一关不是初始化__init__()  而是__new__()
        if cls.__instance == None:
            cls.__instance = object.__new__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print("对象1:", id(obj1))
    print("对象2:", id(obj2))
    # 输出
    # 对象1: 93993201898176
    # 对象2: 93993201898176
