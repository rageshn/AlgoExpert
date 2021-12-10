"""
 Write a function that takes in a non-empty string and returns its run-length encoding.
 From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a
 single data value and count, rather than as the original run." For this problem, a run of data is any sequence of
 consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".
 To make things more complicated, however, the input string can contain all sorts of special characters, including numbers.
 And since encoded data must be decodable, this means that we can't naively run-length-encode long runs.
 For example, the run "AAAAAAAAAAAA" (12 A's) can't naively be encoded as "12A", since this string can be decoded as
 either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion;
 the aforementioned run should be encoded as "9A3A".
"""


# Using run length variable and additional characters array
# Time: O(n) | Space: O(n)
###########################
# This approach maintains the run length for every character. If the consecutive characters are same, run length is
# incremented by 1.
# If the run length is > 9, then it will split the run lengths with 9 and additional lengths to characters list.
# If the current character is different from previous character, the run length for previous character will be appended
# to the characters list
# The main edge case in this problem is handling the last character in the string. This character will not be appended to
# the characters list as are appending the run lengths and characters at previous index. So, the last character & its
# run lengths explicitly after the loop.
#
# Initialize run_length = 1
# Initialize characters as empty list
# If the string length < 2
#   return 1 + character
# Loop through the string from 1st index till end
#   If the character at current index == character at previous index
#       Increment run_length by 1
#       If run_length > 9:
#           Append 9 to characters list
#           Append character at previous index to characters list
#           Reset run_length back to 1
#   else:
#       Append run_length to characters list
#       Append character at previous index to characters list
#       Reset run_length back to 1
#
# Append the run_length to characters list [Last element must be handled explicitly]
# Append the character at the last index to characters list
# Append all elements in the characters list and return the string
###########################


def runLengthEncoding(string):
    run_length = 1
    characters = []
    if len(string) < 2:
        return "1" + string[0]

    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            run_length += 1
            if run_length > 9:
                characters.append(str(9))
                characters.append(string[index - 1])
                run_length = 1
        else:
            characters.append(str(run_length))
            characters.append(string[index - 1])
            run_length = 1

    characters.append(str(run_length))
    characters.append(string[-1])

    return "".join(characters)


# Below method uses the same approach except for the condition check


def runLengthEncoding(string):
    encoded_characters = []
    current_run_length = 1

    for index in range(1, len(string)):
        current_character = string[index]
        prev_character = string[index - 1]

        if current_character != prev_character or current_run_length == 9:
            encoded_characters.append(str(current_run_length))
            encoded_characters.append(prev_character)
            current_run_length = 0

        current_run_length += 1

    encoded_characters.append(str(current_run_length))
    encoded_characters.append(string[-1])
    return "".join(encoded_characters)
