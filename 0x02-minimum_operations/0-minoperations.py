#!/usr/bin/python3

"""
Solution to minimum operations interview practice questions.
"""
from sys import argv


def minOperations(n):
    """
    calculate the minimum number of operations to go from one 'H' to n 'H's
    if the only available operations are "Copy All" and "Paste".
    """

    # if n is 1, 0 operations are needed.
    if n <= 1:
        return 0

    # find the smallest prime factors
    for i in range(2, int((n/2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n
