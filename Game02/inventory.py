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


nothing = Item("nothing","Thre is nothing here")

inv = []