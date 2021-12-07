"""
 Write a function that takes in an integer matrix of potentially unequal height and width and returns the
 minimum number of passes required to convert all negative integers in the matrix to positive integers.
 A negative integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements
 is positive. An adjacent element is an element that is to the left, to the right, above, or below the current element
 in the matrix. Converting a negative to a positive simply involves multiplying it by -1.
 Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to a positive.
 A single pass through the matrix involves converting all the negative integers that can be converted at a
 particular point in time.
 For example,consider the following input matrix:
 [
  [0, -2, -1],
  [-5, 2, 0],
  [-6, -2, 0],
 ]
 After a first pass, only 3 values can be converted to positives:
 [
  [0, 2, -1],
  [5, 2, 0],
  [-6, 2, 0],
 ]
 After a second pass, the remaining negative values can all be converted to positives:
 [
  [0, 2, 1],
  [5, 2, 0],
  [6, 2, 0],
 ]
"""


# Using temporary queue to hold positive values
# Time: O(width * height) | Space: O(width * height)
####################################################
# This approach first gets all the positive value's index and append it to a queue
# For each index in the queue, get all adjacent positions. If the position has a negative value, its updated to
# positive (multiply by -1) and added to the next pass queue.
# After this pass, loop the next pass queue and repeat the same process.
# This is repeated until both the queues are empty.
# If the matrix still has a negative value, it means that value cannot be converted to positive value. So we return -1.
# Else we return number of passes -1
#
# Call convert_negatives function with matrix as parameter. This returns the number of passes. --> convert_negatives(matrix)
# If the contains_negatives function return True, then we return -1, else we return number of passes - 1 --> contains_negative(matrix)
#
# Declare a function --> convert_negatives(matrix)
#   Get all the positive positions in the matrix and assign it to next_pass_queue --> get_all_positive_positions(matrix)
#   Initialize number of passes to 0
#   Loop till next_pass_queue is not empty
#       Set current_pass_queue = next_pass_queue
#       Update next_pass_queue to empty list
#       Loop till current_pass_queue is not empty
#           Pop the front element from current_pass_queue as assign it to curr_row, curr_col
#           Get the adjacent positions of curr_row & curr_col in matrix --> get_adjacent_positions(curr_row, curr_col, matrix)
#           For every position in adjacent positions
#               Get row & column from position index
#               Get the value at row, column in matrix
#               If value < 0
#                   Update the value to positive & append [row, column] to next_pass_queue
#       Increment passes by 1
#   return passes
#
# Declare a function --> get_all_positive_positions(matrix)
#   Initialize positive_positions to empty list
#   For ever row in matrix
#       For every column in matrix
#           If the value at row, column > 0
#               Append [row, column] to positive_positions
#   return positive_positions
#
# Declare a function --> get_adjacent_positions(row, column, matrix)
#   Initialize adj_positions as empty list
#   If row > 0
#       Append [row-1, column] to adj_positions
#   If row < len(matrix)
#       Append [row+1, column] to adj_positions
#   If column > 0:
#       Append [row, column-1] to adj_positions
#   If column < len(matrix[0]) - 1
#       Append [row, column+1] to adj_positions
#   return adj_positions
#
# Declare a function --> contains_negative(matrix)
#   For row in matrix
#       For value in row
#           if value < 0
#               return True
#   return False
####################################################


def minimumPassesOfMatrix(matrix):
    total_passes = convert_negatives(matrix)
    return total_passes - 1 if not contains_negative(matrix) else -1


def convert_negatives(matrix):
    next_pass_queue = get_all_positive_positions(matrix)
    passes = 0
    while len(next_pass_queue) > 0:
        current_pass_queue = next_pass_queue
        next_pass_queue = []
        while len(current_pass_queue) > 0:
            curr_row, curr_col = current_pass_queue.pop(0)
            adjacent_positions = get_adjacent_positions(curr_row, curr_col, matrix)
            for position in adjacent_positions:
                row, column = position
                value = matrix[row][column]
                if value < 0:
                    matrix[row][column] *= -1
                    next_pass_queue.append([row, column])
        passes += 1
    return passes


def get_all_positive_positions(matrix):
    positive_positions = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            value = matrix[row][column]
            if value > 0:
                positive_positions.append([row, column])
    return positive_positions


def get_adjacent_positions(row, column, matrix):
    adj_positions = []
    if row > 0:
        adj_positions.append([row - 1, column])
    if row < len(matrix) - 1:
        adj_positions.append([row + 1, column])
    if column > 0:
        adj_positions.append([row, column - 1])
    if column < len(matrix[0]) - 1:
        adj_positions.append([row, column + 1])
    return adj_positions


def contains_negative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False




