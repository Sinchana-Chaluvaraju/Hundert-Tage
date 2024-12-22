'''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
choice1 = input("you are at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()
if choice1 == "left":
    choice2 = input('You have come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at the island unharmed. "
                        "There is a house with 3 doors. One red,"
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.\n")
        elif choice3 == "yellow":
            print("You have found the treasure. You win!\n")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game Over!\n")
        else:
            print("You chose a door that does not exist. Game over!\n")
    else:
        print("You got attacked by an angry trout. Game over!\n")
    # Continue the game.
else:
    print("You fell in to a hole. Game over.\n")





















"""
print("Welcome to Python Pizza Deliveries!!")
size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra pizza? Y or N: ")
bill = 0

if size == "S":
    bill = 10
    print("pizza small is $10 ")
elif size == "M":
    bill = 15
    print("pizza medium is $15 ")
else:
    bill = 20
    print("pizza large is $20 ")

if pepperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"Total amount is ${bill}")

# Conditional Statements : if / else
water_level = float(input("What is the current water level?"))
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")


Tickets Box Replacement:
    1.height qualification  > 120 cm


height = float(input("Enter your height: "))
if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("We are sorry. You cannot ride :( ")



To check the number is even or odd.
Even number 12 % 2 = 0


number = int(input("Enter a number to check whether it is even or odd: "))
if number % 2 == 0:
    print("The number entered is even.")
else:
    print("The entered number is odd.")



# Ticket price distribution based on age. for example:  (1) <= 18 : $7 (2) > 18 : $12
# Nested if / else

age = float(input("Enter your age: "))
height = float(input("Enter your height in cms: "))
bill = 0
if height > 120:
    print("Good News! You can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print("ticket price for you is $5.")
    elif age <= 18:
        bill = 7
        print("Ticket price for you is $7.")
    else:
        bill = 12
        print("Ticket price for you is $12.")

    wants_photo = input("Do you want to print a photo?(note: use the lower case) y for Yes or n for No: ")
    if wants_photo == "y":
        # Adds $3
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You cannot ride the rollercoaster :( ")


"""


