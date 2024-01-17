#!/usr/bin/env python3

class Intern:
  name: str = "My name? I’m nobody, an intern, I have no name."

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def work(self):
    raise Exception("I’m just an intern, I can’t do that...")

  def make_coffee(self):
    return Coffee()


class Coffee:
  def __str__(self):
    return "This is the worst coffee you ever tasted."



