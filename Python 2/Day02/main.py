"""

@Author Timothy
@Date 1st May 2024

Functions

"""

# Functions
# use the def command
# run several commands

def greeting(name):
    print(f"Hello {name}")

greeting("Timothy")

def add(num1, num2):
    result = num1 + num2
    print(f"The result is {result}")

add(3, 5)

# Task 1 - Write a function that substracts
#          two numbers

def minus(num1, num2):
    result = num1 - num2
    print(f"The result is {result}")

minus(7, 10)

# Task 2 - Write 2 functions, one for multiplication and division
#          Behave like the other two functions as well
#          Expand your calculator, so that it can handle, * and /

# Task 3 - Make your calculator run forever
#          Remember to add a condition to the user to exit
#          Example: action == 0, ends the loop

def multiply(num1, num2):
    result = num1 * num2
    print(f"The result is {result}")

def divide(num1, num2):
    result = num1 / num2
    print(f"The result is {result}")

while True:
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    print("0: exit")
    action = int(input("What action do you want to do? "))
    if action == 0:
        break
    
    num1 = int(input("What is your first number? "))
    num2 = int(input("What is your second number? "))

    if action == 4 and num2 == 0:
        print("Can't divide by zero")
        continue

    if action == 1:
        add(num1, num2)
    elif action == 2:
        minus(num1, num2)
    elif action == 3:
        multiply(num1, num2)
    elif action == 4:
        divide(num1, num2)














