import inventory as inv
import time

# levels.py
# Beckham Thompson

txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"
txtContinue = "PRESS ENTER TO CONTINUE"


class Direction:
    def __init__(self,dir:str,txt:str,level:str) -> None:
        self.dir = dir
        self.txt = txt
        self.level = level
    def show(self):
        print(self.txt)
        input("\n"+txtContinue)

class Level:
    def __init__(self,name:str) -> None:
        self.name = name
        self.dirs:list[object] = "this does nothing"
        self.txtLook:list[str] = ("this does nothing")
        self.item = inv.nothing
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
            if self.south.level == "self":
                return (self.name + ".menu()")
            else:
                return (self.south.level + ".menu()")     
        elif userInput == "n":
            self.north.show()
            if self.north.level == "self":
                return (self.name + ".menu()")
            else:
                return (self.north.level + ".menu()")
        elif userInput == "w":
            self.west.show()
            if self.west.level == "self":
                return (self.name + ".menu()")
            else:
                return (self.west.level + ".menu()")
        elif userInput == "e":
            self.east.show()
            if self.east.level == "self":
                return (self.name + ".menu()")
            else:
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
        for i in inv.inventory:
            print(i)
        input("\n"+txtContinue)    

class SubLevel:
    def __init__(self,type:str,startLev:str,endLev:str,yesTxt=None,optTxt=None) -> None:
        self.type = type
        self.startLev = startLev
        self.endLev = endLev
        self.yesTxt = yesTxt
        self.optTxt = optTxt

    def menu(self):
        if self.type == "option":
            userInput = input("\n\n"+self.optTxt+" (y/n)").lower()
            if userInput == "y":
                for i in self.yesTxt:
                    print(i)
                    time.sleep(1)
                input("\n"+txtContinue)
                return (self.endLev+".menu()")
            else:
                return (self.startLev+".menu()")
        elif self.type == "end":
            print(self.yesTxt)
            inv.Clear()
            return(self.startLev+".menu()")
        else: 
            return(self.startLev+".menu()")



###### End Levels ######

WinLevel = SubLevel("end",None,"Level0_0","Congrats you win!")

DeathLevel = SubLevel("end",None,"Level0_0","You Died")

txtRockHit = "Ouch, That Rock Hurt"

###### Start ######

# Create the Level with the level name

Level0_0 = Level("Level0_0")

# Create the Levels Direction in order North,South,West,East

Level0_0.dirs = (
    Direction("North",txtRockHit,"self"),
    Direction("South","Entering Cave..","Level0_1"),
    Direction("West","Ouch, Rock","self"),
    Direction("East","You follow a path east","Level1_0"))

# Create the Look txt for the level

Level0_0.txtLook = ("You find yourself in a breathtaking forest","There are cliffs raised beside you","There is  a path to the south and the the east","There is a treasure chest in the hollow of a tree")

# Create the Item for the level

Level0_0.item = inv.leatherCap

###### Cave ######

Level0_1 = Level("Level0_1") 

Level0_1.dirs = (
    Direction("North","Backing out of Cave","Level0_0"),
    Direction("South","If you Move Gru will eat you","Level0_1"),
    Direction("West","If you Move Gru will eat you","Level0_1"),
    Direction("East","If you Move Gru will eat you","Level0_1"))

Level0_1.txtLook = ("Its pitch black in this cave","You can see dalight far at the end of the cave","North is back the way you came, South is foward")

###### Foot Hills ######

Level1_0 = Level("Level1_0") 

Level1_0.dirs = (
    Direction("North",txtRockHit,"Level0_0"),
    Direction("South","You follow path south...","Level1_1"),
    Direction("West","You follow path west...","Level0_0"),
    Direction("East",("You kick off your shoes and start to swim to the setting sun...\nYou change your mind, return and put your shoes back on"),"self"))

Level1_0.txtLook = ("You are at the foot hils of a mountain range","North is a mountain","East is an ocean","There is a watch in the sand")

Level1_0.item = inv.watch

##### Canyon ######

Level1_1 = Level("Level1_1") 

Level1_1.dirs = (
    Direction("North","You follow a path north...","Level1_1"),
    Direction("South","You follow a path south...","Level1_2"),
    Direction("West",txtRockHit,"self"),
    Direction("East","","Level2_1"))

Level1_1.txtLook = ("")


###### Mysterious Portal ######

MysteriousPortal = SubLevel("option","Level1_2","Level0_0",("You go through the portal","As you exit the other side of the portal you find yourself where you started..."),"Would you like to go through the portal?")


###### Swamp ######

Level1_2 = Level("Level1_2")

Level1_2.dirs = (
    Direction("North","You follow path north...","Level1_1"),
    Direction("South","This seems to be the end of the world","self"),
    Direction("West","You walk into a cave...","Level0_1"),
    Direction("East","You aproach the mysterious portal","MysteriousPortal"))

Level1_2.txtLook = ("You are in a canyon in the ground","Abe Lincolns golden top hat","Paths to the north, south and east")

Level1_2.item = inv.topHat

###### Wasteland ######

Level2_1 = Level("Level2_1")

Level2_1.dirs = (
    Direction("North","You see a sea serpent in the water and decide it is best to stay on land","self"),
    Direction("South","You follow path south...","Level2_2"),
    Direction("West","You follow path west...","Level1_1"),
    Direction("East","You forgot your skis and cannot go that way","self"))

Level2_1.txtLook = ("Volcanic wasteland","A diamond in a pile of ash","Paths to west and south", "Ocean to the north")

Level2_1.item = inv.diamond

###### Grass Plain ######

Level2_2 = Level("Level2_2")

Level2_2.dirs = (
    Direction("North","You follow path north...","Level2_1"),
    Direction("South","You follow a path south...","WinLevel"),
    Direction("West","","Level0"),
    Direction("East","","Level0"))

Level2_2.txtLook = ("A grass plain","East: a huge chasm in the ground","West and north are the paths", "A pot of gold in the grass","A glowing exit to the south")

Level2_2.item = inv.potGold

###### Casmn ######

Casm = SubLevel("option","Level2_2","DeathLevel","You Died","Would You Like to Dive?")


print("\nLevels Loaded\n")