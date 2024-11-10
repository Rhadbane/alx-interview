#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.

How do I solve this when I don't know how to play chess?
"""
import sys


def queens(n):
    """Solve for the queens
    """
    print(n)


def play():
    """This is the main program
    """
    try:
        n = sys.argv[1]
        x = int(n) / 1
        if x < 4:
            print('N must be at least 4')
        else:
            queens(n)
    except IndexError:
        print("Usage: nqueens N")
    except (TypeError, ValueError):
        print("N must be a number")


if __name__ == "__main__":
    play()
