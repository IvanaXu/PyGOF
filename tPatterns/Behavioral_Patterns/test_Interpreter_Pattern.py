# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-20 21:18:12
# @goal test for Interpreter Pattern


class Expression:
    def __init__(self):
        return

    def interpret(self, context):
        return


class TerminalExpression(Expression):
    def __init__(self, data):
        Expression.__init__(self)
        self.data = data

    def interpret(self, context):
        if self.data in context:
            return True
        return False
    # T = TerminalExpression('data')
    # print T.interpret('data error')


class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        Expression.__init__(self)
        self.expr1, self.expr2 = expr1, expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)


class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        Expression.__init__(self)
        self.expr1, self.expr2 = expr1, expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)


class InterpreterPatternDemo:
    def getMaleExpression(self):
        robert = TerminalExpression('Robert')
        john = TerminalExpression('John')
        return OrExpression(robert, john)

    def getMarriedWomanExpression(self):
        julie = TerminalExpression('Julie')
        married = TerminalExpression('Married')
        return AndExpression(julie, married)

    def run(self):
        isMale = self.getMaleExpression()
        isMarriedWoman = self.getMarriedWomanExpression()

        print('John is male? ')
        print(isMale.interpret('John'))
        # print self.getMaleExpression().interpret('John')
        print('Julie is a married women?')
        print(isMarriedWoman.interpret('Married Julie'))
        # print self.getMarriedWomanExpression().interpret('Married Julie')
        return


I = InterpreterPatternDemo()
I.run()



