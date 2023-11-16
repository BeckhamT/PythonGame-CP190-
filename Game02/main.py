from typing import Any
import time
import os
import random
import inventory as i

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



class Level:
    def __init__(self,name) -> None:
        self.name = name
        self.dirs = "this does nothing"
        self.txtLook = "this does nothing"
        self.item = i.nothing
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

    Level0_1 = Level("Level0_1")

    # Create the Levels Direction in order North,South,West,East

    Level0_1.dirs = (
        Direction("North","Ouch, Rock","Level0_1"),
        Direction("South","Entering Cave..","Level0_2"),
        Direction("West","Ouch, Rock","Level0_1"),
        Direction("East","You follow a path east","Level1_1"))

    # Create the Look txt for the level

    Level0_1.txtLook = ("You find yourself in a breathtaking forest","There are cliffs raised beside you","There is  a path to the south and the the east","There is a treasure chest in the hollow of a tree")

    # Create the Item for the level

    Level0_1.item = i.Item("Leather Cap","You open the chest in the tree and...")


    Level0_2 = Level("Level0_2")

    Level0_2.dirs = (
        Direction("North","Backing out of Cave","Level0_1"),
        Direction("South","If you Move Gru will eat you","Level0_2"),
        Direction("West","If you Move Gru will eat you","Level0_2"),
        Direction("East","If you Move Gru will eat you","Level0_2"))
    
    Level0_2.txtLook = ("Its pitch black in this cave","You can see dalight far at the end of the cave","North is back the way you came, South is foward")


    Level1_1 = Level("Level1_1")

    Level1_1.dirs = (
        Direction("North","Backing out of Cave","Level1"),
        Direction("South","If you Move Gru will eat you","Level2"),
        Direction("West","If you Move Gru will eat you","Level2"),
        Direction("East","If you Move Gru will eat you","Level2"))
    
    Level1_1.txtLook = ("")

    # The Level Meny will Return a level to call as a string ie "level0_1.menu()"
    # Eval will turn the string into that line of code
    # Every time the levels menu gets called it is called here

    result = Level0_1.menu()
    while result != "exit":
        result = eval(result)
        

Main()
