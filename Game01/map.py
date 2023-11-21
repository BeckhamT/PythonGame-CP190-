import time
import os
import random
import inventory as inv

#VARIBLES 
username = "Player"

#CONSTANTS
txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"

#Level MENU
def LevelMenu(Levelname):
    options = ["move","take","look","exit"]
    print(sectionDiv)
    print(Levelname)
    print ("\nOptions: \n")
    for n in options:
        print(n)
    return input("\nInput: ").lower()

#MENU FOR THE MOVE ACTION
def MoveMenu():
    userInput = ""
    print(sectionDiv)
    print("MOVING\n")
    print(txtDirection)
    userInput = input("\nInput direction: ").lower()
    if len(userInput) < 1:
        return "f"
    else:
        return userInput[0]

#MENU FOR THE TAKE ACTION returns either true or false, either they take the item or not
def TakeMenu(item):
    print(sectionDiv)
    print(item)
    userInput = input("\nWould you like to take this item? (y/n) ").lower()
    if userInput == "y":
        inv.items.append(item)
        return True
    else:
        return False

#MENU FOR THE LOOK ACTION
def LookMenu(text):
    for i in text:
        print(i)
        time.sleep(1)
    input("\nPRESS ENTER TO CONTINUE")


#FUNCTIONS FOR ROCK HITTING AND SWIMMING

def HitRock():
    print("Ouch, that rock hurt")
    input("\nPRESS ENTER TO CONTINUE")

def Swim():
    print("You kick off your shoes and start to swim to the setting sun...")
    time.sleep(1)
    print("You change your mind, return and put your shoes back on")
    input("\nPRESS ENTER TO CONTINUE")

#FUNCTIONS FOR LEVELS

def Level0_0():
    name = "Start"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        # moving north or west
        if move == "n" or move == "w":
            HitRock()
            Level0_0()
        # moving south to Level 0_1
        elif move =="s":
            print(sectionDiv)
            print("\nYou walk into a cave...")
            input("\nPRESS ENTER TO CONTINUE to continue")
            Level0_1()
        #moving east to Level 1_0
        elif move =="e":
            Level1_0()
        else:
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level0_0()
    elif action == "look":
        LookMenu(("You find yourself in a breathtaking forest","There are cliffs raised beside you","There is a path to the south and the the east","There is a treasure chest in the hollow of a tree"))
        Level0_0()
    elif action == "take":
        print(sectionDiv)
        if inv.leatherCap == True:
            print("The chest is empty")
            input("\nPRESS ENTER TO CONTINUE")
        else:
            print("\nYou open the chest in the tree to find a...")
            time.sleep(1)
            inv.leatherCap = TakeMenu("Leather Cap")
            input("\nPRESS ENTER TO CONTINUE")
        Level0_0()
    elif action == "exit":
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level0_0()
    else:
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level0_0()


def Level0_1():
    name = "Cave"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        if move == "n":
            print(sectionDiv)
            print("You back out of the cave...")
            input("\nPRESS ENTER TO CONTINUE")
            Level0_0()
        elif move == "s" or "e" or "w":
            print(sectionDiv)
            print("If you move a grue will eat you")
            input("\nPRESS ENTER TO CONTINUE")
            Level0_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level0_1()
    elif action == "look":
        print(sectionDiv)
        LookMenu(("Its pitch black in this cave","You can see dalight far at the end of the cave","North is back the way you came, South is foward"))
        Level0_1()
    elif action == "take":
        print("\nThat did nothing")
        input("\nPRESS ENTER TO CONTINUE")
        Level0_1()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level0_1()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level0_1()


def Level1_0():
    name = "Foot Hills"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        if move == "n":
            print(sectionDiv)
            HitRock()
            Level1_0()
        elif move == "s":
            print(sectionDiv)
            print("You follow path south...")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_1()
        elif move == "e":
            print(sectionDiv)
            Swim()
            Level1_0()
        elif move == "w":
            print(sectionDiv)
            print("You follow path west...")
            input("\nPRESS ENTER TO CONTINUE")
            Level0_0()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_0()
    elif action == "look":
        print(sectionDiv)
        looktxt = ("You are at the foot hils of a mountain range","North is a mountain","East is an ocean","There is a watch in the sand")
        LookMenu(looktxt)
        Level1_0()
    elif action == "take":
        print(sectionDiv)
        doesFall = random.randint(0,9)
        print("\nYou try go to reach for in the sand and...")
        time.sleep(1)
        if doesFall < 3:
            print(sectionDiv)
            print("YOU FALL IN AND DIE!")
            input("\nPRESS ENTER TO CONTINUE")
            exit()
        else: 
            if inv.watch == True:
                print("You already have this item")
                input("\nPRESS ENTER TO CONTINUE")
            else:
                print("You got the watch!")
                input("\nPRESS ENTER TO CONTINUE")
                inv.watch = TakeMenu("Watch")
            Level1_0()
            print(sectionDiv)

            Level1_0()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level1_0()
    else:
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level1_0()


