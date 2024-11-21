#!/usr/bin/python3
""" script for the implementation of rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Implementation of rotate_2d_matrix"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
