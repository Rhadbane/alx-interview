#!/usr/bin/python3
""" This script contains validUTF8 implementation """

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Implementation of validUTF8 function"""
    count = 0

    for character in data:
        binary_str = bin(character)[2:]
        binary_byte = binary_str.zfill(8)[-8:]

        if binary_byte.startswith("0") and count == 0:
            continue

        if binary_byte.startswith("110") and count == 0:
            count = 1
            continue

        if binary_byte.startswith("1110") and count == 0:
            count = 2
            continue

        if binary_byte.startswith("11110") and count == 0:
            count = 3
            continue

        if binary_byte.startswith("10") and count > 0:
            count -= 1
            continue

        return False

    return count == 0
