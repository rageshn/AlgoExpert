"""
 Write a function that takes in an array of words and returns the smallest array of characters needed to form all the words.
 The characters don't need to be in any particular order.
 For example, the characters ['y', 'r', 'o', 'u'] are needed to for the words ['your', 'you', 'or', 'yo'].
 Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.
"""

# Using dictionary
# Time: O(n * l) | Space: O(c)
# l - length of the longest word
# c - number of unique characters across words
###############################
# This approach maintains the global dictionary to maintain the maximum frequency of characters.
# We also use a secondary dictionary to maintain the character frequency in each word.
#
# Initialize max_freq = empty dictionary
# Initialize final_result = empty list
# Loop through each word in words list
#   Initialize char_count = empty dictionary
#   Loop through each letter in the word
#       If the letter is available in the char_count
#           Increment the value by 1
#       else
#           Initialize the key as letter and value as 1
#   Loop through every character key in char_count
#       If the character is available in max_freq
#           Get the maximum value between current character frequency and the frequency in max_freq
#           Set the value against the character key as the maximum value
# For every letter in max_freq
#   Append the character (max value number of times) to final_result list
# return final_result
###############################


def minimumCharactersForWords(words):
    max_freq = {}
    final_result = []
    for word in words:
        char_count = {}
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in char_count:
            if char in max_freq:
                max_freq[char] = max(char_count[char], max_freq[char])
            else:
                max_freq[char] = char_count[char]

    for char in max_freq:
        freq = max_freq[char]
        final_result.extend([char] * freq)
    return final_result
