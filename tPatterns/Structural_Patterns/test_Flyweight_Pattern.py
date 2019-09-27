# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-20 17:27:02
# @goal test for Flyweight Pattern
import random


class Shape:
    def __init__(self):
        return

    def draw(self):
        return


class Circle(Shape):
    def __init__(self, color):
        Shape.__init__(self)
        self.color = color
        self.x, self.y, self.radius = 0, 0, 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setRadius(self, radius):
        self.radius = radius

    def draw(self):
        print("Circle: Draw() [Color : " + self.color + \
                                ", x : " + str(self.x) + \
                                ", y : " + str(self.y) + \
                                ", radius :" + str(self.radius)
              )


class ShapeFactory:
    def __init__(self):
        self.circle = None
        self.circleMap = []

    def getCircle(self, color):
        if color not in self.circleMap:
            self.circle = Circle(color)
            self.circleMap.append(color)
            print("Creating circle of color : " + color)
        return self.circle


class FlyweightPatternDemo:
    def __init__(self):
        self.colors = ["Red", "Green", "Blue", "White", "Black"]
        self.circle = None

    def run(self):
        S = ShapeFactory()
        for i in range(0, 20):
            # self.circle = ShapeFactory().getCircle(self.getRandomColor()) # Error
            self.circle = S.getCircle(self.getRandomColor())
            self.circle.setX(self.getRandomX())
            self.circle.setY(self.getRandomY())
            self.circle.setRadius(100)
            self.circle.draw()
        return

    def getRandomColor(self):
        return self.colors[random.randint(0, len(self.colors)-1)]

    def getRandomX(self):
        return random.randint(0, 100)

    def getRandomY(self):
        return random.randint(0, 100)
F = FlyweightPatternDemo()
F.run()

