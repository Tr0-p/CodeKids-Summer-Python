'''
PYTHON 2 - LESSON 1
Introduction and Recap

@Author: Nav
@Date: 20 April 2024


Explain what we are going to do this term

(1) Recap - its important to understand basics
(2) functions
(3) APIs and connection to websites
(4) Games with Turtle

'''


## STEP 1: Python takes in information and displays information

# How do we display information with Python?
print("Hello and welcome to Python")
# Go ahead and practice at least 2 print commands

# How do we give python information. What is that function?
input("What is your name?")

# So what is wrong with this? What are missing?
# Any information has to be stored. Does anyone remember the thing that Python uses
# to store information. A clue, begins with a 'V'

name = input("What is your name?")
# Go ahead and practoce at least 2 more inputs

# Ask for a age input
age = input("What is your age?")
# Is 'age' a number?

# KEY DATA TYPES IN Python 
# STRINGS, INTEGERS, BOOLEANS
# Anything with an input is treated as a String, which means
# we have to convert it to a number
# CONVERSIONS or 'CASTING'

age = int(input("What is your age?"))

# Now we can do maths with this variable
print(age + 12)


# STEP 2: SELECTORS. How dopes Python make decisions

# We use IF/ELIF/ELSE

if name == "Nav":
    print("You are cool!")
else:
    print("Not cool")

# Create a new IF/ELSE statement
# Use a new input
# How can you you say if AGE is more than 8 yopu can use me


# We can also use IF and ELIFs like a waterfall check

if name == "Nav":
    print("You are cool!")
elif name == "Mehraab":
    print("Slightly cool")
else:
    print("Not cool")


# STEP 3 - LOOPS

# What are the 2 main loops in Python?
# FOR loop and the WHILE
# When would we use each loop? What situation?

# FOR LOOP is useful when count or loop a certain number of times
# WHILE loops useful for games i.e. keep looping until Player1 is alive


for i in range(0,10):
    print("I'm looping")

# can you do this 100 times?

# The i is a counter for how many times loop is running
# i can be anything 
for i in range(0,10):
    print(i)

# Structure of a FOR loop (STARTING NUMBER, ENDING NUMBER, HOW TO COUNT)
for i in range(10):
    print(i)

# Count from a range
for i in range(100,200):
    print(i)

# Count in blocks
for i in range(100,200, 10):
    print(i)

# Challenge: make a count down timer with a blast off
# Import libraries like TIME
for i in range(100,0, -1):
    print(i)

print("BLAST OFF!")





## STEP 4 - importing stuff 

import random

# Choose random numbers, randomly pick things from a list, Shuffle a list

# Pick a number = randint
# Pick from a list = choice
toss = ['head','tails']

print(random.choice(toss))



# TASK 4
# Can you pick some random stuff yourself ie randomly pick out 5 lottery numbers 


import random

# Ask the user for 5 numbers
user_numbers = []
for i in range(5):

    # {} is a placeholder that will be replaced with the value of i + 1.
    # So, for the first iteration of the loop, it will display "Enter number 1:",
    #for the second iteration "Enter number 2:", and so on.
    user_number = input("Enter number {}: ".format(i + 1))
    user_numbers.append(user_number)

# Display user's numbers
print("\nYour numbers:")
for number in user_numbers:
    print(number)

# Generate 5 random numbers
random_numbers = []
for i in range(5):
    # convert the integers to strings 
    random_numbers.append(str(random.randint(1, 20)))

# Display randomly generated numbers
print("\nRandomly generated numbers:")
for number in random_numbers:
    print(number)

            
    
