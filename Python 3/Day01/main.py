"""

@Author: Timothy
@Date: 25th April 2024

Recapping on Dictionaries, Functions, and APIs

"""

# Dictionaries

dictionary = {
    # key   # value
    "apple": 2,
    "banana": 3,
}

print(dictionary["apple"])

dictionary["orange"] = 10
print(dictionary)

del dictionary["apple"]
print(dictionary)

if "mango" in dictionary:
    print(dictionary["mango"])

# It is a collection of items
# Stored in key-value pairs
# Access the value with a key

# Functions
# Predefined code, can be called
# Use the word def


def convertsC2F(celsius):
    f = celsius * 9 / 5 + 32
    return f


print(convertsC2F(37))

# Task 1 - Write a function that can tell me
#          if a number is a prime
#
# Divisible by 1 and itself only


def isPrime(number):
    if number <= 1:
        return False
    else:
        for index in range(2, number):
            if number % index == 0:
                return False
    return True


print(isPrime(37))  # True
print(isPrime(38))  # False

# Divisibility

print(6 % 3)  # 0
print(5 % 3)  # 2
print(4 % 3)  # 1
print(3 % 3)  # 0

# Task 2 - Create a function that creates a
#          list with numbers 0 to n


def createList(n):
    # some code here
    l = []
    for index in range(0, n):
        l.append(index)
    return l


l = createList(5)
print(l)  # [0, 1, 2, 3, 4]
