# Introduction to Functions

# Addition Function
def add(num1, num2):
    print(f"Adding {num1} and {num2}")
    print(num1 + num2)

# Call add function
add(567,875)

# Subtract Function - add input function
def subtract():
    num1 = int(input("Enter your first number"))
    num2 = int(input("Enter your second number"))
    print(f"Subtracting {num1} and {num2}")
    answer = num1 - num2
    print(f"The answer is {answer}.")

# Call subtract function
subtract()

# Multiplication function - 3 variables
def multiply():
    num1 = int(input("Enter your first number"))
    num2 = int(input("Enter your second number"))
    num3 = int(input("Enter your third number"))
    print(f"Multiplying {num1}, {num2} and {num3}")
    answer = num1 * num2 * num3
    print(f"The answer is {answer}.")

multiply()

# Division function - 2 variables
def divide():
    num1 = int(input("Enter your first number"))
    num2 = int(input("Enter your second number"))
    print(f"Dividing {num1} by {num2}")
    answer = num1 / num2
    print(f"The answer is {answer}.")

divide()

# Power
def power():
    num = int(input("Enter your number"))
    exponent = int(input("Enter your exponent"))
    print(f"Power {exponent} of {num} is")
    answer = num1 ** exponent
    print(answer)
    
# Square Root
def square():
    num = int(input("Enter your number"))
    answer = num1 ** 0.5
    print(answer)
