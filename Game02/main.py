from typing import Any
import time
import os
import random

#VARIBLES

txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"
txtContinue = "PRESS ENTER TO CONTINUE"

inv = []


class Direction:
    def __init__(self,dir,txt,level) -> None:
        self.dir = dir
        self.txt = txt
        self.level = level
    def show(self):
        print(self.txt)
        input("\n"+txtContinue)

class Item:
    def __init__(self,name,txt) -> None:
        self.name = name
        self.txt = txt
        self.have = False
    def menu(self):
        if self.name != "nothing":
            print(sectionDiv+"\n"+self.txt+"\n")
            print("You found a "+ self.name)
            if self.have == False:
                answer = input("\nWould you like to take? (y/n) ").lower()
                if answer == "y": 
                    self.have = True
                    inv.append(self.name)
            else:
                print("You already have this item")
                input(txtContinue)
        else:
            print("\nThere is nothing to take\n")
            input(txtContinue)

class Level:
    def __init__(self,name) -> None:
        self.name = name
        self.dirs = "this does nothing"
        self.txtLook = "this does nothing"
        self.item = Item("nothing","nothing")
    def menu(self):
        options = ["move","take","look","inventory","exit"]
        print(sectionDiv)
        print(self.name)
        print ("\nOptions: \n")
        for n in options:
            print(n)
        userInput = input("\nInput: ").lower()
        if userInput == "":
            userInput = "f"
        else:
            userInput = userInput[0]
        if userInput == "m":
            return (self.moveMenu())
        elif userInput == "l":
            self.lookMenu()
            return(self.name +".menu()")
        elif userInput == "t":
            self.takeMenu()
            return(self.name +".menu()")
        elif userInput == "i":
            self.invMenu()
            return(self.name +".menu()")
        elif userInput == "e":
            if input("Would you like to exit? (y/n) ").lower() == "y":
                return exit()
            else:
                return(self.name +".menu()")
        else:
            print(sectionDiv)
            input("Invalid Input\nPRESS ENTER TO CONTINUE")
            self.menu()
    def moveMenu(self):
        self.north = self.dirs[0]
        self.south = self.dirs[1]
        self.west = self.dirs[2]
        self.east = self.dirs[3]
        self.directions = (self.north,self.south,self.west,self.east)
        print(sectionDiv)
        print("MOVING\n")
        print(txtDirection)
        userInput = input("\nInput direction: ").lower()
        if len(userInput) < 1:
            userInput = "f"
        else:
            userInput = userInput[0]
        if userInput == "s":
            self.south.show()
            return (self.south.level + ".menu()")
        elif userInput == "n":
            self.north.show()
            return (self.north.level + ".menu()")
        elif userInput == "w":
            self.west.show()
            return (self.west.level + ".menu()")
        elif userInput == "e":
            self.east.show()
            return (self.east.level + ".menu()")
        else:
            print(sectionDiv)
            input("Invalid Input\nPRESS ENTER TO CONTINUE")
            self.moveMenu()
    def lookMenu(self):
        for i in self.txtLook:
            print(i)
            time.sleep(1)
        input("\n"+txtContinue)
        self.menu()
    def takeMenu(self):
        self.item.menu()
    def invMenu(self):
        print("\nInventory:\n")
        for i in inv:
            print(i)
        input("\n"+txtContinue)

        

def Main():

    # Create the Level with the level name


    Level0_0 = Level("Level0_0")   #Starting Level

    # Create the Levels Direction in order North,South,West,East

    Level0_0.dirs = (
        Direction("North","Ouch, Rock","Level0_0"),
        Direction("South","Entering Cave..","Level0_1"),
        Direction("West","Ouch, Rock","Level0_0"),
        Direction("East","You follow a path east","Level1_0"))

    # Create the Look txt for the level

    Level0_0.txtLook = ("You find yourself in a breathtaking forest","There are cliffs raised beside you","There is  a path to the south and the the east","There is a treasure chest in the hollow of a tree")

    # Create the Item for the level

    Level0_0.item = Item("Leather Cap","You open the chest in the tree and...")


    Level0_1 = Level("Level0_1") #Cave

    Level0_1.dirs = (
        Direction("North","Backing out of Cave","Level0_0"),
        Direction("South","If you Move Gru will eat you","Level0_1"),
        Direction("West","If you Move Gru will eat you","Level0_1"),
        Direction("East","If you Move Gru will eat you","Level0_1"))
    
    Level0_1.txtLook = ("Its pitch black in this cave","You can see dalight far at the end of the cave","North is back the way you came, South is foward")

    Level1_0 = Level("Level1_0") #Foot Hills

    Level1_0.dirs = (
        Direction("North","Ouch, That Rock Hurt","Level1_0"),
        Direction("South","You follow a path south","Level1_2"),
        Direction("West","You follow a path west","Level0_0"),
        Direction("East","You kick off your shoes and start to swim to the setting sun...\nYou change your mind, return and put your shoes back on","Level1_0"))
    
    Level1_0.txtLook = ("You are at the foot hils of a mountain range","North is a mountain","East is an ocean","There is a watch in the sand")

    Level1_0.item = Item("Watch","You reach into the sand")


    Level1_1 = Level("Level1_1") #Canyon

    Level1_1.dirs = (
        Direction("North","Ouch, That Rock Hurt","Level1_0"),
        Direction("South","You follow a path south","Level1_2"),
        Direction("West","You follow a path west","Level0_0"),
        Direction("East","You kick off your shoes and start to swim to the setting sun...\nYou change your mind, return and put your shoes back on","Level1_0"))
    
    Level1_1.txtLook = ("You are at the foot hils of a mountain range","North is a mountain","East is an ocean","There is a watch in the sand")

    Level1_1.item = Item("Top Hat","You reach into the sand")    

    # The Level Meny will Return a level to call as a string ie "Level0_0.menu()"
    # Eval will turn the string into that line of code
    # Every time the levels menu gets called it is called here

    result = Level0_0.menu()
    while result != "exit":
        result = eval(result)
        

Main()
