#Working with Lists
#List Functions .append, .extend, .insert(1,2), .remove, .clear, .pop, .count, .sort, .copy
import random
randomLists = [
    [1, 2, 3],
    ["tough", "Hard", "strong "]
]
games = ["Arcadia", "Sonic", "Dragon's Dogma"]

def letter_getter(word):
    i = 0
    for letter in word:
        print(letter)
        i+=1
    print("There are " +str(i)+ " letters in the word " + word.upper() + ". The first letter is " + word[0].upper())

class game:
    def __init__(self, name, type, rating):
        self.name = name
        self.type = type
        self.rating = rating

class player:
    def __init__(self, name, age, console):
        self.name = name
        self.age = age
        self.console = console
