"""
 Write a function that, given a string, returns its longest palindromic substring.
 A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
 You can assume that there will only be one longest palindromic substring.
"""


# Traversing outwards approach
# Time: O(n^2) | Space: O(n)
############################
# This approach traverse through every character and expand outwards to check whether we are having a palindrome or not.
# The palindromes can have even or odd length characters.
# The palindrome is checked with previous and next character to current index (odd palindromes)
# The current and next index is checked for verifying even palindromes.
# Maintain the max palindrome with a temporary variable.
#
# Initialize final_sub_sequence as empty string
# Loop through each character in the string
#   Get the previous and next index of current character
#   Get the palindrome of odd length --> traverse_outwards_odd(index, before, after, string, string[index])
#   For odd length palindromes, the centre character must be a character in the string
#   Get the palindrome of even length --> traverse_outwards_even(index, index + 1, string, "")
#   For even length palindromes, the centre character must be an empty string
#   Get the palindrome sequence which has maximum length
#   If the length is greater than the length of final_sub_sequence
#       Set final_sub_sequence = result
#
# Declare a function --> traverse_outwards_even(i, j, string, subsequence)
#   If the indices (i, j) are outside the string limits
#       return the subsequence
#   If the character at current index (i) is not equal to character at next index (j)
#       return the subsequence
#   Loop till the character at current index (i) is same as next index (j)
#       Set subsequence = Append current index with subsequence and next index
#       recursively call traverse_outwards_even by passing current index - 1, next index + 1. (Expand outwards)
#
# Declare a function --> traverse_outwards_odd(centre_index, i, j, string, subsequence)
#   If the indices (i, j) are outside string limits
#       return the subsequence
#   If the character at i is not equal to character at j
#       return subsequence
#   Loop till the character at i is equal to character at j
#       Set subsequence = Append character at i, subsequence, character at j
#       recursively call traverse_outwards_odd by passing i 1, j + 1. (Expand outwards)
############################


def longestPalindromicSubstring(string):
    final_sub_seq = ""
    for index in range(len(string)):
        before = index - 1
        after = index + 1
        odd_result = traverse_outwards_odd(index, before, after, string, string[index])
        even_result = traverse_outwards_even(index, index + 1, string, "")
        result = odd_result if len(odd_result) > len(even_result) else even_result
        if len(result) > len(final_sub_seq):
            final_sub_seq = result

    return final_sub_seq


def traverse_outwards_even(i, j, string, subsequence):
    if i < 0 or j > len(string) - 1:
        return subsequence

    if string[i] != string[j]:
        return subsequence

    while string[i] == string[j]:
        subsequence = string[i] + subsequence + string[j]
        return traverse_outwards_even(i - 1, j + 1, string, subsequence)


def traverse_outwards_odd(centre_index, i, j, string, subsequence):
    if i < 0 or j > len(string) - 1:
        return subsequence

    if string[i] != string[j]:
        return subsequence

    while string[i] == string[j]:
        subsequence = string[i] + subsequence + string[j]
        return traverse_outwards_odd(centre_index, i - 1, j + 1, string, subsequence)


# Traversing outwards (using index)
# Time: O(n^2) | Space: O(n)
############################
# Same approach, but it maintains the palindrome indices instead of actual palindrome.
############################


def longestPalindromicSubstring(string):
    current_longest = [0, 1]
    for index in range(1, len(string)):
        odd_palindrome = get_longest_palindrome(string, index - 1, index + 1)
        even_palindrome = get_longest_palindrome(string, index - 1, index)
        longest = max(odd_palindrome, even_palindrome, key=lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key=lambda x: x[1] - x[0])
    return string[current_longest[0]: current_longest[1]]


def get_longest_palindrome(string, left_index, right_index):
    while left_index >= 0 and right_index < len(string):
        if string[left_index] != string[right_index]:
            break
        left_index -= 1
        right_index += 1
    return [left_index + 1, right_index]
