"""
@Author Timothy
@Date 15-05-2024

Tic Tac Toe
"""


def printBoard(board):
    print("\n   [1] [2] [3]")
    for i, row in enumerate(board):
        print(f"[{i + 1}] " + " | ".join(row))
        print("   " + ("---+" * 3)[:-1] if i < 2 else "")


def checkWin(board):
    l = ["012", "345", "678", "036", "147", "258", "048", "246"]
    for p in l:
        r = list(map(lambda x: board[int(x) // 3][int(x) % 3], p))
        if r[0] == r[1] == r[2] != " ":
            return r[0]
    return " "


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

printBoard(board)

"""
turn: 0, 1, 2, 3, ...
symb: O, X, O, X, ...
"""

counter = 0
while True:
    # input section
    row = int(input("Row: ")) - 1
    col = int(input("Col: ")) - 1

    # check if the cell is already filled
    if board[row][col] != " ":
        continue

    # update section
    if counter % 2 == 0:
        board[row][col] = "O"
    else:
        board[row][col] = "X"

    # board preview
    printBoard(board)

    # checking if the game has been won
    result = checkWin(board)  # possible returns: O, X, " "
    if result != " ":
        print(f"Player {result} has won!")
        break

    # checking if the game is tied
    counter = counter + 1
    if counter == 9:
        print("It is a tie!")
        break
