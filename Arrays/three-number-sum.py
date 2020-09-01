"""
Write a function that takes a non-empty array of distinct integers and an integer representing a target sum.
The function should find all the triplets in the array that sum up to the target sum and return the two-dimensional array of all these triplets.
The numbers in each triplet should be ordered in ascending order and the triplets themselves should be ordered in ascending
order with respect to the numbers they hold.
If no three numbers sum up to the target sum, then the function should return an empty array.
"""

# Sort approach
# Time: O(n^2) | Space: O(n)
#############################
# Initialize a list for storing triplets
# Sort the array
# Loop through the elements in the array
#     Initialize left = i + 1, right = len(array) - 2. i -> Current index
#         Set currentSum as array[i] + array[left] + array[right]
#         If currentSum == TargetSum, then append [array[i], array[left], array[right]] to global list of triplets
#         If currentSum < TargetSum, Increment left by 1
#         If currentSum > TargetSum, Decrement right by 1
#         Repeat this till left < right
# After the loop, return the global list of triplets
#############################


def threeNumberSum(array, targetSum):
    list_of_triplets = []
    array.sort()
    for i in range(0, len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                list_of_triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return list_of_triplets
