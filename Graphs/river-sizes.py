"""
 You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
 Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either
 horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.
 Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
 it can be L-shaped.
 Write a function that returns an array of the sizes of all rivers represented in the input matrix.
 The sizes don't need to be in any particular order.
"""

# Using graph traversal approach
# Time: O(width * height) | Space: O(width * height)
####################################################
# Only adjacent 1s will be considered for river and will not consider the diagonal 1s
# Iterate through the matrix, if we reach 1, check for all neighbour nodes (top, left, right, bottom)
# If the adjacent element is unvisited, visit the element and continue for its neighbours
# Use dfs to reach to all connected 1s. Maintain a counter for river size.
#
# Initialize river_sizes to empty array
# Initialize visited to the same size of matrix and set all values to False
# Loop through the rows --> row
#   Loop through the columns --> column
#       If the index at row & column in visited is True
#           continue
#       call traverse_node(row, column, matrix, visited, river_sizes)
# return river_sizes
#
# Declare a function --> traverse_node(row, column, matrix, visited, river_sizes)
#   Initialize current river size to 0
#   Initialize nodes_to_explore as [[row, column]]
#   Loop till there are no elements in nodes_to_explore
#       Pop the element from nodes_to_explore and set it to current_node
#       Get the row & column values from current_node object
#       If the index at row & column in visited is True
#           continue
#       Set the index value at row & column in visited to True
#       If the element at row & column in matrix is 0
#           continue
#       Increment current river size by 1
#       Get all the unvisited neighbours of the current node --> get_unvisited_neighbours(row, column, matrix, visited)
#       Loop through each neighbour
#           Append each neighbour to nodes_to_explore
#   If current river size > 0
#       Append current river size to river_sizes list
#
# Declare a function --> get_unvisited_neighbours(row, column, matrix, visited)
#   Initialize unvisited neighbours to empty list
#   If row > 0 and element at index row - 1 & column in visited is False (If current element has an unvisited top neighbour)
#       Append [row - 1, column] to unvisited neighbours list (Index of top neighbour)
#   If row < len(matrix) - 1 and element at index row + 1 & column in visited is False (If current element has an unvisited bottom neighbour)
#       Append [row + 1, column] to unvisited neighbours list (Index of bottom neighbour)
#   If column > 0 and element at index row & column - 1 in visited is False (If the current element has an unvisited left neighbour)
#       Append [row, column - 1] to unvisited neighbours list (Index of left neighbour)
#   If column < len(matrix[0]) - 1 and element at index row & column + 1 in visited is False (If the current element has an unvisited right neighbour)
#       Append [row, column + 1] to unvisited neighbours list (Index of right neighbour)
#   return unvisited neighbours list
####################################################


def riverSizes(matrix):
    river_sizes = []
    visited = [[False for _ in row] for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if visited[row][column]:
                continue
            traverse_node(row, column, matrix, visited, river_sizes)
    return river_sizes


def traverse_node(row, column, matrix, visited, river_sizes):
    current_river_size = 0
    nodes_to_explore = [[row, column]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        row = current_node[0]
        column = current_node[1]
        if visited[row][column]:
            continue
        visited[row][column] = True
        if matrix[row][column] == 0:
            continue
        current_river_size += 1
        unvisited_neighbours = get_unvisited_neighbours(row, column, matrix, visited)
        for neighbour in unvisited_neighbours:
            nodes_to_explore.append(neighbour)
    if current_river_size > 0:
        river_sizes.append(current_river_size)


def get_unvisited_neighbours(row, column, matrix, visited):
    unvisited_neighbours = []
    if row > 0 and not visited[row - 1][column]:
        unvisited_neighbours.append([row - 1, column])
    if row < len(matrix) - 1 and not visited[row + 1][column]:
        unvisited_neighbours.append([row + 1, column])
    if column > 0 and not visited[row][column - 1]:
        unvisited_neighbours.append([row, column - 1])
    if column < len(matrix[0]) - 1 and not visited[row][column + 1]:
        unvisited_neighbours.append([row, column + 1])
    return unvisited_neighbours


