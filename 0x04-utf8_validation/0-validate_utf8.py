#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    data: an array of integers
    Return: True if data is a valid UTF-8 encoding, else return false
    """

    byte_Count = 0
    for i in data:
        if byte_Count == 0:
            if i >> 5 ==0b110 or i >> 5 == 0b1110:
                byte_Count = 1
            elif i >> 4 == 0b1110:
                byte_Count = 2
            elif i >> 3 == 0b11110:
                byte_Count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_Count -= 1
    return byte_Count == 0
