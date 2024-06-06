# Task 1: Welcome message using print()
print("Hello and welcome to the world's best Times Tabler!")

timestable = int(input("Which times tables do you want me to do? "))

# Task 2: Create a variable and input to store the number to which the computer
#         should work at the times table up until
number = int(input("Up to which number do you want me to work out the timestable?"))

# for loop
for index in range(number+1):
    print(index * timestable)
