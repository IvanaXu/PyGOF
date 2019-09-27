# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 19:51:14
# @goal test Bridge


class DrawAPI:
    def __init__(self):
        return

    def drawCircle(self, radius, x, y):
        return


class GreenCircle(DrawAPI):
    def drawCircle(self, radius, x, y):
        print("Drawing Circle[ color: green, radius: " + str(radius) + ", x: " + str(x) + ", " + str(y) + "]")


class RedCircle(DrawAPI):
    def drawCircle(self, radius, x, y):
        print("Drawing Circle[ color: red, radius: " + str(radius) + ", x: " + str(x) + ", " + str(y) + "]")


class Shape:
    def __init__(self):
        self.drawAPI = None

    def Shape(self, drawAPI):
        self.drawAPI = drawAPI

    def draw(self):
        return


class Circle(Shape):
    def __init__(self, x, y, radius, drawAPI):
        Shape.__init__(self)
        self.drawAPI = drawAPI
        self.x, self.y, self.radius = x, y, radius

    def draw(self):
        self.drawAPI.drawCircle(self.radius, self.x, self.y)


class BridgePatternDemo:
    def __init__(self):
        redCircle = Circle(100, 100, 10, RedCircle())
        greenCircle = Circle(100, 100, 10, GreenCircle())
        redCircle.draw()
        greenCircle.draw()
BridgePatternDemo()

