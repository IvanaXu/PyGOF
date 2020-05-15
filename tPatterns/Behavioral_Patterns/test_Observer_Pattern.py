# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-25 21:00:02
# @goal test for Observer Pattern


class Subject():
    def __init__(self):
        self.observers = []
        self.state = 0

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def attach(self, observer):
        self.observers.append(observer)
        self.notifyAllObservers()

    def notifyAllObservers(self):
        for observer in self.observers:
            observer.update()


class Observer:
    def update(self):
        return


class BinaryObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("Binary String: " + bin(self.subject.getState()))
# BinaryObserver


class OctalObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("Octal String: " + oct(self.subject.getState()))
# OctalObserver


class HexaObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("Hex String: " + hex(self.subject.getState()))
# HexaObserver


class ObserverPatternDemo:
    def run(self):
        self.subject = Subject()
        BinaryObserver(self.subject)
        OctalObserver(self.subject)
        HexaObserver(self.subject)

        print("First state change: 15")
        self.subject.setState(15)

        print("Second state change: 10")
        self.subject.setState(10)


O = ObserverPatternDemo()
O.run()



