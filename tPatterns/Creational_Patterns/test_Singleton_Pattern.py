# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 17:16:26
# @goal test Singleton Pattern


class SingleObject:
    def __init__(self):
        self.instance = None

    def getInstance(self):
        self.instance = SingleObject()
        return self.instance

    def showMessage(self):
        print('Hello World')


class SingletonPatternDemo:
    def __init__(self):
        object = SingleObject().getInstance()
        object.showMessage()


SingletonPatternDemo()



