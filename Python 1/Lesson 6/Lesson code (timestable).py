# Task 1: Welcome message using print()
print("Hello and welcome to the world's best Times Tabler!")

while True:
    
    timestable = int(input("Which times tables do you want me to do? "))

    # Task 2: Create a variable and input to store the number to which the computer
    #         should work at the times table up until
    number = int(input("Up to which number do you want me to work out the timestable?"))

    # for loop
    for index in range(number+1):
        print(f"{index} x {timestable} = {index * timestable}")

    # Task 3: Improve our print statement using an f-string to display
    #         the calculation on each line (e.g. 5 x 8 = 40)
