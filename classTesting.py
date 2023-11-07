from typing import Any
import time
import os
import random
import inventory as inv

txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"

class Direction:
    def __init__(self,dir,txt,level) -> None:
        self.dir = dir
        self.txt = txt
        self.level = level
    def show(self):
        print(self.txt)
        input("")

class Level:
    def __init__(self,name,dirs) -> None:
        self.name = name
        self.dirs = dirs
    def menu(self):
        options = ["move","take","look","exit"]
        print(sectionDiv)
        print(self.name)
        print ("\nOptions: \n")
        for n in options:
            print(n)
        userInput = input("\nInput: ").lower()
        if userInput == "move":
            self.moveMenu()
    def moveMenu(self):
        self.north = Direction("North","go",self.menu())
        self.south = ""
        self.west = ""
        self.east = ""
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
            self.south
        elif userInput == "n":
            self.north.show()
        elif userInput == "e":
            self.east
        elif userInput == "w":
            self.west



def LevelLoader():
    pass

def MenuMaker():
    pass

def Main():
    Level1 = Level("Level 1")
    Level1Dirs = Direction("North","Ouch, Rock","self")
    
    Level1.menu()

Main()
