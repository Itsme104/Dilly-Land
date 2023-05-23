# Name: Ryan Stone
# Date: 5/19/2023
# Project: Final
# Grayson Beamesderfer

from time import sleep
from Player import Player
from Enemies import Enemies
from Weapons import Weapons
from Consumables import Consumables
import Dialogue as dg

def gameLoop():
  name = input("What Is Your Username? ")
  player = Player(name)
  print(f"Welcome To Dilly Land {player.getName()}.\n")
  dg.gameStart()
  while player.isAlive():
    print(f"Current Room: {player.map.currentRoom}\n")
    player.options()
  print('''██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚═╝
                                                             ''')
  yon = input("Would You Like To Try Again? ").lower()
  if len(yon) == 0:
    yon = ' '
  while yon[0] not in ['y', 'n']:
    yon = input("\nWould You Like To Try Again? (Yes or No) ").lower()
    if len(yon) == 0:
      yon = ' '
  if yon[0] == 'y':
    gameLoop()
    
    
if __name__ == '__main__':
  try:
    gameLoop()
  except:
    print("The Game Broke")
    sleep(86400)
