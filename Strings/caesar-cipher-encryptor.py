"""
 Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that
 returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.
 Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by 1 returns the letter a.

 Sample Input:
 string = "xyz"
 key = 2

 Sample Output:
 "zab"
"""

# Using alphabets dictionary
# Time: O(n) | Space: O(n)
###########################
# Initialize final_string to empty string
# For each character in string
#   get the shifted character --> get_shifted_character(character, key)
#   Append shifted character to final_string
# return final_string
#
# Declare a function --> get_shifted_character(character, key)
#   Initialize alphabets to a dictionary with key as every alphabet and value as integers from 0 to 25
#   Get the index of the current character from the dictionary
#   Get the shifted index of the character --> get_shift_index(char_index, key)
#   Get the alphabet key whose value is equal to the shifted index value
#   return the shifted alphabet
#
# Declare a function --> get_shift_index(current_index, key)
#   Get the shift index by adding the key to current index and apply modulo with 26
#   return the shift index
###########################


def caesarCipherEncryptor(string, key):
    final_string = ""
    for character in string:
        shifted_character = get_shifted_character(character, key)
        final_string += shifted_character
    return final_string


def get_shifted_character(character, key):
    alphabets = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    char_index = alphabets[character]
    shifted_index = get_shift_index(char_index, key)
    return list(alphabets.keys())[list(alphabets.values()).index(shifted_index)]


def get_shift_index(current_index, key):
    next_index = (current_index + key) % 26
    return next_index


# Using alphabets list
# Time: O(n) | Space: O(n)
##########################
# Initialize new_letters to empty list
# Initialize new_key = key % 26
# Initialize alphabets to list of alphabet characters
# Loop through every character in the string
#   Get the shifted character and append it to new_letters list --> get_new_letter(letter, new_key, alphabets)
# Join all the characters in the new_letters list and return the string
#
# Declare a function --> get_new_letter(letter, key, alphabets)
#   Get the index of the character in the alphabets list
#   Set shifted_index to character index + key
#   Get the new character at shifted_index from alphabets list
#   return new character
##########################


def caesarCipherEncryptor(string, key):
    new_letters = []
    new_key = key % 26
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabets))
    return "".join(new_letters)


def get_new_letter(letter, key, alphabets):
    letter_index = alphabets.index(letter)
    shifted_index = letter_index + key
    new_character = alphabets[shifted_index % 26]
    return new_character


# Using unicode values
# Time: O(n) | Space: O(n)
##########################
# This method uses the unicode values of alphabets
# a -> 96
# z -> 122
#
# Initialize new_letters to empty list
# Initialize new_key = key % 26 (If the key is very large, modulo operation will reduce the value when its added with 96)
# For every character in string
#   get the new letter and append it to new_letters array --> get_new_letter(letter, new_key)
# join the characters in list and return the string
#
# Declare a function --> get_new_letter(letter, key)
#   Use ord() function to get the unicode value and add it with the key. Set this as new_letter_code
#   If the new_letter_code <= 122
#       use chr() function to get the character from unicode value and return the character
#   else
#       Apply mod 122 to new_letter_code and add it with 96. This will return the unicode value of the new character
#       Use chr() function to get the character from unicode value and return the character
##########################


def caesarCipherEncryptor(string, key):
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))
    return "".join(new_letters)


def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    if new_letter_code <= 122:
        return chr(new_letter_code)
    else:
        return chr(96 + new_letter_code % 122)
