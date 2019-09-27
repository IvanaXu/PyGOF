# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-20 20:53:16
# @goal test for Command Pattern


class Order:
    def __init__(self):
        return

    def execute(self):
        return


class Stock:
    def __init__(self):
        self.name = 'ABC'
        self.quantity = 10

    def buy(self):
        print("Stock [ Name: " + self.name + ", Quantity: " + str(self.quantity) + " ] bought")

    def sell(self):
        print("Stock [ Name: " + self.name + ", Quantity: " + str(self.quantity) + " ] sold")


class BuyStock(Order):
    def __init__(self, abcStock):
        Order.__init__(self)
        self.abcStock = abcStock

    def execute(self):
        self.abcStock.buy()


class SellStock(Order):
    def __init__(self, abcStock):
        Order.__init__(self)
        self.abcStock = abcStock

    def execute(self):
        self.abcStock.sell()


class Broker:
    def __init__(self):
        self.orderList = []

    def takeOrder(self, order):
        self.orderList.append(order)

    def placeOrders(self):
        for order in self.orderList:
            order.execute()
        self.orderList = []


class CommandPatternDemo:
    def run(self):
        abcStock = Stock()
        buyStockOrder = BuyStock(abcStock)
        sellStockOrder = SellStock(abcStock)

        broker = Broker()
        broker.takeOrder(buyStockOrder)
        broker.takeOrder(sellStockOrder)

        broker.placeOrders()
C = CommandPatternDemo()
C.run()

