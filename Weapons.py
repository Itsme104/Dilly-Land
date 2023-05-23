# Name: Ryan Stone
# Date: 5/19/2023
# Project: Weapons Classes

from random import randint

class Weapons():
  def __init__(self):
    self.name = None

  def __str__(self):
    return f"Weapon: {self.name}\n"

class Fist(Weapons):
  def __init__(self):
    self.name = 'Fist'

  def use(self):
    return randint(2,4)

class FarmingHoe(Weapons):
  def __init__(self):
    self.name = 'Farming Hoe'

  def use(self, luck):
    if luck > 75:
      if randint(1,3) == 1:
        return 10
    return randint(4,6)

class BrokenBottle(Weapons):
  def __init__(self):
    self.name = 'Broken Glass Bottle'

  def use(self, luck):
    if luck > 75:
      if randint(1,3) == 1:
        return 14
    if randint(1,10) == 1:
      return [randint(6,10), False]
    return [randint(6,10)]

class Shotgun(Weapons):
  def __init__(self):
    self.name = 'Jank Shotgun'

  def use(self, luck):
    if luck > 75:
      if randint(1,3) == 1:
        return 30
    return 25 - randint(0,10)

class Scythe(Weapons):
  def __init__(self):
    self.name = 'Forgotten Scythe'

  def use(self, luck):
    if luck > 75:
      if randint(1,3) == 1:
        return 25
    return randint(15,20)
