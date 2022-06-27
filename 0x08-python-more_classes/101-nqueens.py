"""Find all possible chess-board combinations of size n*n with n queens,
where queens are represented by the digit 2"""
from collections import Counter
import numpy as np


def block_positions(chess_board, row, column, limit):
    """Fills all squares that can no longer contain a queen with the value -1
    There are a maximum of 8 directions that must be blocked from a given square"""
    # Block left
    for col in range(column - 1, -1, -1):
        chess_board[row, col] = 0
    # Block right
    for col in range(column + 1, limit):
        chess_board[row, col] = 0
    # Block up
    for rw in range(row - 1, -1, -1):
        chess_board[rw, column] = 0
    # Block down
    for rw in range(row + 1, limit):
        chess_board[rw, column] = 0
    # Block L up-diag
    rw = row
    col = column
    while rw > 0 and col > 0:
        rw -= 1
        col -= 1
        chess_board[rw, col] = 0
    # Block L down-diag
    rw = row
    col = column
    while rw < limit - 1 and col > 0:
        rw += 1
        col -= 1
        chess_board[rw, col] = 0
    # Block R up-diag
    rw = row
    col = column
    while rw > 0 and col < limit - 1:
        rw -= 1
        col += 1
        chess_board[rw, col] = 0
    # Block R down-diag
    rw = row
    col = column
    while rw < limit - 1 and col < limit - 1:
        rw += 1
        col += 1
        chess_board[rw, col] = 0
    return chess_board


def initialise_board(num):
    """Build the empty board"""
    board = np.ones(num * num).reshape(num, num)
    return board


def valid_boards(board, row, num):
    """Find all valid N-queen boards"""
    global counter
    while row < num:
        indices = [index for index in range(num) if board[row, index] == 1]
        if indices == []:
            return False
        for index in indices:
            old_board = board.copy()
            board[row, index] = 2
            board = block_positions(board, row, index, num)
            is_possible = valid_boards(board, row + 1, num)
            board = old_board
            if not is_possible and index == indices[-1]:
                return False
    flattened = Counter(board.flatten())
    if flattened[2] == num:
        print(board)
        print()
        counter += 1


if __name__ == "__main__":
    counter = 0
    num = 5
    board = initialise_board(num)
    valid_boards(board, row=0, num=num)
    print(counter, "solutions")
    print("Finished")
