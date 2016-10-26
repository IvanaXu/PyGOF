# -*-coding:utf-8-*-
# @auth ivan 
# @time 2016-10-26 19:01:45
# @goal test for Business Delegate Pattern


class BusinessService:
    def __init__(self):
        return

    def doProcessing(self):
        return


class EJBService(BusinessService):
    def __init__(self):
        BusinessService.__init__(self)
        return

    def doProcessing(self):
        print "Processing task by invoking EJB Service"


class JMSService(BusinessService):
    def __init__(self):
        BusinessService.__init__(self)
        return

    def doProcessing(self):
        print "Processing task by invoking JMS Service"


class BusinessLookUp:
    def getBusinessService(self, serviceType):
        if serviceType.upper() == 'EJB':
            return EJBService()
        else:
            return JMSService()


class BusinessDelegate:
    def __init__(self):
        self.lookupService = BusinessLookUp()
        self.businessService = None
        self.serviceType = ''

    def setServiceType(self, serviceType):
        self.serviceType = serviceType

    def doTask(self):
        self.businessService = self.lookupService.getBusinessService(self.serviceType)
        self.businessService.doProcessing()


class Client:
    def __init__(self, businessService):
        self.businessService = businessService

    def doTask(self):
        self.businessService.doTask()


class BusinessDelegatePatternDemo:
    def __init__(self):
        self.businessDelegate = None

    def run(self):
        self.businessDelegate = BusinessDelegate()
        client = Client(self.businessDelegate)

        self.businessDelegate.setServiceType("EJB")
        client.doTask()

        self.businessDelegate.setServiceType("JMS")
        client.doTask()
B = BusinessDelegatePatternDemo()
B.run()

