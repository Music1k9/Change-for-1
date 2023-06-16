# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:53:09 2023

@author: nlewisbassett
"""

def count_change(amount):
    coins = [25, 10, 5, 1]  # Available coin denominations
    ways = [0] * (amount + 1)  # Initialize a list to store the number of ways

    ways[0] = 1  # There is one way to make change for 0 cents (using no coins)

    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]  # Accumulate the ways to make change

    return ways[amount]

# Test the function with one dollar (100 cents)
num_ways = count_change(100)
print("Number of ways to make change from a dollar:", num_ways)
