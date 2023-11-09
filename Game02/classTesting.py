from typing import Any
import time
import os
import random
import inventory as inv

#VARIBLES

txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"
txtContinue = "PRESS ENTER TO CONTINUE"

class Direction:
    def __init__(self,dir,txt,level) -> None:
        self.dir = dir
        self.txt = txt
        self.level = level
    def show(self):
        print(self.txt)
        input("\nPress ENTER TO CONTINUE")

class Level:
    def __init__(self,name,dirs) -> None:
        self.name = name
        self.dirs = dirs
        self.txtLook = "this does nothing"
    def menu(self):
        options = ["move","take","look","exit"]
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
            return (self.lookMenu())
        elif userInput == "e":
            return exit()
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
        print(self.txtLook)
        input("\n"+txtContinue)
        self.menu()
        


def Main():

    #First make the level Directions in order of North,South,West,East


    Level0_1Dirs = (
        Direction("North","Ouch, Rock","Level0_1"),
        Direction("South","Entering Cave..","Level0_2"),
        Direction("West","Ouch, Rock","Level0_1"),
        Direction("East","You follow a path east","Level1_1"))
    
    #Then create the level with the level name and directions

    Level0_1 = Level("Level 0_1",Level0_1Dirs)

    Level0_1.txtLook = "A grass plain"

    Level0_2Dirs = (
        Direction("North","Backing out of Cave","Level0_1"),
        Direction("South","If you Move Gru will eat you","Level0_2"),
        Direction("West","If you Move Gru will eat you","Level0_2"),
        Direction("East","If you Move Gru will eat you","Level0_2"))
    
    Level0_2 = Level("Level 0_2",Level0_2Dirs)


    Level1_1Dirs = (
        Direction("North","Backing out of Cave","Level1"),
        Direction("South","If you Move Gru will eat you","Level2"),
        Direction("West","If you Move Gru will eat you","Level2"),
        Direction("East","If you Move Gru will eat you","Level2"))
    
    Level1_1 = Level("Level 1_1",Level1_1Dirs)
    # The Level Meny will Return a level to call as a string ie "level0_1.menu()"
    # Eval will turn the string into that line of code

    result = Level0_1.menu()
    while result != "exit":
        result = eval(result)
        


Main()
