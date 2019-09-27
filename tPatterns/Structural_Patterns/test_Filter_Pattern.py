# -*- coding:utf-8 -*-
# @auth ivan 
# @time 2016-10-14 21:04:43
# @goal tPatterns Filter Pattern


class Person:
    def __init__(self, name, gender, maritalStatus):
        self.name, self.gender, self.maritalStatus = name, gender, maritalStatus
    
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getMaritalStatus(self):
        return self.maritalStatus


class Criteria:
    def __init__(self):
        return

    def meetCriteria(self, persons):
        return


class CriteriaMale(Criteria):
    def meetCriteria(self, persons):
        malePersons = []
        for person in persons:
            if person.getGender() == 'MALE':
                malePersons.append(person)
        return malePersons
# print CriteriaMale().meetCriteria([Person('MALE', 'MALE', 'MALE')])[0].getName()
# print Person('MALE', 'MALE', 'MALE').getGender()


class CriteriaFemale(Criteria):
    def meetCriteria(self, persons):
        malePersons = []
        for person in persons:
            if person.getGender() == 'FEMALE':
                malePersons.append(person)
        return malePersons


class CriteriaSingle(Criteria):
    def meetCriteria(self, persons):
        malePersons = []
        for person in persons:
            if person.getGender() == 'SINGLE':
                malePersons.append(person)
        return malePersons
# CriteriaMale CriteriaFemale CriteriaSingle


class AndCriteria(Criteria):
    def __init__(self, criteria, otherCriteria):
        Criteria.__init__(self)
        self.criteria, self.otherCriteria = criteria, otherCriteria
        self.firstCriteriaPersons = []

    def meetCriteria(self, persons):
        self.firstCriteriaPersons = self.criteria.meetCriteria(persons)
        return self.otherCriteria.meetCriteria(self.firstCriteriaPersons)


class OrCriteria(Criteria):
    def __init__(self, criteria, otherCriteria):
        Criteria.__init__(self)
        self.criteria, self.otherCriteria = criteria, otherCriteria
        self.firstCriteriaItems, self.otherCriteriaItems = [], []

    def meetCriteria(self, persons):
        self.firstCriteriaItems = self.criteria.meetCriteria(persons)
        self.otherCriteriaItems = self.otherCriteria.meetCriteria(persons)

        for person in self.otherCriteriaItems:
            if person not in self.firstCriteriaItems:
                self.firstCriteriaItems.append(person)
        return self.firstCriteriaItems
# AndCriteria OrCriteria


class CriteriaPatternDemo:
    def __init__(self):
        self.persons = []
        self.persons.append(Person("Robert", "MALE", "SINGLE"))
        self.persons.append(Person("John", "MALE", "MARRIED"))
        self.persons.append(Person("Laura", "FEMALE", "MARRIED"))
        self.persons.append(Person("Diana", "FEMALE", "SINGLE"))
        self.persons.append(Person("Mike", "MALE", "SINGLE"))
        self.persons.append(Person("Bobby", "MALE", "SINGLE"))

        self.male = CriteriaMale()
        self.female = CriteriaFemale()
        self.single = CriteriaSingle()
        self.singleMale = AndCriteria(self.single, self.male)
        self.singleOrFemale = OrCriteria(self.single, self.female)

        print("Males: ")
        self.printPersons(self.male.meetCriteria(self.persons))

        print("\nFemales: ")
        self.printPersons(self.female.meetCriteria(self.persons))
        
        print("\nSingle Males: ")
        self.printPersons(self.singleMale.meetCriteria(self.persons))
        
        print("\nSingle Or Females: ")
        self.printPersons(self.singleOrFemale.meetCriteria(self.persons))
        return

    def printPersons(self, persons):
        # print 'tPatterns'
        # print persons
        for person in persons:
            print("Person : [ Name : " + person.getName() + ", Gender : " + person.getGender() + ", Marital Status : " \
                  + person.getMaritalStatus() + " ]")
        return
CriteriaPatternDemo()

# CriteriaPatternDemo
# error

