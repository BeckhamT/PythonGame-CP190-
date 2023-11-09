import map as m

def runGame():
    username = input("Charecter Name: ")
    print(f"Welcome to the game {username}\n")
    m.username = username
    m.Room0_0()
 
runGame()
