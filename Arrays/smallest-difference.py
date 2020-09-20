"""
Write a function that takes in two non-empty array of integers, finds the pair of numbers (one from each array),
whose absolute array is closest to zero, and returns an array containing these two numbers,
with number from first array in first position.
Assume that there will only be one pair of numbers with the smallest difference. 
"""


# Basic approach
# Time: O(n^2) | Space: O(n)
#############################
# Set the least variable to a random large number.
# Initialize small_diff as empty array.
# Use nested for loops to traverse the array and get the absolute difference between two numbers.
#     If the difference is less than least variable values,
#         Set least as difference.
#         Set small_diff to the two numbers.
# return small_diff
#############################


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    least = 1000
    small_diff = []
    for first in arrayOne:
        for second in arrayTwo:
            abs_diff = abs(first - second)
            if abs_diff < least:
                least = abs_diff
                small_diff = [first, second]
    return small_diff


# Using Binary Search
# Time: O(n*log(n) + m*log(m)) | Space: O(1)
##################################
# Sort both arrays
# Initialize least variable to random large number.
# Initialize small_diff to empty list.
# Loop through every element in arrayOne (val)
#     Set mid as middle index of arrayTwo, left as 0 and right as arrayTwo length
#     Loop till mid is less than right and greater than left
#         Set array_sum as absolute difference between val and arrayTwo[mid]
#         if array_sum < least, update least to array_sum, right = mid, mid as (mid - left) / 2
#         if array_sum > least, update left = mid, mid as (right - left) / 2
#         else set small_diff as [val, arrayTwo[mid]] and break the loop.
# return small_diff
# Inner loop uses binary search to get the smallest absolute difference between val and arrayTwo[mid].
##################################


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.

    # -1, 3, 5, 10, 20, 28,
    # 15 17 26 134, 135
    arrayOne.sort()
    arrayTwo.sort()  # n*logn
    least = 1000
    small_diff = []
    for val in arrayOne:  # n*logn

        mid = int(len(arrayTwo) / 2)
        left = 0
        right = len(arrayTwo) - 1

        while left < mid < right:  # mid > left and mid < right
            array_sum = abs(val - arrayTwo[mid])
            if array_sum < least:
                least = array_sum
                right = mid
                mid = int((mid - left) / 2)
            elif array_sum > least:
                left = mid
                mid = int((right - left) / 2)
            else:
                small_diff = [val, arrayTwo[mid]]
                break

    return small_diff


# Using two pointers
# Time: O(n*log(n) + m*log(m)) | Space: O(1)
#############################################
# Sort both arrayOne and arrayTwo
# Initialize two pointers to 0 for two arrays
# Initialize two variables least, currentSum to infinity.
# Initialize smallest_pair to empty array.
# Loop both arrays at same time, with firstIdx and secondIdx
#     Get the values from two arrays as firstNumber and secondNumber
#     If firstNumber is less than secondNumber
#         Get the absolute difference and increment firstIdx (Incrementing secondIdx will give even bigger difference)
#     If secondNumber < firstNumber
#         Get the absolute difference and increment secondIdx (Incrementing firstIdx will give even bigger difference)
#     else
#         return [firstNumber, secondNumber]
#     If absolute difference is less than least
#         Set least to absolute difference
#         Set smallest_pair to [firstNumber, secondNumber]
##############################################


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    firstIdx = 0
    secondIdx = 0
    least = float('inf')
    currentSum = float('inf')
    smallest_pair = []

    while firstIdx < len(arrayOne) and secondIdx < len(arrayTwo):
        firstNumber = arrayOne[firstIdx]
        secondNumber = arrayTwo[secondIdx]
        if firstNumber < secondNumber:
            currentSum = secondNumber - firstNumber
            firstIdx += 1
        elif secondNumber < firstNumber:
            currentSum = firstNumber - secondNumber
            secondIdx += 1
        else:
            return [firstNumber, secondNumber]
        if currentSum < least:
            least = currentSum
            smallestPair = [firstNumber, secondNumber]

    return smallestPair
