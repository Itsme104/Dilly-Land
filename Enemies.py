# Name: Ryan Stone
# Date: 5/24/2023

from random import randint, triangular

class Enemies():
  def __init__(self):
    self.name = None
    self.hp = 0
    self.rarity = 0

  def __str__(self):
    return f"Enemy: {self.name}\n   Hp: {self.hp}\n \n**chaotic {self.name} noises**\n\n"

  def reward(self):
    if randint(1, 45) == 1 and self.rarity != 3:
      return "Jank Shotgun"
    if self.rarity == 0:
      return randint(1, 5)
    elif self.rarity == 1:
      return randint(3,7)
    elif self.rarity == 2:
      return randint(7,15)
    elif self.rarity == 3:
      if self.name == "Pickle Rick":
        return "Pickle Juice"
      elif self.name == "Commander Conway":
        return "Forgotten Scythe"
      else:
        return randint(15,25)

  # Health Point Modifiers
  def removeHealth(self, amount):
    self.hp -= amount

  def isAlive(self):
    if self.hp > 0:
      return True
    else:
      return False

  # Getters
  def getHp(self):
    return self.hp


class Fox(Enemies):
  def __init__(self):
    self.name = 'Fox'
    self.hp = 10
    self.rarity = 0

  def attack(self):
    return randint(1,5)


class Wolf(Enemies):
  def __init__(self):
    self.name = 'Wolf'
    self.hp = 15
    self.rarity = 1

  def attack(self):
    return randint(5,10)


class SkinWalker(Enemies):
  def __init__(self):
    self.name = 'Skinwalker'
    self.hp = 35
    self.rarity = 2

  def attack(self):
    return randint(10,15)


class Buck(Enemies):
  def __init__(self):
    self.name = '28 Point Buck'
    self.hp = 1
    self.rarity = 3

  def __str__(self):
    return f"Enemy: {self.name}\n   Hp: ???\n"

  def removeHealth(self, luck):
    if luck >= 95:
      if randint(1,10) == 1:
        self.hp -= 1
      else:
        print("\nYou Seem To Be Very Lucky...\nBut That Alone Is Not Enough.\n")
        return self.attack()
    else:
      print("\nThe Buck Seems Uneffected By Your Attack.\n")
      return self.attack()

  def attack(self):
    return 100


class Conway(Enemies):
  def __init__(self):
    self.name = 'Commander Conway'
    self.hp = 50
    self.rarity = 3

  def attack(self):
    return randint(15,25)


class Rick(Enemies):
  def __init__(self):
    self.name = 'Pickle Rick'
    self.hp = 100
    self.rarity = 3

  def attack(self):
    return int(triangular(20, 30, 25))
