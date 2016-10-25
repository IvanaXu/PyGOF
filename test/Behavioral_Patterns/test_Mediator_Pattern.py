# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-25 19:30:19
# @goal test for Mediator Pattern
import datetime


class ChatRoom:
    def showMessage(self, user, message):
        print str(datetime.datetime.now()) + '[' + user.getName() + ']' + message


class User:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def sendMessage(self, message):
        ChatRoom().showMessage(self, message)


class MediatorPatternDemo:
    def run(self):
        robert = User("Robert")
        john = User("John")
        robert.sendMessage("Hi! John!")
        john.sendMessage("Hello! Robert!")
M = MediatorPatternDemo()
M.run()

