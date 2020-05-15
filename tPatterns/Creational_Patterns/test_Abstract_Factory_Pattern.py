# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 16:36:15 
# @goal test Abstract Factory Pattern


class Shape:
    def __init__(self):
        return

    def draw(self):
        return
# Circle Rectangle Square


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Color:
    def __init__(self):
        return

    def fill(self):
        return
# Blue Green Red


class Blue(Color):
    def fill(self):
        print("Inside Blue::fill() method.")


class Green(Color):
    def fill(self):
        print("Inside Green::fill() method.")


class Red(Color):
    def fill(self):
        print("Inside Red::fill() method.")


class AbstractFactory:
    def __init__(self):
        return

    def getShape(self, shapeType):
        return

    def getColor(self, colorType):
        return

# ShapeFactory ColorFactory


class ColorFactory(AbstractFactory):
    def getColor(self, colorType):
        if not colorType:
            return
        elif colorType == 'BLUE':
            return Blue()
        elif colorType == 'GREEN':
            return Green()
        elif colorType == 'RED':
            return Red()
        return

    def getShape(self, shapeType):
        return


class ShapeFactory(AbstractFactory):
    def getShape(self, shapeType):
        if not shapeType:
            return
        elif shapeType == 'CIRCLE':
            return Circle()
        elif shapeType == 'RECTANGLE':
            return Rectangle()
        elif shapeType == 'SQUARE':
            return Square()
        return

    def getColor(self, colorType):
        return


class FactoryProducer:
    def getFactory(self, choice):
        if choice == 'SHAPE':
            return ShapeFactory()
        elif choice == 'COLOR':
            return ColorFactory()
        return


class AbstractFactoryPatternDemo:
    def __init__(self):
        self.shapeFactory = FactoryProducer().getFactory("SHAPE")
        self.colorFactory = FactoryProducer().getFactory("COLOR")
        self.shape_list = ["CIRCLE", "RECTANGLE", "SQUARE"]
        self.color_list = ["BLUE", "GREEN", "RED"]

    def run(self):
        for i in self.shape_list:
            shape = self.shapeFactory.getShape(i)
            shape.draw()

        for i in self.color_list:
            color1 = self.colorFactory.getColor(i)
            color1.fill()


A = AbstractFactoryPatternDemo()
A.run()



