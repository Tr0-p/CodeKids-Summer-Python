'''

DOOR OF DOOM

With loops
Tracks how many lives it takes to survive the game  

'''

# We need the random library to add a bit of chance to our game.
import random

# We're creating a variable to keep track of how many times the player has lost.
deaths = 0

# Let's start the game with a welcome message and explaining the rules.
print("Welcome to the Maze Game!")
print("You are standing at the entrance of a dangerous maze. Your goal is to escape.")
print("In every step, you have three doors: A, B, and C. Your choices will determine your fate!")
print("Enter your name:")
name = input()

# We're using a 'while True' loop to keep the game running until the player wins.
# 'True' here means that the loop will keep running indefinitely until we break it.

while True:

    print("")
    print("")


    # Ask the player to make their first choice.
    choice = input(f"{name}, you see three doors in front of you (A, B, C). Which one do you choose? ").upper()

    # Now we use if-elif-else statements to create different outcomes based on the player's choice.
    if choice == 'A':
        choice = input(f"Well done {name}, you have survived the first trap. Now, choose again (A, B, C): ").upper()
        if choice == 'B':
            # Oh no, they fell into a pit of spikes. We add 1 to the death count and start over.
            print(f"Sorry {name}, you fell into a pit of spikes. Try again.")
            print("")
            deaths += 1 
        elif choice == 'A':
            # Here we flip a coin to decide if they escape or not.
            if random.randint(0, 1) == 0:
                # They escaped! We tell them how many times they died and break the loop to end the game.
                print(f"Congratulations {name}, you found the exit and escaped the maze! You died {deaths} times before escaping.")
                print("")
                break 
            else:
                # A grue got them... We add 1 to the death count and start over.
                print(f"Sorry {name}, you were eaten by a grue. Try again.")
                print("")

                deaths += 1
        else:
            # A giant rock falls on them. We add 1 to the death count and start over.
            print(f"Sorry {name}, a giant rock fell on you. Try again.")
            deaths += 1

    elif choice == 'B':
        choice = input(f"Great {name}, you dodged a swinging axe. Now, choose again (A, B, C): ").upper()
        if choice == 'C':
            # Again, we flip a coin to decide their fate.
            if random.randint(0, 1) == 0:
                # They escaped! We tell them how many times they died and break the loop to end the game.
                print(f"Congratulations {name}, you found the exit and escaped the maze! You died {deaths} times before escaping.")
                print("")
                break
            else:
                # They fell into lava... We add 1 to the death count and start over.
                print(f"Sorry {name}, a trapdoor opened and you fell into lava. Try again.")
                print("")

                deaths += 1
        else:
            # They were attacked by bats. We add 1 to the death count and start over.
            print(f"Sorry {name}, you were attacked by a swarm of bats. Try again.")
            print("")

            deaths += 1

    else:
        # Poisonous gas was released. We add 1 to the death count and start over.
        print(f"Sorry {name}, a poisonous gas was released when you opened door C. Try again.")
        deaths += 1
