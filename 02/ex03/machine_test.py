from machine import *

def test():
  machine = CoffeeMachine()
  for i in range(11):
    try:
      print("---Serving hot beverage...---")
      print(machine.serve(Coffee()))
      print(f"served drink: {machine._drinks_served}")
      print("-----------------------------")
    except BrokenMachineException as e:
      print(e)
      print("Repairing machine...")
      machine.repair()
      print("Machine repaired!")
  print("-----------------------------")
  print("Test if machine is repaired...")
  try:
    print(machine.serve(Tea()))
  except BrokenMachineException as e:
    print(e)

if __name__ == "__main__":
  test()