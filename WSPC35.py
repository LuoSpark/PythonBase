#coding:utf-8
import sys
import os

class Fruit(object):
    total = 0
    @classmethod
    # @staticmethod
    def print_total(cls):
        print cls.total
        print id(Fruit.total)
        print id(cls.total)

    @classmethod
    # @staticmethod
    def set(cls, value):
        print "calling class_method(%s, %s)" %(cls, value)
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

if "__main__" == __name__:
    app1 = Apple()
    app1.set(200)
    # app1.set(app1,200)
    app2 = Apple()
    org1 = Orange()
    org1.set(300)
    # org1.set(org1,300)
    org2 = Orange()
    app1.print_total()
    org1.print_total()