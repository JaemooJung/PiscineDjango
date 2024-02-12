#!/usr/bin/env python3

class HotBeverage:
    name: str
    price: float
    _description: str

    def __init__(self, name="hot beverage", 
                 price=0.30, 
                 description="Just some hot water in a cup."):
        self.name = name
        self.price = price
        self._description = description

    def description(self):
        return self._description

    def __str__(self):
        return f"name : {self.name}\nprice : {format(self.price, '.2f')}\ndescription : {self.description()}"


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__("coffee", 0.40, "A coffee, to stay awake.")


class Tea(HotBeverage):
    def __init__(self):
        super().__init__("tea")


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__("chocolate", 0.50, "Chocolate, sweet chocolate...")


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__("cappuccino", 0.45, "Un po’ di Italia nella sua tazza!")

if __name__ == '__main__':
  hot_beverage = HotBeverage()
  coffee = Coffee()
  tea = Tea()
  chocolate = Chocolate()
  cappuccino = Cappuccino()

  print("--HotBeverage--")
  print(hot_beverage)
  print("--Coffee--")
  print(coffee)
  print("--Tea--")
  print(tea)
  print("--Chocolate--")
  print(chocolate)
  print("--Cappuccino--")
  print(cappuccino)
