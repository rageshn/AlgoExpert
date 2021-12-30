"""
 Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has
 these words in reverse order. For example, given the string "tim is great", your function should return "great is tim".
 For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be
 separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original
 string. For example, given the string "whitespaces    4" you would be expected to return "4    whitespaces".
 Note that you're not allowed to use any built-in split or reverse methods. However, you are allowed to use join method.
 Also note that the input string isn't guaranteed to always contain words.
"""

# Reversing entire string and then reversing individual words
# Time: O(n) | Space: O(n)
##########################
# This method reverses the entire string and then reverses individual words in the reversed string.
#
# Initialize index  = last index of string
# Initialize reversed_str = empty string
# Loop till index >= 0
#   Append character at index to reversed_str
#   Decrement index by 1
# Initialize index = 0
# Loop till index < length of reversed_str
#   If the character in reversed_str at index is space (Loop continues till we hit a valid character)
#       Increment index by 1
#       continue
#   Get the word's end index --> get_word_end_index(reversed_str, index)
#   Reverse the characters in the word and assign it back to reversed_str --> swap_chars(reversed_str, index, word_end_index)
# return reversed_str
#
# Declare a function --> get_word_end_index(string, index)
#   This function is called when we reach a valid character
#   This returns the current word's end index based on the start index provided
#   Assign end_index = start index
#   From start_index loop till an empty space is encountered or the end of string
#       Increment the end_index by 1
#   return end_index
#
# Declare a function --> swap_chars(string, start, end)
#   Assign string = convert string to list of characters
#   Loop till start < end
#       Swap the characters in string at start & end indices
#       Increment start by 1
#       Decrement end by 1
#   return string
##########################


def reverseWordsInString(string):
    index = len(string) - 1
    reversed_str = ""
    while index >= 0:
        reversed_str += string[index]
        index -= 1

    index = 0
    while index < len(reversed_str):
        if reversed_str[index] == " ":
            index += 1
            continue

        word_end_index = get_word_end_index(reversed_str, index)
        reversed_str = swap_chars(reversed_str, index, word_end_index)
        index = word_end_index + 1
    return reversed_str


def swap_chars(string, start, end):
    string = list(string)
    while start < end:
        temp = string[start]
        string[start] = string[end]
        string[end] = temp

        start += 1
        end -= 1
    return "".join(string)


def get_word_end_index(string, start_index):
    end_index = start_index
    while end_index < len(string) and string[end_index] != " ":
        end_index += 1
    return end_index - 1
