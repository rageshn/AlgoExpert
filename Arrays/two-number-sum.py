"""
Write a function that takes a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
If no two number sum up to the target sum ,then the function should return an empty array.
The target sum should be obtained by summing two different integers; you cant add an integer to itself to get the target sum.
You can assume that there will be at most one pair of number summing up to the target sum.
"""


# Basic approach
# Time: O(n^2) | Space: O(1)
##############################
# Set i between 0 and len(array)
# Set j between 1 and len(array)
# Use nested for loops
# Check if array[i] + array[j] == TargetSum
# If Yes, return [array[i], array[j]]
# Once the loop completes, return []
##############################

def twoNumberSum(array, targetSum):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length-1):
            if (i != j) and (array[i] + array[j] == targetSum):
                return [array[i], array[j]]
    return []


# Using Hash Table
# Time: O(n) | Space: O(n)
##############################
# Traverse the array
#    Set X = current number, Y = TargetSum - X
#    Check if Y in Hash Table
#    If Y is not available in HT, then add X to HT and continue
#    If Y is available in HT, then return [X, Y]
# return []
##############################

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# Using Sort
# Time: O(n*log(n)) | Space: O(1)
##############################
# Sort the array
# Set two pointer Left = 0 and Right = len(array)-1
# check if array[Left] + array[Right] == TargetSum
# If the Sum > TargetSum, Move Right pointer one step backward. (As the array is sorted, moving the Left pointer will increase the sum)
# If the Sum < TargetSum, Move Left pointer one step forward. (As the array is sorted, moving the Right pointer will reduce the sum even more)
# If the Sum == TargetSum, return [array[Left], array[Right]]
# Continue this until Left < Right
# If left == right, break the loop and return []
##############################

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


