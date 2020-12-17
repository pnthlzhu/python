#所有的类名要求首字母大写，多个单词使用驼峰式命名
"""
    class 类名(父类):
        属性：特征

        方法：动作
"""

class Employee:
    "类的文档字符串"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")

    def displayCount(self):
        print("total employee %d" %Employee.empCount)

    def displayEmployee(self):
        print("name: ", self.name, ", salary: ", self.salary)

    def prt(self):
        print(self)
        print(self.__class__)

"""
e1 = Employee("hlzhu", 8000)
e2 = Employee("ghy", 6000)

e1.displayCount()
e2.displayCount()

e1.displayEmployee()
e2.displayEmployee()

e1.prt()
"""

#python内置类属性
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

"""
e1 = Employee("temp", 10)
e2 = e1
e3 = e1

print(id(e1))
print(id(e2))
print(id(e3))

del e1
del e2
del e3
"""