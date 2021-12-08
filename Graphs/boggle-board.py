"""
 You're given a two-dimensional array (a matrix) of potentially unequal height and width containing letters;
 this matrix represents a boggle board. You're also given a list of words.
 Write a function that returns an array of all the words contained in the boggle board.
 The final words don't need to be in any particular order.
 A word is constructed in the boggle board by connecting adjacent (horizontally, vertically, or diagonally) letters,
 without using any single letter at a given position more than once; while a word can of course have repeated letters,
 those repeated letters must come from different positions in the boggle board in order for the word to be contained in the board.
 Note that two or more words are allowed to overlap and use the same letters in the boggle board.

 Sample Input:
 board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"],
 ]

 words = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]

 Sample Output:
 ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
"""


# Using Trie & DFS
# Time: O(w * h * 8^l) | Space: O(w * h + n*l)
# w - width of the board
# h - height of the board
# l - length of the longest word
# n - number of words
##############################################
# This method uses a Trie data structure to hold the words list. This data structure will be helpful in searching the
# word letter by letter. As we are using a dictionary to hold the letters, the retrieval takes only constant time.
#
# Initialize a Trie object
# Loop the words list and add every word to Trie
# Initialize available_words to empty dictionary. This will hold all the valid words that are available in board
# Initialize visited as a 2D array of dimension same as the board and set all values to False
# Loop through every row
#   Loop through every column in the current row
#       call explore(row, column, board, trie.root, visited, available_words)
# return all keys in available_words dictionary as a list
#
# Declare a function --> explore(row, column, board, trie_node, visited, available_words)
#   This method performs the DFS to all the neighbour nodes and check the characters against the trie created.
#   If the element at row, column is visited
#       skip
#   Get the letter at the current row & column in board
#   If the letter is not in current trie node
#       skip
#   Set the current letter as visited
#   Assign trie_node = trie_node[letter] i.e., this will get the next letter in trie branch
#   Check if "*" in trie_node (We reached the end of the word)
#       Get the word from trie i.e., word = trie_node["*"]
#       Add the word to the available_words dictionary and set the value to True i.e., word is available in board
#   Get the current letter's neighbours from board--> get_neighbours(row, column, board)
#   For every neighbour letter (returns the indices in the form of [row, column])
#       recursively call explore(neighbour row, neighbour column, board, trie_node, visited, available_words)
#   Once the recursive call is completed, again set the current node as un visited.
#
# Declare a function --> get_neighbours(row, column, board)
#   This function returns the indices of the current element's up, right, bottom, top, diagonally top left, diagonally
#   top right, diagonally bottom left, diagonally bottom right
#   This functions returns the 8 [row, column] index in a list
#
# Create a Trie class
#   init()
#       Initialize self.root as empty dictionary
#       Initialize self.end_symbol as "*". This denotes the final word created by the branch
#   add(self, word)
#       Set current as self.root
#       For every letter in the word
#           If the letter is not in current node
#               Set current[letter] as empty dictionary
#           Set current = current[letter]
#       current[self.end_symbol] = word
#
# This class holds the words "HELLO" & "HAPPY" in the below format
#         { H : { E : { L : { L: { 0: { * : HELLO
#                                      }
#                                 }
#                            }
#                      },
#                 A : { P : { P : { Y : { * : HAPPY
#                                          }
#                                   }
#                             }
#                      }
#                }
#         }
#
##############################################


def boggleBoard(board, words):
    words_trie = Trie()
    for word in words:
        words_trie.add(word)
    available_words = {}
    visited = [[False for _ in row] for row in board]
    for row in range(len(board)):
        for column in range(len(board[row])):
            explore(row, column, board, words_trie.root, visited, available_words)
    return list(available_words.keys())


def explore(row, column, board, trie_node, visited, available_words):
    if visited[row][column]:
        return
    letter = board[row][column]
    if letter not in trie_node:
        return
    visited[row][column] = True
    trie_node = trie_node[letter]
    if "*" in trie_node:
        word = trie_node["*"]
        available_words[word] = True
    neighbours = get_neighbours(row, column, board)
    for neighbour in neighbours:
        neighbour_row = neighbour[0]
        neighbour_column = neighbour[1]
        explore(neighbour_row, neighbour_column, board, trie_node, visited, available_words)
    visited[row][column] = False


def get_neighbours(row, column, board):
    neighbours = []
    if row > 0 and column > 0:
        neighbours.append([row - 1, column - 1])  # Diagonally top left
    if row > 0 and column < len(board[0]) - 1:
        neighbours.append([row - 1, column + 1])  # Diagonally top right
    if row < len(board) - 1 and column < len(board[0]) - 1:
        neighbours.append([row + 1, column + 1])  # Diagonally bottom right
    if row < len(board) - 1 and column > 0:
        neighbours.append([row + 1, column - 1])  # Diagonally bottom left
    if row > 0:
        neighbours.append([row - 1, column])  # Top
    if row < len(board) - 1:
        neighbours.append([row + 1, column])  # Bottom
    if column > 0:
        neighbours.append([row, column - 1])  # Left
    if column < len(board[0]) - 1:
        neighbours.append([row, column + 1])  # Right
    return neighbours


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word