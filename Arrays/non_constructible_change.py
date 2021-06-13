"""
Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of change (the
minimum sum of money) that you cannot create. The given coins can have
any positive integer value and aren't necessarily unique (i.e., you can have
multiple coins of the same value).
For example, if you're given coins = [1, 2, 5] , the minimum amount of change
that you can't create is 4. If you're given no coins, the minimum amount of
change that you can't create is 1.
"""

# Direct approach
# Time: O(n) | Space: O(1)
###########################
# Sort the coins in ascending order
# Initialize the current change variable to 0
# Loop through coins
#   If coin value > current change + 1
#      return the current change + 1
#   else
#      Set the current change = current change + coin value
# return current change
###########################


def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1

