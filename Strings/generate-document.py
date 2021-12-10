"""
 You're given a string of available characters and a string representing a document that you need to generate.
 Write a function that determines if you can generate the document using the available characters. If you can generate
 the document, your function should return true; otherwise it should return false.
 You're only able to generate the document if the frequency of unique characters in the characters string is
 greater than or equal to the frequency of unique characters in the document string. For example, if you're given
 characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one 'c'.
 The document that you need to create may contain any characters, including special characters, capital letters,
 numbers, and spaces.
 Note: you can always generate the empty string ("").
"""


# Brute force approach
# Time: O(m * (n + m)) | Space: O(1)
# n - Number of characters
# m - Length of the document
##################################
# This approach checks every character frequency in characters list against the character frequency in document.
#
# Loop through every character in document
#   Get the frequency of the current character in the document         --> count_character_frequency(character, document)
#   Get the frequency of the current character in the characters list  --> count_character_frequency(character, characters)
#   If the character frequency in document > character frequency in characters list
#       return False
# return True
#
# Declare a function --> count_character_frequency(character, target)
#   Initialize frequency to 0
#   For each letter in target
#       If current letter == character
#           Increment frequency by 1
#   return frequency
##################################

def generateDocument(characters, document):
    for character in document:
        document_frequency = count_character_frequency(character, document)
        characters_frequency = count_character_frequency(character, characters)
        if document_frequency > characters_frequency:
            return False
    return True


def count_character_frequency(character, target):
    frequency = 0
    for letter in target:
        if letter == character:
            frequency += 1
    return frequency

# Using set
# Time: O(c * (n + m)) | Space: O(c)
# c - Number of unique characters in the document
# n - Number of characters
# m - Length of the document
#####################################
# This approach uses a set to check whether the character is already counted or not
#####################################


def generateDocument(characters, document):
    already_counted = set()
    for character in document:
        if character in already_counted:
            continue

        document_frequency = count_character_frequency(character, document)
        characters_frequency = count_character_frequency(character, characters)
        if document_frequency > characters_frequency:
            return False
        already_counted.add(character)
    return True


def count_character_frequency(character, target):
    frequency = 0
    for letter in target:
        if letter == character:
            frequency += 1
    return frequency


# Using dictionary
# Time: O(n + m) | Space: O(c)
##############################
# Initialize characters_map to a dictionary
# Loop through each character in characters list
#   Add each character to characters_map if not already available
#   Else increment the value by 1
# For every letter in the document
#   If letter is not available in characters_map
#       return False
#   else
#       If the value in characters_map > 0
#           Decrement the value by 1. (This means that we used this character in the document)
#       else
#           return False (If the value is -1, then document has one extra letter than in characters)
# return True
##############################


def generateDocument(characters, document):
    characters_map = {}
    for character in characters:
        if character in characters_map:
            characters_map[character] += 1
        else:
            characters_map[character] = 1

    for letter in document:
        if letter not in characters_map:
            return False
        else:
            if characters_map[letter] > 0:
                characters_map[letter] -= 1  #
            else:
                return False

    return True
