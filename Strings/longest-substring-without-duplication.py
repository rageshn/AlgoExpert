"""
 Write a function that takes in a string and returns its longest substring without duplicate characters.
 You can assume that there will only be one longest substring without duplication.
"""

# Using sliding window approach
# Time: O(n) | Space: O(n)
##########################
# This uses sliding window approach to get the substring. Starting from 0th index, the window moves along the string.
# Left index start from 0, and the right index moves from 0 to the right till we reach a duplicate character.
# It maintains a list which hold all the characters right pointer sees. If we reach a character already visited (duplicate)
# the letter at left index will be removed from list and left index will be incremented by 1 till there are no duplicates.
# Another list is used to maintain the largest substring.
#
# Initialize substring = empty list
# Initialize left pointer  = 0
# Initialize final_result = empty list
# Loop through index in the string --> right
#   Loop till the character at right index already available in substring
#       Remove the character at left index from substring
#       Increment left index by 1
#   Append the character at right index to substring
#   If the substring length > final_result length
#       Assign final_result = substring (use list copy/cloning and not direct assign)
#   return final_result as string
##########################


def longestSubstringWithoutDuplication(string):
    substring = []
    left = 0
    final_result = []

    for right in range(len(string)):
        while string[right] in substring:
            substring.remove(string[left])
            left += 1
        substring.append(string[right])

        if len(substring) > len(final_result):
            final_result = substring[:]

    return "".join(final_result)


# Using dictionary to hold the character's last seen index
# Time: O(n) | Space: O(min(n, l))
# l - length of the longest substring without duplicates
##################################
# This uses a dictionary to hold the character's last seen index.
# Whenever a new character is encountered, it will be added in dictionary with its index.
# When a letter already exists in dictionary, update the start index with the maximum of current start index and
# the position we last saw the current letter. This is to check whether the current substring ending at the
# current letter is longer than the current longest substring. After this, update the index of character in the dictionary.
#
# Initialize last_seen as empty dictionary.
# Initialize longest = indices of start index & end index of substring as list
# Initialize start_index = 0
# Iterate through the string
#   If the character is already in last_seen
#       Set start_index = max(start_index, last_seen[char] + 1)
#   If the length of current longest substring < current substring ending at current letter
#       Set longest = [start_index, current index + 1]
#   Update the index of current letter in last_seen
# return the substring between longest[0] & longest[1]
##################################


def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    start_index = 0
    for index, char in enumerate(string):
        if char in lastSeen:
            start_index = max(start_index, lastSeen[char] + 1)
        if longest[1] - longest[0] < index + 1 - start_index:
            longest = [start_index, index + 1]
        lastSeen[char] = index
    return string[longest[0]: longest[1]]
