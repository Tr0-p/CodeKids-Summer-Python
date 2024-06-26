import tkinter as tk

# mac specific
import tkmacosx as tkm


def checkWin(board):
    if board[0] == board[1] == board[2] != " ":
        return board[0]
    if board[3] == board[4] == board[5] != " ":
        return board[3]
    if board[6] == board[7] == board[8] != " ":
        return board[6]
    if board[0] == board[3] == board[6] != " ":
        return board[0]
    if board[1] == board[4] == board[7] != " ":
        return board[1]
    if board[2] == board[5] == board[8] != " ":
        return board[2]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    return " "


def press(row, col, self):
    # allows access to global variables
    global board, counter
    # each round, we increase the counter
    counter = counter + 1
    # converts rows and columns into indices
    cell = row * 3 + col

    # check if the cell in the board is not empty
    # prevent overwritting existing cells
    if board[cell] != " ":
        print("Cell is not empty")
        return

    # if counter is odd
    # write X onto the board
    # set the button to red
    if counter % 2 == 1:
        self.config(bg="red")
        board[cell] = "X"
    # if counter is even
    # write O onto the board
    # set the button to yellow
    else:
        self.config(bg="yellow")
        board[cell] = "O"

    # use checkWin to save result of the board
    result = checkWin(board)
    if result != " ":
        print(f"Player {result} has won!")

    # if nine turns have passed
    # all spaces have been filled
    # the game is a draw
    if counter == 9:
        print("It is a draw!")


# creates a list with 9 elements
# each element is a space
board = [" "] * 9
counter = 0

# create the window of our app
root = tk.Tk()
# creates the app title, set it as "Tic Tac Toe"
root.title("Tic Tac Toe")
# sets the size of the window
root.geometry("300x300")
# color the application black
root.config(bg="black")

# creates a container to hold our buttons
frame = tk.Frame(root, bg="black")
# move the container to the centre
frame.pack(expand=True)

# for loop - counts to 2
for row in range(3):
    for col in range(3):

        # creates the buttons, gives them background color and dimension
        # button = tk.Button(frame, bg="grey", width=8, height=4)
        button = tkm.Button(frame, bg="grey", width=75, height=75)

        # allocate position of button
        button.grid(row=row, column=col, padx=5, pady=5)

        # set what the button does when pressed
        button.config(command=lambda r=row, c=col, b=button: press(r, c, b))

root.mainloop()
