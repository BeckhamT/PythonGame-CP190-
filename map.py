import time
import os
import random
import inventory as inv

txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"
username = "Player"



def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#ROOM MENU
def roomMenu(roomname):
    options = ["move","take","look","exit"]
    print(sectionDiv)
    print(roomname)
    print ("\nOptions: \n")
    for n in options:
        print(n)
    return input("\nInput: ").lower()

#MENU FOR THE MOVE ACTION
def moveMenu():
    userInput = ""
    print(sectionDiv)
    print("MOVING\n")
    print(txtDirection)
    userInput = input("\nInput direction: ").lower()
    if len(userInput) < 1:
        return "f"
    else:
        return userInput[0]

#MENU FOR THE TAKE ACTION
def takeMenu(item):
    print(sectionDiv)
    print(item)
    userInput = input("\nWould you like to take this item? (y/n) ").lower()
    if userInput == "y":
        inv.items.append(item)
        return True
    else:
        return False

def lookMenu(text):
    for i in text:
        print(i)
        time.sleep(1)
    input("\nPRESS ENTER TO CONTINUE")


#MENU TO EXIT
def exitMenu():
    pass


def HitRock():
    print("Ouch, that rock hurt")
    input("\nPRESS ENTER TO CONTINUE")

def Swim():
    print("You kick off your shoes and start to swim to the setting sun...")
    time.sleep(1)
    print("You change your mind, return and put your shoes back on")
    input("\nPRESS ENTER TO CONTINUE")

#################################################

def Room0_0():
    name = "Room0_0"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        # moving north or west
        if move == "n" or move == "w":
            HitRock()
            Room0_0()
        # moving south to room 0_1
        elif move =="s":
            print(sectionDiv)
            print("\nYou walk into a cave...")
            input("\nPRESS ENTER TO CONTINUE to continue")
            Room0_1()
        #moving east to room 1_0
        elif move =="e":
            Room1_0()
        else:
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_0()
    elif action == "look":
        lookMenu(("You find yourself in a breathtaking forest","There are cliffs raised beside you","There is  a path to the south and the the east","There is a treasure chest in the hollow of a tree"))
        Room0_0()
    elif action == "take":
        print(sectionDiv)
        if inv.leatherCap == True:
            print("You already have this item")
            input("\nPRESS ENTER TO CONTINUE")
        else:
            print("\nYou open the chest in the tree to find a...")
            time.sleep(1)
            inv.leatherCap = takeMenu("Leather Cap")
            input("\nPRESS ENTER TO CONTINUE")
        Room0_0()
    elif action == "exit":
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room0_0()
    else:
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room0_0()

#################################################

def Room0_1():
    name = "Room0_1"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        if move == "n":
            print(sectionDiv)
            print("You back out of the cave...")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_0()
        elif move == "s" or "e" or "w":
            print(sectionDiv)
            print("If you move a grue will eat you")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_1()
    elif action == "look":
        print(sectionDiv)
        lookMenu(("Its pitch black in this cave","You can see dalight far at the end of the cave","North is back the way you came, South is foward"))
        Room0_1()
    elif action == "take":
        print("\nThat did nothing")
        input("\nPRESS ENTER TO CONTINUE")
        Room0_1()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room0_1()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room0_1()

#################################################

def Room1_0():
    name = "Room1_0"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        if move == "n":
            print(sectionDiv)
            HitRock()
            Room1_0()
        elif move == "s":
            print(sectionDiv)
            print("You follow path south...")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_1()
        elif move == "e":
            print(sectionDiv)
            Swim()
            Room1_0()
        elif move == "w":
            print(sectionDiv)
            print("You follow path west...")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_0()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_0()
    elif action == "look":
        print(sectionDiv)
        lookMenu(("You are at the foot hils of a mountain range","North is a mountain","East is an ocean","There is a watch in the sand"))
        Room1_0()
    elif action == "take":
        print(sectionDiv)
        doesFall = random.randint(0,9)
        print("\nYou try go to reach for the watch in the sand and...")
        time.sleep(1)
        if doesFall < 3:
            print(sectionDiv)
            print("YOU FALL IN AND DIE!")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_0()
        else: 
            if inv.watch == True:
                print("You already have this item")
                input("\nPRESS ENTER TO CONTINUE")
            else:
                print("You got the watch!")
                input("\nPRESS ENTER TO CONTINUE")
                inv.watch = takeMenu("Watch")
            Room1_0()
            print(sectionDiv)

            Room1_0()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room1_0()
    else:
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room1_0()

