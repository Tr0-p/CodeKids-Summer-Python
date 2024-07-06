import requests

# RECAP

# Input
my_number = int(input("Give me a number"))

# Lists
# Indexing
#          0  1  2  3  4
#          -5 -4 -3 -2 -1
my_list = [2, 4, 6, 8, 10]
print(my_list[2])  # 6
print(my_list[-1])

print(len(my_list))  # length of the list / how many items are inside

# Looping
index = 0
for x in range(len(my_list)):
    # print(my_list[index])
    index = index + 1

for x in range(len(my_list)):
    print(my_list[x])

# good to know thing about python
# for every "item" in "my_list", print the "item" out
for item in my_list:
    item = item + 2
    # print(item)

# Adding items into a list
print(my_list)
my_list.append(12)
print(my_list)

# Remove items from a list
# my_list.remove(0)
my_list.remove(2)  # targets the specified VALUE
print(my_list)

my_list.pop(0)  # targets the specified INDEX
print(my_list)

# Dictionaries
# Creating
people = {
    "Timothy": 22,
    "Sam": 23,
    # ....
}

# Indexing
print(people["Sam"])  # Sam's age

# String Functions
my_string = "some text"
my_string_2 = "SOME other text"
my_string_3 = "some text with a new line\n"
print(my_string.upper())
print(my_string_2.lower())
print(my_string_3.strip())  # removes any blank lines that follow

# APIs
url = f"https://pokeapi.co/api/v2/pokemon/pikachu/"

result = requests.get(url).json()
print(result.keys())  # first, look at what keys there are, to know what data there is

# FILE WRITING
with open("my_file.txt", "w") as w:
    w.write("some text in a file\n")
