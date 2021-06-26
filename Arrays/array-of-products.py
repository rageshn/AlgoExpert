"""
 Write a function that takes in a non-empty array of integers and returns an array of same length, where
 each element in the output array is equal to the product of every other number in the input array.
 In other words, the value at output[i] is equal to the product of every other number in the input array other than
 output[i].
 Note that you're expected to solve this problem without using division.
"""

# Bruteforce approach
# Time: O(n^2) | Space: O(n)
##############################
# Initialize products as array of 1's
# For every element i in the array
#   Set the product_val to 1
#   For every element j in the array
#       if i != J
#           Set product_val = product_val * array[j]
#   Set product[i] as product_val
# return products
##############################


def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct = runningProduct * array[j]
        products[i] = runningProduct
    return products


# Computing Left and Right Products
# Time: O(n^2) | Space: O(n)
#############################
# Initialize result as empty array
# Loop through the array
#   Initialize right_product variable to 1
#   Loop through the array elements from index + 1 to end of array
#       Set right_product = right_product * element
#   Initialize left_product to 1
#   Loop through the array elements from 0 to index - 1
#       Set left_product = left_product * element
#   append (left_product * right_product) to result array
# return result
#############################


def arrayOfProducts(array):
    result = []
    for index in range(0, len(array)):
        right_product = 1
        for val in array[index + 1:]:
            right_product = right_product * val
        left_product = 1
        for val in array[:index]:
            left_product = left_product * val
        result.append(left_product * right_product)
    return result


# Computing Left and Right Products
# Time: O(n) | Space: O(n)
###########################
# Initialize product as array of 1's
# Initialize left_products as array of 1's
# Initialize right_products as array of 1's
# Initialize left_product to 1
# Loop though the array
#   Set left_products[i] to left_product
#   Set left_product = left_product * array[i]
# Initialize right_product to 1
# Loop through the array in reverse
#   Set the right_products[i] to right_product
#   Set right_product = right_product * array[i]
# Loop through the array
#   Set product[i] = left_products[i] * right_products[i]
# return products
############################


def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    left_products = [1 for _ in range(len(array))]
    right_products = [1 for _ in range(len(array))]

    left_product = 1
    for i in range(len(array)):
        left_products[i] = left_product
        left_product = left_product * array[i]

    right_product = 1
    for i in reversed(range(len(array))):
        right_products[i] = right_product
        right_product = right_product * array[i]

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    return products


# Computing Left and Right Products
# Time : O(n) | Space : O(n)
###############################
# Initialize products as array of 1's
# Initialize left_product to 1
# Loop through the array
#   Set products[i] = left_product
#   Set left_product = left_product * array[i]
# Initialize right_product to 1
# Loop through the array in reverse
#   Set products[i] = products[i] * right_product
#   right_product = right_product * array[i]
# return products
################################


def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    left_product = 1
    for i in range(len(array)):
        products[i] = left_product
        left_product = left_product * array[i]

    right_product = 1
    for i in reversed(range(len(array))):
        products[i] = products[i] * right_product
        right_product = right_product * array[i]

    return products


