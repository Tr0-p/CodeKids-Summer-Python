"""
name
date
what we doing

@Author Timothy
@Date 24-04-2024

Recap on statements, conditions, and loops
"""

# how do we output information

print("Hello, Python")

# variables
# something you set tell python to remember
# can be changed

myVariable = "Timothy"

# ask the user for some data/information

name = input("What is your name? ")

# TASK 1 - print out the name from the input

print(name)

# f string
# put variables inside it

# print(f"Your name is {name}, you are a student of python 2")

# if elif and else

if name == "Tim":
    print("Hi teacher")
elif name == "Fabian" or name == "Sonia" or name == "Anika" or name == "Selim":
    print("Hi student")
else:
    print("Sorry, I don't know who you are...")

# loops
# what are the 2 main types of loops in python
# for something in range
# while True / while False

for index in range(1, 12, 3):
    print(index)

# Task 2 - Print out every number from 0 to 50, including both 0 and 50

# for index in range(0, 51):
#    print(index)

# Task 3 - Print out every single multiple of 10, from 0 to 101

for index in range(0, 101, 10):
    print(index)

# while loop

counter = 0

while counter < 5:
    print(counter)

    counter = counter + 1

# lists
# a set amount of items and things

shoppingList = ["apple", "orange", "banana"]
print(shoppingList)

# access items in a list

print(shoppingList[0])
print(shoppingList[-1])

# add item into a list

shoppingList.append("kiwi")
print(shoppingList)

# remove an item from a list

shoppingList.remove("apple")
print(shoppingList)

if "mango" in shoppingList:
    shoppingList.remove("mango")

print(shoppingList)

# Task 4 - Ask the user what item to remove from the shopping and remove it if it's there

item = input("What is the item you want to remove? ")

if item in shoppingList:
    shoppingList.remove(item)

print(shoppingList)
