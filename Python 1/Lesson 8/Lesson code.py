my_shopping = [] # shopping list

# Task 1: Create a welcome message using the print statement
print("I am your personal shopping assistant - start adding your items now!")

while True:
    # Task 2: Create an input statement which asks the user if they want to add
    #         any items to their shopping list (Y/N) - store the answer in a variable
    # Extension: Convert the user's input to upper case (e.g y --> Y, n --> N)
    add_item = input("Do you want to add items to your shopping list (Y/N)? ").upper()
    if add_item == "N":
        break # ends the while true loop
    else:
        # Task 3: Create an input statement which asks the user to type in the
        #         item they want to add into their shopping list and stores it in
        #         a variable called 'item'
        item = input("Enter your grocery item here: ")
        my_shopping.append(item) # add item to the end of my_shopping

print(my_shopping)
