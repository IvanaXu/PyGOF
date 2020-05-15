# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 10:12:29
# @goal test Factory Pattern


class Shape:
    def __init__(self):
        return

    def draw(self):
        return


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeFactory:
    def __init__(self):
        return

    def getShape(self, share_type):
        if not share_type:
            return
        elif share_type == 'RECTANGLE':
            return Rectangle()
        elif share_type == 'SQUARE':
            return Square()
        elif share_type == 'CIRCLE':
            return Circle()
        else:
            return


class FactoryPatternDemo:
    def __init__(self):
        shapefactory = ShapeFactory()
        shape_rectangle = shapefactory.getShape('RECTANGLE')
        shape_square = shapefactory.getShape('SQUARE')
        shape_circle = shapefactory.getShape('CIRCLE')

        shape_rectangle.draw()
        shape_square.draw()
        shape_circle.draw()


FactoryPatternDemo()



