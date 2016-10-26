# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-26 09:45:26
# @goal test for State Pattern


class State:
    def __init__(self):
        return

    def doAction(self, context):
        return


class StartState(State):
    def __init__(self):
        State.__init__(self)
        return

    def doAction(self, context):
        print 'Player is in start state'
        context.setState(self)

    def toString(self):
        return 'Start State'


class StopState(State):
    def __init__(self):
        State.__init__(self)
        return

    def doAction(self, context):
        print 'Player is in stop state'
        context.setState(self)

    def toString(self):
        return 'Stop State'


class Context:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state


class StatePatternDemo:
    def run(self):
        self.context = Context()

        self.startState = StartState()
        self.startState.doAction(self.context)

        print self.context.getState().toString()

        self.stopState = StopState()
        self.stopState.doAction(self.context)

        print self.context.getState().toString()
S = StatePatternDemo()
S.run()

