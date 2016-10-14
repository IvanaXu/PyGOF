# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 15:34:54
# @goal test Model-View-Controller


class Student:
    def __init__(self):
        self.rollNo = None
        self.name = None

    @property
    def rollNo(self):
        return self.rollNo

    @rollNo.setter
    def rollNo(self, rollNo):
        self.rollNo = rollNo

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name
# A = Student()
# A.name, A.rollNo = '1', '2'
# print A.name, A.rollNo


class StudentView:
    def __init__(self):
        return

    def printStudentDetails(self, studentName, studentRollNo):
        print "Student: "
        print "Name: " + studentName
        print "Roll No: " + studentRollNo
# B = StudentView()
# B.printStudentDetails('ivan', '3112005932')


class StudentController:
    def __init__(self, model, view):
        self.model, self.view = model, view
        return

    def getStudentName(self):
        return self.model.name

    def setStudentName(self, name):
        self.model.name = name

    def getStudentRollNo(self):
        return self.model.rollNo

    def setStudentRollNo(self, rollNo):
        self.model.rollNo = rollNo

    def updateView(self):
        self.view.printStudentDetails(self.model.name, self.model.rollNo)


class MVCPatternDemo:
    def __init__(self):
        return

    def run(self):
        # get data
        model = self.retriveStudentFromDatabase()

        # view input
        view = StudentView()
        controller = StudentController(model, view)
        controller.updateView()

        # update data
        controller.setStudentName('John')Q
        controller.updateView()
        return

    def retriveStudentFromDatabase(self):
        student = Student()
        student.name = "Robert"
        student.rollNo = "10"
        return student
C = MVCPatternDemo()
C.run()

