#!/usr/bin/env python3

from intern import Intern

intern1 = Intern()
intern2 = Intern("Mark")

print(intern1)
print(intern2)

coffee = intern2.make_coffee()
print(coffee)

try:
  intern1.work()
except Exception as e:
  print(e)