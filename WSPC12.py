#encoding:utf-8
__author__ = 'luoxt'


import types

class UserInt(int):
    def __init__(self, val = 0):
        self._val = int(val)


if __name__ == "__main__":
    uInt = UserInt(2)
    if type(uInt) is types.IntType:
        print u"应该输出这句"
    else:
        print u"你看到这句输出，就应该知道为什么不推荐对非内置类型使用type来求类型了"

