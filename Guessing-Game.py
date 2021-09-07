import random
i = 1
number = int(random.randrange(0,10))
guess = int(input("Guess What Number I'm Thinking Of Between 0-10? "))

while guess != number:
    print("Guess Again")
    guess = int(input(""))
    i += 1

print("You Got It! It Took You " + str(i) + " Tries")