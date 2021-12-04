"""
 You're given a list of edges representing an unweighted, directed graph with at least one node. Write a function that
 returns a boolean representing whether the given graph contains a cycle.
 For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex,
 that are connected in a closed chain. A cycle can also be defined as a chain of at least one vertex in which the first
 vertex is the same as the last.
 The given list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph
 is equal to the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order.
 Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list
 that this vertex is connected to. Note that these edges are directed, meaning that you can only travel from a
 particular vertex to its destination, not the other way around (unless the destination vertex itself has an
 outbound edge to the original vertex).
 Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin;
 in other words, it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is
 considered a cycle.
"""


# Using recursive DFS
# Time: O(V+E) | Space: O(V)
############################
# This approach uses DFS to visit the current node and all its neighbouring nodes (out edges) to check if there is any cycle.
# in_stack arrays is to track the back edge. i.e., a cycle exists
#
# Initialize visited and in_stack as two arrays which has len(edges) number of elements which are False
# Loop through each node in tree
#   If the node is not in visited
#       Call dfs function and assign the return value to is_cyclic --> dfs(node, visited, in_stack, edges)
#       If is_cyclic is true
#           return True
# return False
#
# Declare a function --> dfs(node, visited, in_stack, edges)
#   Set the node as visited and in stack
#   Get all the node's neighbours (out going edges)
#   Loop through each neighbour
#       If the neighbour is not visited
#           Recursively call dfs with the neighbour node and assign the return value to is_cyclic
#           If is_cyclic is True
#               return True
#       else
#           If the neighbour is in stack
#               return True
#   After the traversal for the current node & its neighbours are completed, we set the node value in in_stack to False
#   return False
############################


def cycleInGraph(edges):
    visited = [False] * len(edges)
    in_stack = [False] * len(edges)
    for node in range(len(edges)):
        if not visited[node]:
            is_cyclic = dfs(node, visited, in_stack, edges)
            if is_cyclic:
                return True
    return False


def dfs(node, visited, in_stack, edges):
    visited[node] = True
    in_stack[node] = True
    outgoing_edges = get_outgoing_edges(node, edges)
    for out_edge in outgoing_edges:
        if not visited[out_edge]:
            is_cyclic = dfs(out_edge, visited, in_stack, edges)
            if is_cyclic:
                return True
        else:
            if in_stack[out_edge]:
                return True
    in_stack[node] = False
    return False


def get_outgoing_edges(node, edges):
    return edges[node]


# Using colors
# Time: O(V+E) | Space: O(V)
############################
# This approach uses different colors (WHITE, GREY, BLACK)
# WHITE - Unvisited (Undiscovered)
# GREY  - In Stack
# BLACK - Visited
#
# Initialize colors as a list of WHITE (unvisited), with length as the number of edges
# For every node in graph
#   If color of the node is not WHITE (Node is visited or in stack)
#       continue
#   Traverse all child nodes (dfs) and color the nodes --> traverse_and_color(node, edges, colors) and assign it to is_cycle_exists
#   If is_cycle_exists is True
#       return True
# return False
#
# Declare a function --> traverse_and_color(node, edges, colors)
#   Set the node color to GREY  --> Visited & In stack
#   Get all the neighbouring nodes (out edges)
#   Loop through each neighbour node
#       If the neighbour color is GREY (In stack) --> Back edge exists
#           return True
#       If the neighbour color is not WHITE --> Not unvisited i.e., BLACK
#           continue
#       recursively call traverse_and_color function on neighbour node and assign it to is_cycle_exists
#       If is_cycle_exists
#           return True
#   Set the node color to BLACK (unvisited)
#   return False
############################

WHITE, GREY, BLACK = 0, 1, 2


def cycleInGraph(edges):
    colors = [0] * len(edges)
    for node in range(len(edges)):
        if colors[node] != WHITE:
            continue
        is_cycle_exists = traverse_and_color(node, edges, colors)
        if is_cycle_exists:
            return True
    return False


def traverse_and_color(node, edges, colors):
    colors[node] = GREY
    neighbours = get_neighbours(node, edges)
    for neighbour in neighbours:
        if colors[neighbour] == GREY:
            return True
        if colors[neighbour] != WHITE:
            continue
        is_cycle_exists = traverse_and_color(neighbour, edges, colors)
        if is_cycle_exists:
            return True
    colors[node] = BLACK
    return False


def get_neighbours(node, edges):
    return edges[node]