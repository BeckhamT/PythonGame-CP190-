# PythonGame-CP190-

Due October 21st 2023 

Prof: Daniel Kaukinen


This project is for my college Porgramming Fundamentals Course (CP190)


# OOP vs Functions:

The orignal project "Game01" was created using functions exclusively

Testing with OOP in "Game02" to see if I can shorten the code and streamline the creation of "Rooms" or "Levels" (I changed the naming of Rooms from "Game01" to Levels in "Game02").

By using classes in "Game02" it makes level creation easier but is harder to understand how it works 

# Game01:

### Notes: 

- Was depating on what should be a seperate function ie roomMenu(), moveMenu() ect
- As I was making more and more functions for the game is when I decided to try and use objects for the levels to streamline their creation
- Lots of copy and pasting for the "Room" creation 


## Files:

  map.py contains all the rooms/levels that you move around and the functionality of moving, looking, take, and exit.

  inventory.py contains all the items with bool values and a list of what items the charecter has.

  gameFile.py calls map.py and assigns the username.

# Game02: 

### Notes: 

- Classes for Direction, Item and Level
- The Level Class contains menu functions (main menu, move menu ...)
- In order to call other Levels Main Menus the level.menu() needs to return, the return value calls another level.menu() either the same level or a new level if the player is moving. To accomplish this I used return a command as a string and pass it into the eval() function. Not sure if this is proper or not.
- Was debating weather or not to set the direction, item, and look when the level was created or to difene those after creation and decided on assiging them after to make the code more readable.


## Files:

  *should probably seperate classes into other files*

  main.py contains all the code required to run the game

  

