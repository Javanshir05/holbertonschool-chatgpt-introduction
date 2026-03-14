#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # check range
        if row not in range(3) or col not in range(3):
            print("Invalid position. Use 0, 1, or 2.")
            continue

        # check if spot is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # place move
        board[row][col] = player

        # check winner
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # check draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()