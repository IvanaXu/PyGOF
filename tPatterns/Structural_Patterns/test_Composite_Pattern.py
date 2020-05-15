# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-19 20:36:37
# @goal test for Composite Pattern


class Employee:
    def __init__(self, name, dept, salary):
        self.name, self.dept, self.salary = name, dept, salary
        self.subordinates = []

    def add(self, e):
        self.subordinates.append(e)

    def remove(self, e):
        self.subordinates.remove(e)

    def getSubordinates(self):
        return self.subordinates

    def toString(self):
        return "Employee :[ Name : " + self.name + ", dept : " + self.dept + ", salary :" + str(self.salary) + " ]"


class CompositePatterDemo:
    def run(self):
        CEO = Employee("John", "CEO", 30000)
        headSales = Employee("Robert", "Head Sales", 20000)
        headMarketing = Employee("Michel", "Head Marketing", 20000)
        clerk1 = Employee("Laura", "Marketing", 10000)
        clerk2 = Employee("Bob", "Marketing", 10000)
        salesExecutive1 = Employee("Richard", "Sales", 10000)
        salesExecutive2 = Employee("Rob", "Sales", 10000)

        CEO.add(headSales)
        CEO.add(headMarketing)

        headSales.add(salesExecutive1)
        headSales.add(salesExecutive2)

        headMarketing.add(clerk1)
        headMarketing.add(clerk2)

        print(CEO.toString())

        for headEmployee in CEO.getSubordinates():
            print(headEmployee.toString())
            for employee in headEmployee.getSubordinates():
                print(employee.toString())


C = CompositePatterDemo()
C.run()



