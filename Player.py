# Name: Ryan Stone
# Date: 5/19/2023
# Project: Player Class

from random import randint, triangular
from Map import Map
from os import system
from time import sleep
from Weapons import *
from Consumables import *
from Enemies import *

class Player():
  def __init__(self, name=''):
    self.map = Map()
    self.inventory = {"Dilly Dollar":0}
    self.luck = randint(0, 100)
    self.hp = int(triangular(65,100,90))
    self.weapon = Fist()
    if name == '':
      name = 'Unknown'
    elif name == "Grayson Beamesderfer":
      self.addItem("Forgotten Scythe")
      for i in range(5):
        self.addItem("Bottle of Alcohol")
        self.addItem("Apple Juice")
      for i in range(10):
        self.addItem("Dilly Dollar")
    self.name = name

  def __str__(self):
    return f"Player Name: {self.name}\n\t Health: {self.hp}\n"

  # Options Section
  def options(self, choices=None):
    if choices != None and self.map.currentRoom in ["Farm House", "Dilly's Tavern"]:
      if "Corn" in self.getInventory():
        choices.append("Cook Corn")
    if choices == None:
      choices = ["Explore Area", "Move", "Check Inventory", "Use Consumable", "Select Weapon", "Check Hp"]
    for chioceNum in range(len(choices)):
      print(chioceNum+1, ":", choices[chioceNum])
    print()
    choice = -999
    while choice < 1 or choice > chioceNum+1:
      choice = input("What Do You Want To Do? ")
      try:
        choice = int(choice)
        if choice < 1 or choice > chioceNum+1:
          print("Number Must Align To An Action.\n")
      except:
        print("Must Be An Integer.\n")
        choice = -999
    choiceName = choices[choice-1]
    posDmg = self.open(choiceName)
    system('cls')
    return posDmg

  def open(self, option):
    if option == "Check Inventory":
      self.displayInventory()
    elif option == "Use Consumable":
      self.use()
    elif option == "Select Weapon":
      self.selectWeapon()
    elif option == "Move":
      self.move()
    elif option == "Check Hp":
      print("\nNote: Max Hp Is 100.")
      print(f"Current Hp: {self.getHp()}")
      sleep(3)
    elif option == "Explore Area":
      self.map.exploreRoom(self)
    elif option == "Fight":
      return self.attack()
    elif option == "Open Fridge":
      self.map.exploredFarm1 = True
      amount = randint(1,3)
      posFull = False
      for i in range(amount):
        if posFull != True:
          posFull = self.addItem("Apple Juice")
      if posFull == True:
        print()
      if amount > 1:
        print(f"You Found {amount} Bottles Of Apple Juice.")
      else:
        print(f"You Found {amount} Bottle Of Apple Juice.")
      sleep(3)
    elif option == "Look Around":
      print("\nYou Looked Around The House.")
      sleep(3)
      if randint(1,3) == 1:
        self.map.exploredFarm2 = True
        print("\nYou Found A Farming Hoe.")
        self.addItem("Farming Hoe")
        sleep(3)
    elif option == "Cook Corn":
      loop = True
      if self.map.currentRoom == "Farm House":
        while loop:
          self.removeItem("Corn")
          self.addItem("Cooked Corn")
          if "Corn" not in self.getInventory() or self.inventory["Cooked Corn"] == 5:
            loop = False
      elif self.map.currentRoom == "Dilly's Tavern":
        yon = input("\nWould You Like To Spend 5 Dilly Dollars To Cook A Peice Of Corn? ").lower()
        if len(yon) == 0:
          yon = ' '
        while yon[0] not in ['y', 'n']:
          yon = input("\nWould You Like To Spend 3 Dilly Dollars To Cook A Peice Of Corn? (Yes or No) ").lower()
          if len(yon) == 0:
            yon = ' '
        if yon[0] == 'y':
          if self.inventory["Dilly Dollar"] >= 3:
            for i in range(3):
              self.removeItem("Dilly Dollar")
            self.removeItem("Corn")
            self.addItem("Cooked Corn")
            print("\nYou Cooked One Peice Of Corn.")
          elif "Cooked Corn" in self.getInventory():
            if self.inventory["Cooked Corn"] == 5:
              print("\nYou Have The Max Amount Of Cooked Corn.")
          else:
            print("\nYou Do Not Have Enough Dilly Dollars.")
          sleep(3)
    elif option == "Drink":
      self.resetLuck()
      return True
    elif option == "Break Bottle":
      return False
    elif option == "Buy Alcohol":
      yon = input("\nWould You Like To Spend 5 Dilly Dollars To Buy A Bottle? ").lower()
      if len(yon) == 0:
        yon = ' '
      while yon[0] not in ['y', 'n']:
        yon = input("\nWould You Like To Spend 5 Dilly Dollars To Buy A Bottle? (Yes or No) ").lower()
        if len(yon) == 0:
          yon = ' '
      if yon[0] == 'y':
        if self.inventory["Dilly Dollar"] >= 5:
          for i in range(5):
            self.removeItem("Dilly Dollar")
          self.addItem("Bottle of Alcohol")
          print("\nYou Bought A Bottle Of Alcohol.")
        elif "Cooked Corn" in self.getInventory():
          if self.inventory["Bottle of Alcohol"] == 5:
            print("\nYou Have The Max Amount Of Alcohol.")
        else:
          print("\nYou Do Not Have Enough Dilly Dollars.")
        sleep(3)
          
  
  # Inventory
  def addItem(self, item):
    if item not in self.inventory.keys():
      self.inventory[item] = 1
    else:
      if self.inventory[item] + 1 > 5 and item != "Dilly Dollar":
        print("\nCannot Collect More Of This Item.")
        return True
      else:
        self.inventory[item] = self.inventory[item] + 1
        
  def removeItem(self, item):
      self.inventory[item] = self.inventory[item] - 1
      if self.inventory[item] == 0 and item != "Dilly Dollar":
        del self.inventory[item]
        
  def getInventory(self):
    return list(self.inventory.keys())
    
  def displayInventory(self):
    print("\nNote: You Cannot Have More Than 5 Of The Same Consumable.\n")
    print("Inventory:")
    for itemIndex in range(len(self.inventory.keys())):
      print(f"    {list(self.inventory.values())[itemIndex]} x {list(self.inventory.keys())[itemIndex]}")
    input("\nPress Enter To Continue.")
      
  # Health Point Modifiers
  def addHealth(self, amount):
    self.hp += amount
    if self.hp > 100:
      self.hp = 100
      
  def removeHealth(self, amount):
    if self.hp - amount < 0:
      self.hp = 0
    self.hp -= amount

  def isAlive(self):
    if self.hp > 0:
      return True
    else:
      return False

  # Consumable Section
  def use(self):
    consumables = ["Apple Juice", "Corn", "Cooked Corn", "Bottle of Alcohol", "Pickle Juice"]
    inv = self.getInventory()
    consumablesInv = []
    selection = None
    for item in inv:
      if item in consumables:
        consumablesInv.append(item)
    print()
    if len(consumablesInv) > 0:
      for consumableNum in range(len(consumablesInv)):
        print(consumableNum+1, ":", consumablesInv[consumableNum])
      print()
      consumable = -999
      while consumable < 1 or consumable > consumableNum+1:
        consumable = input("What Consumable Do You Want To Select? ")
        try:
          consumable = int(consumable)
          if consumable < 1 or consumable > consumableNum+1:
            print("Number Must Align To A Consumable.\n")
        except:
          print("Must Be An Integer.\n")
          consumable = -999
      consumableName = consumablesInv[consumable-1]
      self.removeItem(consumableName)
      if consumableName == "Apple Juice":
        health = AppleJuice().use()
      elif consumableName == "Corn":
        health = UncookedCorn().use()
      elif consumableName == "Cooked Corn":
        health = CookedCorn().use()
      elif consumableName == "Bottle of Alcohol":
        print()
        selection = self.options(["Drink", "Break Bottle"])
        if selection == True:
          health = Alcohol().use()
        else:
          self.addItem("Broken Glass Bottle")
          print("You Got One Broken Glass Bottle.")
      elif consumableName == "Pickle Juice":
        health = PickleJuice().use()
      if selection != False:
        print(f"\nYou Gained {health} Hp.")
        self.addHealth(health)
      sleep(3)
    else:
      print("You Do Not Have Any Consumables.\n")
      sleep(3)
    
  
  # Attack Section
  def attack(self):
    if isinstance(self.weapon, Fist):
      return Fist().use()
    elif isinstance(self.weapon, FarmingHoe):
      return FarmingHoe().use(self.getLuck())
    elif isinstance(self.weapon, BrokenBottle):
      posDamage = BrokenBottle().use(self.getLuck())
      if len(posDamage) == 2:
        print("\nYour Glass Bottle Shattered.")
        self.weapon = Fist()
        sleep(3)
      return posDamage[0]
    elif isinstance(self.weapon, Shotgun):
      return Shotgun().use(self.getLuck())
    elif isinstance(self.weapon, Scythe):
      return Scythe().use(self.getLuck())

  def fight(self, enemy):
    system("cls")
    print('''
███████╗██╗ ██████╗ ██╗  ██╗████████╗██╗
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝██║
█████╗  ██║██║  ███╗███████║   ██║   ██║
██╔══╝  ██║██║   ██║██╔══██║   ██║   ╚═╝
██║     ██║╚██████╔╝██║  ██║   ██║   ██╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝
                                        ''')
    sleep(3)
    system("cls")
    print(enemy)
    print(self)
    if isinstance(enemy, Buck) == False:
      firstAttack = randint(1, 2)
      if firstAttack == 1:
        damage = enemy.attack()
        print(f"You Took {damage} Damage.\n")
        self.removeHealth(damage)
        sleep(3)
        if self.isAlive() == False:
          return None
      system("cls")
      while enemy.isAlive():
        print(enemy)
        print(self)
        damage = self.options(["Fight", "Check Inventory", "Use Consumable", "Select Weapon"])
        if damage != None:
          print(enemy)
          print(self)
          print(f"You Did {damage} Damage To The {enemy.name}.\n")
          enemy.removeHealth(damage)
          if enemy.isAlive():
            damage = enemy.attack()
            print(f"You Took {damage} Damage.\n")
            self.removeHealth(damage)
            if self.isAlive() == False:
              return None
          sleep(3)
        system("cls")
    else:
      input("Press Enter To Try And Defeat The Buck.")
      posDmg = enemy.removeHealth(self.getLuck())
      sleep(3)
      if posDmg != None:
        self.removeHealth(posDmg)
        print("You Took I̸̛̜̲̥͈͍̿́̐̾n̸͎̞̼̼̮̓̅̍͋̚ʇ̵̪͓̥͇́̀͒͊͜͝i̸̢̩͎̲͍̍͊̈̽̚n̴̮̠̟̣͈͂̓̄̓͘i̷͕͙̜̜͙̅̍̈́̇̓Ɉ̴̢̬̮̥̥̊͋̓͋̇ǝ̶̖̹̖̺̝̒̑͊̈́̚   Damage.\n")
        sleep(3)
        return None
      self.map.buckDead = True
      print()
    print(f"You Beat The {enemy.name}!")
    reward = enemy.reward()
    if isinstance(reward, int):
      for i in range(reward):
        self.addItem("Dilly Dollar")
      print(f"You Found {reward} Dilly Dollars.")
    else:
      self.addItem(reward)
      print(f"You Found A {reward}!")
    sleep(3)
      
  # Select Weapon
  def selectWeapon(self):
    weapons = ["Fist", "Farming Hoe", "Broken Glass Bottle", "Jank Shotgun", "Forgotten Scythe"]
    inv = self.getInventory()
    weaponsInv = ["Fist"]
    for item in inv:
      if item in weapons:
        weaponsInv.append(item)
    print()
    for weaponNum in range(len(weaponsInv)):
      print(weaponNum+1, ":", weaponsInv[weaponNum])
    print()
    weapon = -999
    while weapon < 1 or weapon > weaponNum+1:
      weapon = input("What Weapon Do You Want To Select? ")
      try:
        weapon = int(weapon)
        if weapon < 1 or weapon > weaponNum+1:
          print("Number Must Align To A Weapon.\n")
      except:
        print("Must Be An Integer.\n")
        weapon = -999
    weaponName = weaponsInv[weapon-1]
    self.setWeapon(weaponName)

  # Move Section  
  def move(self):
    rooms = self.map.availableRooms()
    print()
    for roomNum in range(len(rooms)):
      print(roomNum+1, ":", rooms[roomNum])
    print("")
    room = -999
    while room < 1 or room > roomNum+1:
      room = input("Where Do You Want To Go? ")
      try:
        room = int(room)
        if room < 1 or room > roomNum+1:
          print("Number Must Align To A Room.\n")
      except:
        print("Must Be An Integer.\n")
        room = -999
    roomName = rooms[room-1]
    
    enemy = self.map.interaction(roomName)
    if enemy == "random":
      if randint(1,100) < 65:
        chance = randint(1, 100)
        if chance < 65:
          enemy = Fox()
        elif chance < 95:
          enemy = Wolf()
        else:
          enemy = SkinWalker()
      else:
        enemy = None
    if enemy != None:
      self.fight(enemy)
    self.map.setCurrentRoom(roomName)
  
  # Getters
  def getRoom(self):
    return self.room
  def getLuck(self):
    return self.luck
  def getHp(self):
    return self.hp
  def getName(self):
    return self.name
    
  # Setters
  def setRoom(self, room):
    self.room = room
  def resetLuck(self):
    self.luck = randint(0, 100)
  def setWeapon(self, weaponName):
    if weaponName == "Fist":
      self.weapon = Fist()
    elif weaponName == "Farming Hoe":
      self.weapon = FarmingHoe()
    elif weaponName == "Broken Glass Bottle":
      self.weapon = BrokenBottle()
    elif weaponName == "Jank Shotgun":
      self.weapon = Shotgun()
    elif weaponName == "Forgotten Scythe":
      self.weapon = Scythe()
