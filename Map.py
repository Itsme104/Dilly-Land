# Name: Ryan Stone
# Date: 5/19/2023
# Project: Map Class

from Enemies import *
import Dialogue as dg
from time import sleep

class Map():
  def __init__(self):
    self.currentRoom = "Farm House"
    self.dirtRoadCount = 0
    self.cornPathCount = 0
    self.highwayCount = 0
    self.buckDead = False
    self.explored = False
    self.exploredFarm1 = False
    self.exploredFarm2 = False
    

  def __str__(self):
    return f"Current Room: {self.currentRoom}"

  def availableRooms(self):
    if self.currentRoom == "Farm House":
      return ["Dirt Road"]
    elif self.currentRoom == "Dilly's Tavern":
      return ["Dirt Road"]
    elif self.currentRoom == "Big Corn Field":
      return ["Corn Field Path"]
    elif self.currentRoom == "Cave Of Pickles":
      return ["Highway", "Farm House"]
    elif self.currentRoom == "Corn Field Path":
      if self.cornPathCount > 4:
        self.cornPathCount == 0
        return ["Dirt Road", "Big Corn Field", "Highway"]
      else:
        return ["Corn Field Path"]
    elif self.currentRoom == "Dirt Road":
      if self.dirtRoadCount > 3:
        self.dirtRoadCount == 0
        return ["Farm House", "Dilly's Tavern", "Corn Field Path"]
      else:
        return ["Dirt Road"]
    elif self.currentRoom == "Highway":
      if self.highwayCount > 2:
        self.highwayCount == 0
        return ["Corn Field Path", "Cave Of Pickles"]
      else:
        return ["Highway"]

  def interaction(self, next):
    location = "Area"
    if self.currentRoom == "Dirt Road" and self.dirtRoadCount < 4:
      location = "Part Of The Dirt Road"
    elif self.currentRoom == "Corn Field Path" and self.cornPathCount < 5:
      location = "Part Of The Corn Field Path"
    elif self.currentRoom == "Highway" and self.highwayCount < 3:
      location = "Part Of The Highway"
    print(f"\nYou Move To The Next {location}.\n")
    self.explored = False
    sleep(2)
    if next == "Farm House":
      if self.currentRoom == "Dirt Road" and self.buckDead == False:
        dg.buck()
        return Buck()
    elif next == "Big Corn Field":
      dg.conway()
      return Conway()
    elif next == "Cave Of Pickles":
      dg.rick()
      return Rick()
    elif next == "Dirt Road":
      self.dirtRoadCount += 1
    elif next == "Corn Field Path":
      self.cornPathCount += 1
    elif next == "Highway":
      self.highwayCount += 1
    return "random"
      

  def exploreRoom(self, player):
    print(f"\nYou Explore The {self.currentRoom}.\n")
    if self.currentRoom != "Farm House":
      sleep(3)
    if self.currentRoom == "Farm House":
      if self.exploredFarm1 == False and self.exploredFarm2 == False:
        player.options(["Open Fridge", "Look Around"])
      elif self.exploredFarm1 == False:
        player.options(["Open Fridge"])
      elif self.exploredFarm2 == False:
        player.options(["Look Around"])
      else:
        print("You Did Not Find Anything.")
    elif self.currentRoom == "Dilly's Tavern":
      player.options(["Buy Alcohol"])
    elif self.currentRoom == "Big Corn Field":
      player.addItem("Corn")
      print("You Found A Corn Husk.")
    elif self.currentRoom == "Cave Of Pickles":
      player.addItem("Pickle Juice")
    elif self.currentRoom == "Dirt Road":
      if randint(1,5) == 1 and self.explored == False:
        player.addItem("Dilly Dollar")
        print("You Found One Dilly Dollar.")
        self.explored = True
      else:
        print("You Did Not Find Anything.")
    elif self.currentRoom == "Corn Field Path":
      if randint(1,2) == 1:
        player.addItem("Corn")
        print("You Found A Corn Husk.")
      else:
        print("You Did Not Find Anything.")
    if self.currentRoom not in ["Farm House", "Dilly's Tavern"]:
      sleep(3)
      
  
  def setCurrentRoom(self, room):
    self.currentRoom = room
