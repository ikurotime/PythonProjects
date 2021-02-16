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
print('---Be sure to type the words exactly like in the "quotation marks"---')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
firstChoice = input('You\'re at a cross road. Where do you want to go? Type "left or "right" ')
if firstChoice == 'left':
    secondChoice = input('You face a river, "swim" or "wait"?')
    if secondChoice == 'wait':
        thirdChoice = input('You face three doors: "Red", "Yellow" and "Blue". Which door would you open?')
        if thirdChoice == 'Yellow':
            print('You win!')
        elif thirdChoice == 'Red':
            print('Behind the red door was a room in fire, you get burned. Game Over')
        elif thirdChoice == 'Blue':
            print('You get eaten by beasts... somehow. Game Over')
        else:
            print('Game Over')
    else:
        print('You got attacked by a shark. Game Over')

else:print('You fell into a hole. Game Over')
