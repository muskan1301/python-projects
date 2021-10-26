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
choice_1 = input('You\'re are at a crossroad where do u want to go? Type "left" or "right". ').lower()
if choice_1 == "left":
    choice_2 = input("You have come to a lake.There is an island in the middle of lake. Type 'wait' to wait for a boat.Type 'swim' to swim across? ").lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red,one yellow and one blue.Which color do u want to choose? ").lower()
        if choice_3 =="red":
            print("It is a room full of fire.")
            print("Game Over")
        elif choice_3 == "yellow":
            print("You found the treasure.")
            print("!You Win!")
        elif choice_3 == "blue":
            print("You enter a room full of beasts.")
            print("Game Over.")
        else:
            print("You choose a door that doesn't exist.")
            print("Game Over!")
    else:
        print("You were attacked by an angry trout.")
        print("Game Over!")
else:
    print("You fell into a hole.")
    print("Game Over!")
