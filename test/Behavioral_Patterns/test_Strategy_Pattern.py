# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-26 10:42:50
# @goal test for Strategy Pattern


class Strategy:
    def doOperation(self, num1, num2):
        return


class OperationAdd(Strategy):
    def doOperation(self, num1, num2):
        return num1 + num2


class OperationSubstract(Strategy):
    def doOperation(self, num1, num2):
        return num1 - num2


class OperationMultiply(Strategy):
    def doOperation(self, num1, num2):
        return num1 * num2


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def executeStrategy(self, num1, num2):
        return self.strategy.doOperation(num1, num2)


class StrategyPatternDemo:
    def run(self):
        context = Context(OperationAdd())
        print "10 + 5 = " + str(context.executeStrategy(10, 5))

        context = Context(OperationSubstract())
        print "10 - 5 = " + str(context.executeStrategy(10, 5))

        context = Context(OperationMultiply())
        print "10 * 5 = " + str(context.executeStrategy(10, 5))
S = StrategyPatternDemo()
S.run()
