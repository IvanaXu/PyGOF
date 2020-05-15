# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-26 11:21:30
# @goal test for Visitor Pattern


class ComputerPart:
    def __init__(self):
        return

    def accept(self, computerPartVisitor):
        return


class Keyboard(ComputerPart):
    def __init__(self):
        ComputerPart.__init__(self)
        return

    def accept(self, computerPartVisitor):
        computerPartVisitor.visit(self)


class Monitor(ComputerPart):
    def __init__(self):
        ComputerPart.__init__(self)
        return

    def accept(self, computerPartVisitor):
        computerPartVisitor.visit(self)


class Mouse(ComputerPart):
    def __init__(self):
        ComputerPart.__init__(self)
        return

    def accept(self, computerPartVisitor):
        computerPartVisitor.visit(self)
# Keyboard Monitor Mouse


class Computer(ComputerPart):
    def __init__(self):
        ComputerPart.__init__(self)
        self.parts = [Keyboard(), Monitor(), Mouse()]
        return

    def accept(self, computerPartVisitor):
        for i in self.parts:
            i.accept(computerPartVisitor)
        computerPartVisitor.visit(self)


class ComputerPartVisitor:
    def __init__(self):
        return

    def visit(self, part):
        return


class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def __init__(self):
        ComputerPartVisitor.__init__(self)
        return

    def visit(self, part):
        # N O G O O D
        if str(part.__class__) == '__main__.Keyboard':
            print('Displaying Keyboard.')
        if str(part.__class__) == '__main__.Monitor':
            print('Displaying Monitor.')
        if str(part.__class__) == '__main__.Mouse':
            print('Displaying Mouse.')
        if str(part.__class__) == '__main__.Computer':
            print('Displaying Computer.')
# C = Mouse()
# D = ComputerPartDisplayVisitor()
# D.visit(C)


class VisitorPatternDemo:
    def run(self):
        self.computer = Computer()
        self.computer.accept(ComputerPartDisplayVisitor())


V = VisitorPatternDemo()
V.run()



