#!/usr/bin/python3
"""Module determins number of coins for total"""

cache = {0: 0}


def makeChange(coins, total):
    """Make change function

    Args:
        coins: first integer
        total: second integer

    Returns:
        Total count
    """
    coins = sorted(coins)
    for coin in coins:
        cache[coin] = 1
    return makeChangeInternal(coins, total)


def makeChangeInternal(coins, total):
    """Make change function internal

    Args:
        coins: first integer
        total: second integer

    Returns:
        Total count
    """
    if total < 0:
        return 0
    if total in cache:
        return cache[total]
    if len(coins) == 0:
        return -1

    maxCoin = coins.pop()
    if maxCoin > total:
        return makeChangeInternal(coins, total)

    mod = total % maxCoin
    if mod in cache:
        cache[total] = cache[mod] + int(total / maxCoin)
        return cache[total]

    temp = makeChangeInternal(coins, mod)
    temp2 = makeChangeInternal(coins, total)
    if 0 < temp and (temp2 == -1 or temp < temp2):
        cache[total] = temp + int(total / maxCoin)
        return cache[total]
    if 0 < temp2:
        cache[total] = temp2
        return cache[total]

    return -1
