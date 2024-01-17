#!/usr/bin/env python3

class HotBeverage:
    name = "hot beverage"
    price = 0.30
    _description = "Just some hot water in a cup."

    def description(self):
        return self._description

    def __str__(self):
        return f"name : {self.name}\nprice : {format(self.price, '.2f')}\ndescription : {self.description()}"


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    _description = "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"


class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    _description = "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    _description = "Un po’ di Italia nella sua tazza!"
