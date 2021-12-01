"""
 You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
 The matrix represents a two-toned image, where each 1 represents black and each 0 represents white.
 An island is defined as any number of 1s that are horizontally or vertically adjacent (but not diagonally adjacent)
 and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isn't
 an island if any of those 1s are in the first row, last row, first column, or last column of the input matrix.
 Note that an island can twist. In other words, it doesn't have to be a straight vertical line or a
 straight horizontal line; it can be L-shaped, for example.
 You can think of islands as patches of black that don't touch the border of the two-toned image.
 Write a function that returns a modified version of the input matrix, where all of the islands are removed.
 You remove an island by replacing it with 0.
 Naturally, you're allowed to mutate the input matrix.
"""

# Using DFS
# Time: O(width * height) | Space: O(width * height)
#####################################################
# Loop through the perimeter of the array. If there are any 1, replace it with 2.
# Use DFS to visit its neighbouring 1 and replace them with 2.
# After this, all the 1 which are not updated to 2 are valid islands. So, replace all 1 to 0 and 2 to 1.
#
# Initialize visited as 2D array with values set to False
# Loop through every row and column index
#   If the current row & column index is in array's perimeter (row/column == 0 or row/column == len(matrix)/len(matrix[row])
#       If the element at row and column index is 1 and not visited
#           Set the current value in matrix to 2
#           Call dfs to reach all the neighbouring 1 and update them to 2. --> dfs(row, column, matrix, visited)
#       else (If current element is 0)
#           Update the current row, column index in visited to True
#
# Loop through the row and column index
#   If current value in matrix is 1
#       Replace the current value to 0 (remove valid islands)
#   else if current value is 2
#       replace the current value to 1
#
# return matrix
#
# Declare a function --> dfs(row, column, matrix, visited)
#   If the row & column is out of matrix boundary or current value is 0
#       return None
#   If the current element at row, column is not visited
#       Update the current index in visited to True
#       Call dfs on elements to right, left, up and down
#       dfs(row + 1, column, matrix, visited) -> down
#       dfs(row - 1, column, matrix, visited) -> up
#       dfs(row, column - 1, matrix, visited) -> left
#       dfs(row, column + 1, matrix, visited) -> right
#####################################################


def removeIslands(matrix):
    visited = [[False for _ in row] for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row == 0 or row == len(matrix) - 1 or column == 0 or column == len(matrix[row]) - 1:
                if matrix[row][column] == 1 and not visited[row][column]:
                    matrix[row][column] = 2
                    dfs(row, column, matrix, visited)
                else:
                    visited[row][column] = True

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                matrix[row][column] = 0
            elif matrix[row][column] == 2:
                matrix[row][column] = 1
    return matrix


def dfs(row, column, matrix, visited):
    if row < 0 or row > len(matrix) - 1 or column < 0 or column > len(matrix[row]) - 1 or matrix[row][column] == 0:
        return None
    if not visited[row][column]:
        visited[row][column] = True
        matrix[row][column] = 2
        dfs(row + 1, column, matrix, visited)
        dfs(row - 1, column, matrix, visited)
        dfs(row, column + 1, matrix, visited)
        dfs(row, column - 1, matrix, visited)


# Algo Expert Solution
########################

def removeIslands(matrix):
    ones_connected_to_perimeter = [[False for _ in matrix[0]] for row in matrix]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            row_is_in_perimeter = row == 0 or row == len(matrix) - 1
            column_is_in_perimeter = column == 0 or column == len(matrix[row]) - 1
            is_perimeter = row_is_in_perimeter or column_is_in_perimeter
            if not is_perimeter:
                continue
            if matrix[row][column] != 1:
                continue
            find_ones_connected_to_perimeter(matrix, row, column, ones_connected_to_perimeter)

    for row in range(1, len(matrix) - 1):
        for column in range(1, len(matrix[row]) - 1):
            if ones_connected_to_perimeter[row][column]:
                continue
            matrix[row][column] = 0
    return matrix


def find_ones_connected_to_perimeter(matrix, start_row, start_column, ones_connected_to_perimeter):
    stack = [(start_row, start_column)]
    while len(stack) > 0:
        current_position = stack.pop()
        current_row, current_column = current_position
        already_visited = ones_connected_to_perimeter[current_row][current_column]
        if already_visited:
            continue
        ones_connected_to_perimeter[current_row][current_column] = True
        neighbours = get_neighbours(matrix, current_row, current_column)
        for neighbour in neighbours:
            row, column = neighbour
            if matrix[row][column] != 1:
                continue
            stack.append(neighbour)


def get_neighbours(matrix, row, column):
    neighbours = []
    num_rows = len(matrix)
    num_column = len(matrix[row])

    if row - 1 > 0:
        neighbours.append((row - 1, column))
    if row + 1 < num_rows:
        neighbours.append((row + 1, column))
    if column - 1 >= 0:
        neighbours.append((row, column - 1))
    if column + 1 < num_column:
        neighbours.append((row, column + 1))
    return neighbours