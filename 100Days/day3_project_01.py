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
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome TO Treasure Island.\n Your mission is to find the treasure.")
print("-" * 80)
print("let's start your journey, one wrong decision will end your hunt.")

hunter_direction = (input("You are at crossroads, where do you want to go? ('left' or 'right'): ").upper())
if hunter_direction == "LEFT":
    print("bravo, go ahead")
    hunter_door = (input("There is a river ahead? What would you do now? ('swim' or 'wait': ").upper())
    if hunter_door == "WAIT":
        print("Patience paid you well, river is now dried, go ahead")
        hunter_door = (
            input("You have three doors in front of you. Which one will you open? ('red' 'blue' 'yellow': ").upper())
        if hunter_door == "YELLOW":
            print("Hurray, you found the treasure chest, you win.")
        elif hunter_door == "RED":
            print("oops, hungry lion attacked you")
        elif hunter_door == "BLUE":
            print("oops frozen room, now you will stay here forever frozen icicle, jk, game over")
        else:
            print("Game Over, you lost")
    else:
        print("Game Over, you are drowned")
else:
    print("Game Over, you fell into a gorge")




