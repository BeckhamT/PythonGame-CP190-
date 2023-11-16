txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"
txtContinue = "PRESS ENTER TO CONTINUE"

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
            else:
                print("You already have this item")
                input(txtContinue)
        else:
            print("\nThere is nothing to take\n")
            input(txtContinue)


nothing = Item("nothing","there is nothing here")
leatherCap = Item("Leather Cap","You open the chest in the tree and...")
watch = Item("Watch", "You try go to reach for in the sand and")
topHat = Item("Golden Top Hat","")
diamond = Item("Diamond","")
skull = Item("Skull","")
potGold = Item("Pot of Gold","")

inventory = []