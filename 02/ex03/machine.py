from random import choice
from beverages import *

class EmptyCup(HotBeverage):
  def __init__(self):
    super().__init__("empty cup", 0.90, "An empty cup?! Gimme my money back!")

class BrokenMachineException(Exception):
  def __init__(self):
    super().__init__("This coffee machine has to be repaired.")

class CoffeeMachine:

  _drinks_served: int

  def __init__(self):
    self._drinks_served = 0

  def _is_broken(self):
    return self._drinks_served >= 10

  def repair(self):
    self._drinks_served = 0

  def serve(self, drink: HotBeverage):
    if self._is_broken():
      raise BrokenMachineException()
    self._drinks_served += 1
    return choice([drink, EmptyCup()])