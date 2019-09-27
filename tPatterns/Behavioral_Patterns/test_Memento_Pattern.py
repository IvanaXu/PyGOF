# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-25 20:08:49
# @goal test for Memento Pattern


class Memento:
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state


class Originator:
    def __init__(self):
        self.state = ''

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def saveStateToMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.getState()
# O = Originator()
# O.setState('1')
# print O.getState()
# O.getStateFromMemento(O.saveStateToMemento())
# print O.getState()


class CareTaker:
    def __init__(self):
        self.memetoList = []

    def add(self, state):
        self.memetoList.append(state)

    def get(self, index):
        return self.memetoList[index]


class MementoPatternDemo:
    def run(self):
        originator = Originator()
        careTaker = CareTaker()

        originator.setState("State #1")
        # N o S a v e
        originator.setState("State #2")
        careTaker.add(originator.saveStateToMemento())
        originator.setState("State #3")
        careTaker.add(originator.saveStateToMemento())
        originator.setState("State #4")

        print("Current State: " + originator.getState())
        originator.getStateFromMemento(careTaker.get(0))
        print("First saved State: " + originator.getState())
        originator.getStateFromMemento(careTaker.get(1))
        print("Second saved State: " + originator.getState())
M = MementoPatternDemo()
M.run()

