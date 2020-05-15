# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 12:00:26
# @goal test Chain of Responsibility Pattern


class AbstractLogger:
    def __init__(self):
        self.INFO, self.DEBUG, self.ERROR = 1, 2, 3
        self.level, self.nextLogger = None, None

    def setNextLogger(self, nextLogger):
        self.nextLogger = nextLogger
        return

    def logMessage(self, level, message):
        if self.level <= level:
            self.write(message)

        if self.nextLogger:
            self.nextLogger.logMessage(level, message)

    def write(self, message):
        return


class ErrorLogger(AbstractLogger):
    def __init__(self, level):
        AbstractLogger.__init__(self)
        self.level = level

    def write(self, message):
        print("Error Console::Logger: " + message)


class FileLogger(AbstractLogger):
    def __init__(self, level):
        AbstractLogger.__init__(self)
        self.level = level

    def write(self, message):
        print("File::Logger: " + message)


class ConsoleLogger(AbstractLogger):
    def __init__(self, level):
        AbstractLogger.__init__(self)
        self.level = level

    def write(self, message):
        print("Standard Console::Logger: " + message)


class ChainPatternDemo:
    def __init__(self):
        self.errorLogger = ErrorLogger(AbstractLogger().ERROR)
        self.fileLogger = FileLogger(AbstractLogger().DEBUG)
        self.consoleLogger = ConsoleLogger(AbstractLogger().INFO)

        self.loggerChain = self.getChainOfLoggers()
        return

    def getChainOfLoggers(self):
        self.errorLogger.setNextLogger(self.fileLogger)
        self.fileLogger.setNextLogger(self.consoleLogger)
        return self.errorLogger

    def func(self):
        self.loggerChain.logMessage(AbstractLogger().INFO, "This is an information.")
        self.loggerChain.logMessage(AbstractLogger().DEBUG, "This is an debug level information.")
        self.loggerChain.logMessage(AbstractLogger().ERROR, "This is an error information.")
        return


ChainPatternDemo().func()



