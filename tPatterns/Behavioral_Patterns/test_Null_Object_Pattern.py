# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-26 10:06:02
# @goal test for Null Object Pattern


class AbstractCustomer:
    def __init__(self):
        self.name = ''

    def isNil(self):
        return

    def getName(self):
        return


class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        AbstractCustomer.__init__(self)
        self.name = name

    def isNil(self):
        return False

    def getName(self):
        return self.name


class NullCustomer(AbstractCustomer):
    def __init__(self):
        AbstractCustomer.__init__(self)

    def isNil(self):
        return True

    def getName(self):
        return "Not Available in Customer Database"


class CustomerFactory:
    def __init__(self):
        self.names = ['Rob', 'Joe', 'Julie']

    def getCustomer(self, name):
        i = 0
        for i in self.names:
            if i.upper() == name.upper():
                return RealCustomer(name)
        return NullCustomer()


class NullPatternDemp:
    def run(self):
        customer1 = CustomerFactory().getCustomer("Rob")
        customer2 = CustomerFactory().getCustomer("Bob")
        customer3 = CustomerFactory().getCustomer("Julie")
        customer4 = CustomerFactory().getCustomer("Laura")

        print("Customers:")
        print(customer1.isNil(),  ':', customer1.getName())
        print(customer2.isNil(), ' :', customer2.getName())
        print(customer3.isNil(),  ':', customer3.getName())
        print(customer4.isNil(), ' :', customer4.getName())
N = NullPatternDemp()
N.run()

