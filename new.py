import Random_Practice
from Random_Practice import game, letter_getter, player

player1 = player("Jamm", "28", "Xbox")
print(player1.console)

letter_getter("Home")

def brick_layer():
    num_bricks = int(input("How many bricks do you want to build your house: "))
    if num_bricks >= 5:
        print("Thats enough for the four walls and roof")
    else:
        print("That's not enough for, four walls and a roof")

brick_layer()