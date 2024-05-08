"""

@Author Timothy
@Date 8th May 2024

Dictionaries and Nested Structures

"""

# Dictionaries
# a way to store data

# number of each item
# shoppingList = [1, 2, 3, 2]

shoppingList = {
    # keys: value,
    "apple": 1,
    "banana": 2,
    "milk": 3,
    "potato": 2,
}

# accessing values in a dictionary
print(shoppingList["apple"])
print(shoppingList["banana"])

# adding values in a dictionary
shoppingList["carrot"] = 4
print(shoppingList)

# Quick Task 1 - Add 3 more items into the shopping list

# remove values from a dictionary
del shoppingList["carrot"]
print(shoppingList)

# Quick Task 2 - Remove all the original items from the dictionary
#                So that your new dictionary only has the items
#                you added in task 1

# del shoppingList["mango"]
# print(shoppingList)

# arr = [1, 2, 3, 4, 5]
# arr.remove(6)

# how can we check if something is in our dictionary????
if "mango" in shoppingList:
    del shoppingList["mango"]

# ================================

timothy = {
    "name": "Timothy",
    "age": 22,
    "fav color": "Blue",
    "fav food": "Chocolate",
    "hobbies": ["Coding", "Eating", "Sports"],
}

sonia = {
    "name": "sonia",
    "age": "10",
    "fav colour": "purple",
    "fav food": "pasta",
    "fav animal": "dog",
    "hobbies": ["swimming", "cycling", "drawing"],
}

anika = {
    "name": "anika",
    "age": 13,
    "school": "pates",
    "country": "england",
    "hobbies": ["reading", "writing", "cooking", "gaming"],
}

# Task 3 - Create a dictionary with your data

print(timothy["age"])  # 22
print(timothy["hobbies"])
print(timothy["hobbies"][0])  # Coding

classroom = [timothy, sonia, anika]

# Task(s) 4 - Print out a few values here

# example
print(classroom[2]["age"])

# Q1: Timothy's 2nd hobby
print(classroom[0]["hobbies"][1])

# Q2: Sonia's age
print(classroom[1]["age"])

# Q3: Anika's 4th hobby
print(classroom[2]["hobbies"][3])
