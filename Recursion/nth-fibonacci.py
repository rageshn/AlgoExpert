"""
 The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the
 nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer 'n' and
 returns the nth Fibonacci number.
 Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1.
 For the purpose of this question, the first Fibonacci number is F0; therefore getNthFib(1) is equal to F0,
 getNthFib(2) is equal to F1, etc.
"""

# Using recursion
# Time: O(2 ^ n) | Space: O(n)
##############################
# Call fibonacci function with n as parameter --> fibonacci(n)
# return result
#
# Declare a function --> fibonacci(n)
#   If n <= 1
#       return 0
#   If n == 2
#       return 1
#   recursively call fibonacci on (n - 1) and (n - 2) and add them.
##############################


def getNthFib(n):
    result = fibonacci(n)
    return result


def fibonacci(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


# Iterative approach
# Time: O(n) | Space: O(1)
##########################
# Initialize last_two = [0, 1] This hold the values for n = 0 & 1 (base cases)
# Initialize counter = 3 (skipping first two as they were added in the last_two array)
# Loop till counter <= n
#   Set next_fib = last_two[0] + last_two[1]
#   last_two[0] = last_two[1]
#   last_two[1] = next_fib
#   counter += 1
# If n > 1
#   return last_two[1]
# else
#   return last_two[0]
##########################


def getNthFib(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


