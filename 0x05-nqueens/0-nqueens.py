#!/usr/bin/python3
"""
N queens solution - place N non-attacking queens on an NxN chessboard
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    # Check row on left side
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check upper diagonal on left side
    for x, y in zip(range(row, -1, -1),
                   range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check lower diagonal on left side
    for x, y in zip(range(row, N, 1),
                   range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """Solve N queens problem using backtracking"""
    # Base case: If all queens are placed, return True
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Make recursive call to place rest of the queens
            solve_nqueens(board, col + 1)
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize empty NxN chessboard
    board = [[0 for x in range(N)] for y in range(N)]
    
    solve_nqueens(board, 0)
