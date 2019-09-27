# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-26 10:56:29
# @goal tPatterns for Template Pattern


class Game:
    def __init__(self):
        return

    def initialize(self):
        return

    def startPlay(self):
        return

    def endPlay(self):
        return

    def play(self):
        self.initialize()

        self.startPlay()

        self.endPlay()


class Cricket(Game):
    def __init__(self):
        Game.__init__(self)

    def initialize(self):
        print "Cricket Game Initialized! Start playing."

    def startPlay(self):
        print "Cricket Game Started. Enjoy the game!"

    def endPlay(self):
        print "Cricket Game Finished!"


class Football(Game):
    def __init__(self):
        Game.__init__(self)

    def initialize(self):
        print "Football Game Initialized! Start playing."

    def startPlay(self):
        print "Football Game Started. Enjoy the game!"

    def endPlay(self):
        print "Football Game Finished!"
# Cricket Football


class TemplatePatternDemo:
    def run(self):
        game = Cricket()
        game.play()
        print '\n'
        game = Football()
        game.play()
T = TemplatePatternDemo()
T.run()

