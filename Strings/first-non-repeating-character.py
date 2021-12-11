"""
 Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the
 string's first non-repeating character.
 The first non-repeating character is the first character in a string that occurs only once.
 If the input string doesn't have any non-repeating characters, your function should return -1.
"""


# Using dictionary
# Time: O(n) | Space: O(1)
##########################
# Initialize character_frequency to a dictionary. This holds the number of times the letter occurs in the string.
# Loop through every letter in the string
#   If the letter is not in character frequency dictionary
#       Add letter as key and value as 1 in the dictionary
#   else
#       Increment value by 1
#
# Loop through every letter in the string
#   Get the letter's frequency from the character_frequency dictionary
#   If the frequency is 1 (This letter occurs only once, and it's the first as we are iterating from the beginning)
#       return the current index
# return -1
##########################


def firstNonRepeatingCharacter(string):
    character_counts = {}
    for index in range(len(string)):
        letter = string[index]
        if letter in character_counts:
            character_counts[letter] += 1
        else:
            character_counts[letter] = 1

    for index in range(len(string)):
        letter = string[index]
        char_freq = character_counts[letter]
        if char_freq == 1:
            return index

    return -1
