#!/usr/bin/python3
"""
Find the fewest number of coins to meet a given amount
"""


def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet total.
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[total] if dp[total] != total + 1 else -1
