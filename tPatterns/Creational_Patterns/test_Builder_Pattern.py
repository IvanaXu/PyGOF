# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 17:32:24
# @goal tPatterns Builder Pattern


class Item:
    def __init__(self):
        return

    def name(self):
        return

    def packing(self):
        return

    def price(self):
        return


class Packing:
    def pack(self):
        return


class Bottle(Packing):
    def pack(self):
        return 'Bottle'


class Wrapper(Packing):
    def pack(self):
        return 'Wrapper'
# (Packing)Bottle Wrapper


class Burger(Item):
    def packing(self):
        return Wrapper()

    def price(self):
        return


class ColdDrink(Item):
    def packing(self):
        return Bottle()

    def price(self):
        return
# (Item)Burger ColdDrink


class ChickenBurger(Burger):
    def price(self):
        return 50.5

    def name(self):
        return 'Chicken Burger'


class VegBurger(Burger):
    def price(self):
        return 25.0

    def name(self):
        return 'Veg Burger'

# (Burger)ChickenBurger VegBurger


class Coke(ColdDrink):
    def price(self):
        return 30.0

    def name(self):
        return 'Coke'


class Pepsi(ColdDrink):
    def price(self):
        return 35.0

    def name(self):
        return 'Pepsi'
# (ColdDrink)Coke Pepsi


class Meal:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getCost(self):
        cost = 0.0
        for item in self.items:
            cost += item.price()
        return cost

    def showItems(self):
        for item in self.items:
            print "Item : " + item.name()
            print ", Packing : " + item.packing().pack()
            print ", Price : " + str(item.price())


class MealBuilder:
    def prepareVegMeal(self):
        meal = Meal()
        meal.addItem(VegBurger())
        meal.addItem(Coke())
        return meal

    def prepareNonVegMeal(self):
        meal = Meal()
        meal.addItem(ChickenBurger())
        meal.addItem(Pepsi())
        return meal

    def prepareList(self):
        meal = Meal()
        meal_list = [Coke(), Coke(), ChickenBurger(), Pepsi()]
        for i in meal_list:
            meal.addItem(i)
        return meal


class BuilderPatternDemo:
    def __init__(self):
        mealBuilder = MealBuilder()

        vegMeal = mealBuilder.prepareVegMeal()
        print "Veg Meal"
        vegMeal.showItems()
        print "Total Cost: " + str(vegMeal.getCost())

        nonVegMeal = mealBuilder.prepareNonVegMeal()
        print "\n\nNon-Veg Meal"
        nonVegMeal.showItems()
        print "Total Cost: " + str(nonVegMeal.getCost())

        print "\n\n____#List#____"
        listMeal = mealBuilder.prepareList()
        print "List Meal"
        listMeal.showItems()
        print "Total Cost: " + str(listMeal.getCost())
BuilderPatternDemo()

