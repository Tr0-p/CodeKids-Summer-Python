"""

@Author Timothy
@Date 6th June 2024

Tic Tac Toe Game from scratch

"""


def printBoard(board):
    display = """ {} | {} | {}\n---+---+---\n {} | {} | {}\n---+---+---\n {} | {} | {}\n\n"""
    print(display.format(*board))


# diagonally
# horizontally
# vertically
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


def __checkWin(board):
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for x, y, z in combinations:
        if board[x] == board[y] == board[z] != " ":
            return board[x]
    return " "


board = [" "] * 9

printBoard(board)

counter = 0
while True:
    counter = counter + 1
    cell = int(input("Cell [0-8]: "))

    if counter % 2 == 1:
        board[cell] = "X"
    else:
        board[cell] = "O"

    printBoard(board)

    result = checkWin(board)
    if result != " ":
        print(f"Player {result} has won!")
        break
