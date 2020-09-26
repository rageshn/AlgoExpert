"""
Write a function that takes in an n x m two-dimensional array (that can be square shaped when n = m)
and returns one dimensional array of all array's elements in spiral order.
Spiral order starts at the top left corner of the two-dimensional array, goes to the right and proceeds in a spiral pattern
all the way until every element has been visited.
"""


# Iterative approach
# Time: O(N) | Space: O(1)
############################
# Initialize four pointers for starr row, start column, end row, end column
# Initialize result as empty array
# Loop the array by perimeter
# Loop the array until start row <= end row and start column <= end column
#     Traverse between start column and end column (on start row)
#         Add the elements to result array
#     Traverse between start row and end row (on end column)
#         Add the elements to result array
#     Traverse between end column and start column (on end row)
#         Add elements to result array
#     Traverse between end row and start row (on start column)
#         Add elements to result array
#
#     Increment start row and start column
#     Decrement end row and end column
#
# return result
############################


def spiralTraverse(array):
    result = []
    start_row = 0
    end_row = len(array) - 1
    start_col = 0
    end_col = len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result


# Recursive approach
# Time: O(N) | Space: O(N)
###########################
# Initialize results as empty array
# Initialize four pointers for starr row, start column, end row, end column
# Call traversePerimeter function by passing the required parameters
# return results
#
# Traverse Perimeter(input array, start row, start column, end row, end column, results):
#     If start row > end row or start column > end column, return from function
#     Traverse from start column to end column (on start row)
#         Add elements to results array
#     Traverse from start row to end row (on end column)
#         Add elements to results array
#     Traverse between end column and start column (on end row)
#         Add elements to results array
#     Traverse between end row and start row (on start column)
#         Add elements to results array
#
#     Update start row, start column, end row, end column parameters
#     Recursively call Traverse Perimeter function with updated parameters.
###########################

def spiralTraverse(array):
    # Write your code here.
    results = []
    traversePerimeter(array, 0, 0, len(array) - 1, len(array[0]) - 1, results)
    return results


def traversePerimeter(array, start_row, start_col, end_row, end_col, results):
    if start_row > end_row or start_col > end_col:
        return results
    for col in range(start_col, end_col + 1):
        results.append(array[start_row][col])
    for row in range(start_row + 1, end_row + 1):
        results.append(array[row][end_col])
    for col in reversed(range(start_col, end_col)):
        if start_row == end_row:
            break
        results.append(array[end_row][col])
    for row in reversed(range(start_row + 1, end_row)):
        if start_col == end_col:
            break
        results.append(array[row][start_col])

    traversePerimeter(array, start_row + 1, start_col + 1, end_row - 1, end_col - 1, results)
