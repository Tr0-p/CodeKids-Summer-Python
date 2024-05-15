"""

@Author Timothy
@Date 15-05-2024

Lists and nested lists
"""

# revision on lists

myList = [1, 2, 3, 4, 5]
print(myList[2])

myList[0] = 0
print(myList)  # [0, 2, 3, 4, 5]

# nested lists

table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# table[row number][column number]
print(table[1][2])

# i want to print the number 8
print(table[2][1])

##############

"""
     4
3 / 14
    12
    __
     2
"""

print(14 % 3)
