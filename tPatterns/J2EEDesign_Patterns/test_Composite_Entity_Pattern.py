# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-26 19:36:14
# @goal test for Composite Entity Pattern


class DependentObject1:
    def __init__(self):
        self.data = ''

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data


class DependentObject2:
    def __init__(self):
        self.data = ''

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data


class CoarseGrainedObject:
    def __init__(self):
        self.do1 = DependentObject1()
        self.do2 = DependentObject2()

    def setData(self, data1, data2):
        self.do1.setData(data1)
        self.do2.setData(data2)

    def getData(self):
        return [self.do1.getData(), self.do2.getData()]


class CompositeEntity:
    def __init__(self):
        self.cgo = CoarseGrainedObject()

    def setData(self, data1, data2):
        self.cgo.setData(data1, data2)

    def getData(self):
        return self.cgo.getData()


class Client:
    def __init__(self):
        self.compsiteEntity = CompositeEntity()

    def printData(self):
        for i in self.compsiteEntity.getData():
            print('Data: ' + i)

    def setData(self, data1, data2):
        self.compsiteEntity.setData(data1, data2)


class CompositeEntityPatternDemo:
    def run(self):
        client = Client()
        client.setData("Test", "Data")
        client.printData()
        client.setData("Second Test", "Data1")
        client.printData()
C = CompositeEntityPatternDemo()
C.run()

