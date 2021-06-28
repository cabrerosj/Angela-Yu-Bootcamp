print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

leftOrRight = input("Choose your path.\nLeft or right?\n").lower()

def chooseYourPath():
    if leftOrRight == "left":
        swimOrWait = input("Swim ahead or wait?\n").lower()
        if swimOrWait == "wait":
            primaryColors = input("Choose your door.\nRed, blue, or yellow?\n").lower()
            if primaryColors == "red":
                print("You were engulfed by flames.\nGAME OVER")
            elif primaryColors == "blue":
                print("You were ravaged by beasts.\nGAME OVER")
            elif primaryColors == "yellow":
                print("YOU FOUND THE TREASURE!!!")
            else:
                print("GAME OVER")
        else:
            print("You were attacked by trout.\nGAME OVER")
    else:
        print("You fell into a hole.\nGAME OVER")

chooseYourPath()