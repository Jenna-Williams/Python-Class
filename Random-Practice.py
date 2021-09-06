#Working with Lists
#List Functions .append, .extend, .insert(1,2), .remove, .clear, .pop, .count, .sort, .copy
import random
games = ["Arcadia", "Sonic", "Dragon's Dogma"]

print("What game should I play?")
#print(games[random.randrange(0,3)])
answer = input("Pick a number from 0-2: ")
print("You picked " + games[int(answer)] + "! I'll play it right away!" )