def Level1_1():
    name = "Canyon"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        if move == "n":
            print(sectionDiv)
            print("You follow path north...")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_0()
        elif move == "s":
            print(sectionDiv)
            print("You follow path south...")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_2()
        elif move == "e":
            print(sectionDiv)
            print("You follow path east...")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_1()
        elif move == "w":
            print(sectionDiv)
            HitRock()
            Level1_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_1()
    elif action == "look":
        print(sectionDiv)
        LookMenu(("You are in a canyon in the ground","Abe Lincolns golden top hat","Paths to the north, south and east"))
        Level1_1()
    elif action == "take":
        if inv.topHat == True:
            print("You already have this item")
            input("\nPRESS ENTER TO CONTINUE")
        else:
            print("You got the watch!")
            input("\nPRESS ENTER TO CONTINUE")
            inv.topHat = TakeMenu("Golden Top Hat")
        Level1_1()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level1_1()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level1_1()


def Level1_2():
    name = "Swamp"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        if move == "n":
            print(sectionDiv)
            print("You follow path north...")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_1()
        elif move == "s":
            print(sectionDiv)
            print("This seems to be the end of the world. You cannot go that way.")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_2()
        elif move == "e":
            print(sectionDiv)
            print("You aproach the mysterious portal")
            userInput = input("Would you like to enter (y/n)")
            if userInput == "y":
                Level0_0()
            else:
                Level1_2()
        elif move == "w":
            print(sectionDiv)
            print("You walk into a cave...")
            input("\nPRESS ENTER TO CONTINUE")
            Level0_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_2()
    elif action == "look":
        print(sectionDiv)
        LookMenu(("You are in a swamp","There is a jeweled skull in the muck","There is a mysterious portal to the east. ", "Paths to the north and west"))
        Level1_2()
    elif action == "take":
        print(sectionDiv)
        inv.skull = TakeMenu("Jeweled Skull")
        Level1_2()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level1_2()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level1_2()


def Level2_1():
    name = "Wasteland"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        if move == "n":
            print(sectionDiv)
            print("You see a sea serpent in the water and decide it is best to stay on land")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_1()
        elif move == "s":
            print(sectionDiv)
            print("You follow path south...")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_2()
        elif move == "e":
            print(sectionDiv)
            print("You forgot your skis and cannot go that way")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_1()
        elif move == "w":
            print(sectionDiv)
            print("You follow path west...")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_1()
    elif action == "look":
        print(sectionDiv)
        LookMenu(("Volcanic wasteland","A diamond in a pile of ash","Paths to west and south", "Ocean to the north"))
        Level2_1()
    elif action == "take":
        print(sectionDiv)
        inv.diamond = TakeMenu("A diamond")
        Level2_1()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level2_1()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level2_1()


def Level2_2():
    name = "Grass Plain"
    action = LevelMenu(name)
    if action == "move":
        move = MoveMenu()
        if move == "n":
            print(sectionDiv)
            print("You follow path north...")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_1()
        elif move == "s":
            print(sectionDiv)
            print(f"YOU ESCAPED!!!!\nCongrats!: {username}\nItems:")
            for i in inv.items:
                print(i)
            input("\nPRESS ENTER TO QUIT")
            exit()
        elif move == "w":
            print(sectionDiv)
            print("You follow path west...")
            input("\nPRESS ENTER TO CONTINUE")
            Level1_2()
        elif move == "e":
            print(sectionDiv)
            print("You aproach the huge casmn in the ground")
            userInput = input("Would you like to dive? (y/n)")
            if userInput == "y":
                print("Display You make a spectacular swan dive and vanish into a void, never to be seen again. Game over")
                exit()
            else:
                Level2_2()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Level2_2()
    elif action == "look":
        print(sectionDiv)
        LookMenu(("A grass plain","East: a huge chasm in the ground","West and north are the paths", "A pot of gold in the grass","A glowing exit to the south"))
        Level2_2()
    elif action == "take":
        inv.potOfGold = TakeMenu("Pot of Gold")
        Level2_2()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Level2_2()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Level2_2()
