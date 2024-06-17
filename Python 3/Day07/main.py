import tkinter as tk

# carla specific
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
    global board, counter
    counter = counter + 1
    cell = row * 3 + col

    # check if cell is empty
    if board[cell] != " ":
        print("Cell is not empty")
        return

    # update board
    if counter % 2 == 1:
        self.config(bg="red")
        board[cell] = "X"
    else:
        self.config(bg="yellow")
        board[cell] = "O"

    # check if anyone has won yet
    result = checkWin(board)
    if result != " ":
        print(f"Player {result} has won!")

    # check if the game is tied
    if counter == 9:
        print("It is a draw!")


board = [" "] * 9
counter = 0

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

frame = tk.Frame(root)
frame.pack(expand=True)

for row in range(3):
    for col in range(3):
        # button = tk.Button(frame, bg="grey", width=75, height=75, text="")
        button = tkm.Button(frame, bg="grey", width=75, height=75)
        # pad x = padding x
        # pad y = padding y
        button.grid(row=row, column=col, padx=5, pady=5)
        button.config(command=lambda r=row, c=col, b=button: press(r, c, b))

root.mainloop()
