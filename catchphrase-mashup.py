"""
file: catchphrase-mashup.py
take user input on possible catch phrase nouns
choose randomly from a list of potential adverbs
provide a premade list of noun/adverb combinations
provide a random list of nouns and one of adverbs

"""
import random

# a dice that has 10 sides
NUM_SIDES = 10

# setting seed is useful for debugging
# random.seed(1)
die1 = random.randint(1, NUM_SIDES)

#total = die1 + die2
#print("Dice have " + str(NUM_SIDES) + " sides each.")
 #print("First die: " + str(die1))
  #  print("Second die: " + str(die2))
   # print("Total of two dice: " + str(total))

"""Get user input and choose random strings"""
print("Create a fun catch phrase...")
user_noun = input("Enter a noun: ")
my_adverb = random.choice(["cheesy", "glowing", "slimy", "fluffy", "ornery", "cheerful", "trusting", "grouchy"])
user_random_noun_pick = ["horse", "kitten", "adventurer", "island-dweller", "aardvark", "puppy", "elephant", "seagull","dolphin", "towel"]
print(f"Hi there {my_adverb} {user_noun}!")
print("")  # an empty line
print("Now I'll pick a catchphrase for you!")
user_int = int(input("Enter a number between 1 and 10: ")) # use that random number to pull from the noun list
user_random_noun = user_random_noun_pick[user_int]
print("")  # an empty line
## need to create a new random adverb choise
## ideally, do a check to make sure it is not hte same as previous choice
# while previous choice == current choice, roll.
print(f"Hi there {my_adverb} {user_random_noun}!")