#################################################

def Room1_1():
    name = "Room1_1"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        if move == "n":
            print(sectionDiv)
            print("You follow path north...")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_0()
        elif move == "s":
            print(sectionDiv)
            print("You follow path south...")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_2()
        elif move == "e":
            print(sectionDiv)
            print("You follow path east...")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_1()
        elif move == "w":
            print(sectionDiv)
            HitRock()
            Room1_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_1()
    elif action == "look":
        print(sectionDiv)
        lookMenu(("You are in a canyon in the ground","Abe Lincolns golden top hat","Paths to the north, south and east"))
        Room1_1()
    elif action == "take":
        if inv.topHat == True:
            print("You already have this item")
            input("\nPRESS ENTER TO CONTINUE")
        else:
            print("You got the watch!")
            input("\nPRESS ENTER TO CONTINUE")
            inv.topHat = takeMenu("Watch")
        Room1_1()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room1_1()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room1_1()

#################################################

def Room1_2():
    name = "Room1_2"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        if move == "n":
            print(sectionDiv)
            print("You follow path north...")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_1()
        elif move == "s":
            print(sectionDiv)
            print("This seems to be the end of the world. You cannot go that way.")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_2()
        elif move == "e":
            print(sectionDiv)
            print("You aproach the mysterious portal")
            userInput = input("Would you like to enter (y/n)")
            if userInput == "y":
                Room0_0()
            else:
                Room1_2()
        elif move == "w":
            print(sectionDiv)
            print("You walk into a cave...")
            input("\nPRESS ENTER TO CONTINUE")
            Room0_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_2()
    elif action == "look":
        print(sectionDiv)
        lookMenu(("You are in a swamp","There is a jeweled skull in the muck","There is a mysterious portal to the east. ", "Paths to the north and west"))
        Room1_2()
    elif action == "take":
        print(sectionDiv)
        inv.leatherCap = takeMenu("Jeweled Skull")
        Room1_2()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room1_2()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room1_2()

#################################################

def Room2_1():
    name = "Room2_1"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        if move == "n":
            print(sectionDiv)
            print("You see a sea serpent in the water and decide it is best to stay on land")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_1()
        elif move == "s":
            print(sectionDiv)
            print("You follow path south...")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_2()
        elif move == "e":
            print(sectionDiv)
            print("You forgot your skis and cannot go that way")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_1()
        elif move == "w":
            print(sectionDiv)
            print("You follow path west...")
            input("\nPRESS ENTER TO CONTINUE")
            Room1_1()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_1()
    elif action == "look":
        print(sectionDiv)
        lookMenu(("Volcanic wasteland","A diamond in a pile of ash","Paths to west and south", "Ocean to the north"))
        Room2_1()
    elif action == "take":
        print(sectionDiv)
        inv.leatherCap = takeMenu("A diamond")
        Room2_1()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room2_1()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room2_1()

#################################################

def Room2_2():
    name = "Room2_2"
    action = roomMenu(name)
    if action == "move":
        move = moveMenu()
        if move == "n":
            print(sectionDiv)
            print("You follow path north...")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_1()
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
            Room1_2()
        elif move == "e":
            print(sectionDiv)
            print("You aproach the huge casmn in the ground")
            userInput = input("Would you like to dive? (y/n)")
            if userInput == "y":
                print("Display You make a spectacular swan dive and vanish into a void, never to be seen again. Game over")
                exit()
            else:
                Room2_2()
        else:
            print(sectionDiv)
            print("\nINVALID DIRECTION")
            input("\nPRESS ENTER TO CONTINUE")
            Room2_2()
    elif action == "look":
        print(sectionDiv)
        lookMenu(("A grass plain","East: a huge chasm in the ground","West and north are the paths", "A pot of gold in the grass","A glowing exit to the south"))
        Room2_2()
    elif action == "take":
        inv.leatherCap = takeMenu("Pot of Gold")
        Room2_2()
    elif action == "exit":
        print(sectionDiv)
        leaving = input("\nAre you sure you would like to exit? (y/n) ")
        if leaving == "y":
            exit()
        else:
            Room2_2()
    else:
        print(sectionDiv)
        print("\nINVALID ACTION")
        input("\nPRESS ENTER TO CONTINUE")
        Room2_2()




