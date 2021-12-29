"""
 Write a function that takes in an array of strings and groups anagrams together.
 Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and
 "iceman" are anagrams; Similarly "foo" and "ofo" are anagrams.
 Your function should return a list of anagram groups in no particular order.
"""


# Using sort
# Time: (w * n * log(n)) | Space: O(w * n)
##########################################
# This approach sorts every word in the list and adds it to a dictionary.
# For all anagrams, the sorted word will always be the same.
# For every word, sort it and store it in the dictionary. If the sorted result is already available in the dictionary,
# then it's an anagram. So append the current word to the value.
#
# Initialize a dictionary for storing the anagrams -> words_map
# Loop through every word
#   Sort the word --> sorted_word
#   If the sorted_word is not in words_map (new word)
#       Insert the words as a list in the dictionary value
#   else
#       Append the word to dictionary value
# Loop through dictionary's values and return them as list of lists
##########################################


def groupAnagrams(words):
    words_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in words_map:
            words_map[sorted_word] = [word]
        else:
            words_map[sorted_word].append(word)

    result = []
    for key, value in words_map.items():
        result.append(value)

    return result


# Using word as encoded string
# Time: O(w * n) | Space: O(w * n)
##################################
# This approach uses encoded string as key to map the anagrams
# Encoded String - Character array with number of times the letter has repeated in the word.
# For anagrams, the encoded strings will be the same. So they can be mapped to same key in dictionary.
#
# Initialize a dictionary which holds the list of anagrams --> words_map
# Create a list which holds all the alphabets --> alphabets
# Loop through every word
#   Get the encoded key of the word --> get_encoded_key(word, alphabets)
#   Convert the encoded key to string --> key_str
#   Append/Add word to words_map with key_str as the key
# Initialize a list to hold the result
# Loop through the words_map
#   Append all anagrams list to result
# return result
#
# Declare a function --> get_encoded_key(word, alphabets)
#   Initialize chars as list of length 26 which holds 0 (This maintains the letters count)
#   For every character in the word
#       Get the character index from alphabets
#       Increment the value at the character index in the chars array by 1
#   return chars
##################################


def groupAnagrams(words):
    words_map = {}
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    for word in words:
        encoded_key = get_encoded_key(word, alphabets)
        key_str = str(encoded_key)
        if key_str in words_map:
            words_map[key_str].append(word)
        else:
            words_map[key_str] = [word]

    result = []
    for key, value in words_map.items():
        result.append(value)
    return result


def get_encoded_key(word, alphabets):
    chars = [0] * 26
    for char in word:
        char_index = alphabets.index(char)
        chars[char_index] += 1
    return chars
