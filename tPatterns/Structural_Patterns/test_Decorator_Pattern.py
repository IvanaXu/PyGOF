# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-19 21:14:15
# @goal tPatterns for Decorator Pattern


class Shape:
    def __init__(self):
        return

    def draw(self):
        return


class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")


class Circle(Shape):
    def draw(self):
        print("Shape: Circle")


# Rectangle Circle


class ShapeDecorator:
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape

    def draw(self):
        self.decoratedShape.draw()


class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decoratedShape):
        ShapeDecorator.__init__(self, decoratedShape)

    def draw(self):
        self.decoratedShape.draw()
        self.setRedBorder(self.decoratedShape)

    def setRedBorder(self, decoratedShape):
        # No Good
        print("Border Color: Red")


class DecoratorPatternDemo:
    def run(self):
        circle = Circle()
        redCircle = RedShapeDecorator(Circle())
        redRectangle = RedShapeDecorator(Rectangle())
        print("Circle with normal border")
        circle.draw()

        print("\nCircle of red border")
        redCircle.draw()

        print("\nRectangle of red border")
        redRectangle.draw()
D = DecoratorPatternDemo()
D.run()

