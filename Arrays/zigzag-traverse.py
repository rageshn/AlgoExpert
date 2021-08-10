"""
 Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m)
 and returns a one-dimensional array of all the array's elements in zigzag order.
 Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element,
 and proceeds in a zigzag pattern all the way to the bottom right corner.
"""


# Naive approach
# Time: O(n) | Space: O(n)
###########################
# Initialize height, width of the array
# Initialize result as empty list
# Set initial row and column values to 0
# Initialize a boolean variable (going_down) to represent whether we are traversing down or up
# Loop will we don't move out of array index --> isOutOfBounds(row, column, height, width)
#   Append the current element to result array
#   If going_down:
#       If we are on left most column or on last row (column == 0 or row == height)
#           going_down = False (as we cannot traverse down)
#           If we are on last row (row == height)
#               Increment column by 1 (move right)
#           else
#               Increment row by 1 (move down)
#       else
#           Increment row by 1 and decrement column by 1 (move diagonally down to left)
#   else
#       If we are on first row or right most column
#           going_down = True
#           If we are on last column (column == width)
#               Increment row by 1 (Move down)
#           else
#               Increment column by 1 (Move right)
#       else
#           Decrement row by 1 and Increment column by 1 (Move diagonally up to right)
# return result
#
# Declare a function --> isOutOfBounds(row, column, height, width)
#   This method returns whether we are moving out of the array size
#   return row < 0 or column < 0 or row > height or column > width
###########################


def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, column = 0, 0
    going_down = True
    while not isOutOfBounds(row, column, height, width):
        result.append(array[row][column])
        if going_down:
            if column == 0 or row == height:
                going_down = False
                if row == height:
                    column += 1
                else:
                    row += 1
            else:
                row += 1
                column -= 1
        else:
            if row == 0 or column == width:
                going_down = True
                if column == width:
                    row += 1
                else:
                    column += 1
            else:
                row -= 1
                column += 1
    return result


def isOutOfBounds(row, column, height, width):
    return row < 0 or column < 0 or row > height or column > width
