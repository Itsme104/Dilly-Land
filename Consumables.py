# Name: Ryan Stone
# Date: 5/19/2023
# Project: Consumables Classes

from random import randint
from time import sleep

class Consumables():
  def __init__(self):
    self.name = None

  def __str__(self):
    return f"Consumable: {self.name}\n"

class AppleJuice(Consumables):
  def __init__(self):
    self.name = 'Apple Juice'

  def use(self):
    return randint(10,15)

class UncookedCorn(Consumables):
  def __init__(self):
    self.name = 'Corn'

  def use(self):
    return randint(1,5)

class CookedCorn(Consumables):
  def __init__(self):
    self.name = 'Cooked Corn'

  def use(self):
    return randint(5,10)

class Alcohol(Consumables):
  def __init__(self):
    self.name = 'Bottle of Alchol'

  def use(self):
    return randint(-5,25)
    
class PickleJuice(Consumables):
  def __init__(self):
    self.name = 'Pickle Juice'

  def use(self):
    print("\nYour Thirst For Pickle Juice Has Been Fulfilled.")
    sleep(3)
    print("You May Finally Rest.\n")
    sleep(2)
    yon = input("Would You Like To Continue Playing In Freeplay? ").lower()
    if len(yon) == 0:
      yon = ' '
    while yon[0] not in ['y', 'n']:
      yon = input("\nWould You Like To Continue Playing In Freeplay? (Yes or No) ").lower()
      if len(yon) == 0:
        yon = ' '
    if yon[0] == 'n':
      print("\nGood Bye.")
      sleep(86400)
      exit()
    return 25
