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
    def __init__(self,type:str,startLev:str,endLev:str,yesTxt=None,optTxt=None,noTxt=None,item=None) -> None:
        self.type = type
        self.startLev = startLev
        self.endLev = endLev
        self.yesTxt = yesTxt
        self.noTxt = noTxt
        self.optTxt = optTxt
        self.item = item

    def menu(self):
        if self.type == "option":
            return(self.optionMenu())
        elif self.type == "end":
            return(self.endMenu())
        elif self.type == "itemcheck":
            return(self.itemCheck())

    def optionMenu(self):
            userInput = input("\n\n"+self.optTxt+" (y/n)").lower()
            if userInput == "y":
                for i in self.yesTxt:
                    print(i)
                    time.sleep(1)
                input("\n"+txtContinue)
                return (self.endLev+".menu()")
            else:
                return (self.startLev+".menu()")    
    def endMenu(self):
        print(self.yesTxt)
        inv.Clear()
        return(self.endLev+".menu()")
    def itemCheck(self):
        if eval(f"inv.{self.item}.have") == True:
            print(f"{sectionDiv} \n {self.yesTxt}")
            input(f"\n{txtContinue}")
            return(self.endLev+".menu()")
        else:
            print(f"{sectionDiv} \n {self.noTxt}")
            input(f"\n{txtContinue}")
            return (self.startLev+".menu()")


###### Level Creations #######


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
    Direction("South","You desend deeper into the cave","Level0_2"),
    Direction("West",txtRockHit,"self"),
    Direction("East",txtRockHit,"self"))

Level0_1.txtLook = ("Its pitch black in this cave","You can see light far at the end of the cave","North is back the way you came, South is foward")

###### Cave2 ######

Level0_2 = Level("Level0_2") 

Level0_2.dirs = (
    Direction("North","Backing out of Cave","Level0_1"),
    Direction("South","You desend deeper into the cave","Level0_3"),
    Direction("West",txtRockHit,"self"),
    Direction("East",txtRockHit,"self"))

Level0_2.txtLook = ("Two torches light up this section of the cave dimly","North is back the way you came, South is foward")

Level0_2.item = inv.torch

###### Cave3 ######

Level0_3 = Level("Level0_3") 

Level0_3.dirs = (
    Direction("North","Backing out of Cave","Level0_2"),
    Direction("South",txtRockHit,"Level0_1"),
    Direction("West","You aproach the cave opening and...","CaveOpening"),
    Direction("East","If you Move Gru will eat you","Level0_1"))

Level0_3.txtLook = ("There is a small opening to the West","North is back the way you came, South is foward")

###### Cave Opening Item Check #######

CaveOpening = SubLevel("itemcheck",startLev="Level0_3",endLev="CaveRoom",item="torch",yesTxt="You enter the cave opening",noTxt="You got scared because its too dark")

###### Cave Room ######

CaveRoom = Level("CaveRoom") 

CaveRoom.dirs = (
    Direction("North",txtRockHit,"self"),
    Direction("South",txtRockHit,"self"),
    Direction("West",txtRockHit,"self"),
    Direction("East","You back out of the room","Level0_3"))

CaveRoom.txtLook = ("A small cave room with no lights other than your torch","There is a chest at the back of the room","East back through the small opening")

CaveRoom.item = inv.sword

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
    Direction("West","You follow a path west...","Level1_2"),
    Direction("East","You aproach the large Casmn","Casmn"))

Level2_2.txtLook = ("A grass plain","East: a huge chasm in the ground","West and north are the paths", "A pot of gold in the grass","A glowing exit to the south")

Level2_2.item = inv.potGold

###### Casmn ######

Casmn = SubLevel("option","Level2_2","DeathLevel","You Died","Would You Like to Dive?")

print("\nLevels Loaded\n")

result = Level0_3.menu()
while result != "exit":
    result = eval(result)    