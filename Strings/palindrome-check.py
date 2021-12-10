"""
 Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
 A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
"""


# Using two pointers
# Time: O(n) | Space: O(1)
##########################
# Initialize two pointers start and end
# Set start to 0 and end to array length
# Loop till start is less than end
#   If the characters at start and end index are not equal
#       return False
#   Increment start by 1
#   Decrement end by 1
# return True
##########################


def isPalindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
