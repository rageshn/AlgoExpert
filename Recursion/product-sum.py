"""
 Write a function that takes in a "special" array and returns its product sum.
 A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum
 of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then
 multiplied by their level of depth.
 The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of inner array
 in [[]] is 2; the depth of innermost array in [[[]]] is 3.
 Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of
 [x, [y, [z]]] is x + 2 * (y + 3 * (z)).
"""


# Recursive method
# Time: O(n) | Space: O(d)
# d - depth of the innermost list
##########################
# Initialize prd_sum = 0
# Loop through every element in the array
#   If the element type is list
#       Recursively call productSum by passing the element and incrementing the multiplier by 1, add the result to prd_sum
#   else
#       Add current element to prd_sum
# return prd_sum * multiplier
##########################


def productSum(array, multiplier=1):
    prd_sum = 0
    for element in array:
        if type(element) is list:
            prd_sum += productSum(element, multiplier + 1)
        else:
            prd_sum += element
    return prd_sum * multiplier
