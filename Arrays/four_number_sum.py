"""
 Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
 The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional
 array of all these quadruplets in no particular order.
 If no four numbers sum up to target sum, the function should return an empty array.
"""

# Two sum approach
# Time (Average): O(n^2) | Space: O(n^2)
# Time (Worst): O(n^3) | Space: O(n^2)
###########################################
# Initialize allPairs as empty dictionary
# Initialize quadruplets as empty array
# Loop through array from 1st index to end of array as set to i
#   Loop from i'th index till end of array -> j
#       Set currentSum = array[i] + array[j]
#       Compute diff as difference between targetSum and currentSum
#       if diff in allPairs
#           Loop through each pair in allPairs[diff]
#               Append (pair + [array[i], array[j]]) to quadruplets
#
#   Loop from 0 to ith value -> k
#       Set currentSum = array[i] + array[k]
#       if currentSum not in allPairs
#           Set allPairs[currentSum] = [[array[k], array[i]]]
#       else
#           Append ([array[k], array[i]]) to appPairs[currentSum]
# return quadruplets
###########################################


def fourNumberSum(array, targetSum):
    allPairs = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum
            if diff in allPairs:
                for pair in allPairs[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairs:
                allPairs[currentSum] = [[array[k], array[i]]]
            else:
                allPairs[currentSum].append([array[k], array[i]])
    return quadruplets


