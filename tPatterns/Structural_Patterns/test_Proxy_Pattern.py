# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-20 19:11:22
# @goal tPatterns for Proxy Pattern


class Image:
    def __init__(self):
        return

    def Image(self):
        return


class RealImage(Image):
    def __init__(self, filename):
        Image.__init__(self)
        self.filename = filename
        self.loadFromDisk()

    def display(self):
        print("Displaying " + self.filename)

    def loadFromDisk(self):
        print("Loading " + self.filename)
# R = RealImage('file')


class ProxyImage(Image):
    def __init__(self, filename):
        Image.__init__(self)
        self.filename = filename
        self.realImage = None

    def display(self):
        if not self.realImage:
            self.realImage = RealImage(self.filename)
        self.realImage.display()


class ProxyPatternDemo:
    def run(self):
        image = ProxyImage('test_10mb.jpg')
        image.display()
        print(' ')
        image.display()
P = ProxyPatternDemo()
P.run()

