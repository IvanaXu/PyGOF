# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-19 21:43:58 
# @goal tPatterns for Facade Pattern


class Shape:
    def __init__(self):
        return

    def draw(self):
        return


class Rectangle(Shape):
    def draw(self):
        print("Rectangle::draw()")


class Square(Shape):
    def draw(self):
        print("Square::draw()")


class Circle(Shape):
    def draw(self):
        print("Circle::draw()")
# Rectangle Square Circle


class ShapeMaker:
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()

    def drawCircle(self):
        self.circle.draw()

    def drawRectangle(self):
        self.rectangle.draw()

    def drawSquare(self):
        self.square.draw()


class FacadePatternDemo:
    def run(self):
        shapeMaker = ShapeMaker()
        shapeMaker.drawCircle()
        shapeMaker.drawRectangle()
        shapeMaker.drawSquare()
F = FacadePatternDemo()
F.run()

