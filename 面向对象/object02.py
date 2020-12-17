"""
类的继承
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。

通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
"""
class Parent:
    parentAttr = 100

    def __init__(self):
        print("call parent constructor")

    def parentMethod(self):
        print("call parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("parent attr:%d" %(Parent.parentAttr))

    def myMethod(self):
        print("call parent myMethod")

class Child(Parent):
    def __init__(self):
        print("call child constructor")

    def childMethod(self):
        print("call child method")

    def myMethod(self):
        print("call child myMethod")

c = Child()

c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

c.myMethod()