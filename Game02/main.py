from typing import Any
import time
import inventory as inv
import levels as lev

# main.py
# Beckham Thompson

#VARIBLES

txtDirection = "                  North\nYou can move:  West   East\n                  South"
sectionDiv = "\n" *3 +"***************************************************\n"
txtContinue = "PRESS ENTER TO CONTINUE"

def Main():
    # The Level Menu will Return a level to call as a string ie "level0_0.menu()"
    # Eval will turn the string into that line of code
    # Every time the levels menu gets called it is called here

    result = lev.Level2_2.menu()
    while result != "exit":
        result = eval("lev."+result)    


Main()
