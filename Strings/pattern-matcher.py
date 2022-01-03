"""
 You're given two non-empty strings. The first one is a pattern consisting of only "x" and/or "y"s; the other one
 is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern.
 A string "S0" is said to match a pattern if replacing all "x"s in the pattern with some non-empty substring "S1" of "S0"
 and replacing all "y"s in the pattern with some non-empty substring "S2" of "S0" yields the same string "S0".
 If the input string doesn't match the input pattern, the function should return an empty array; otherwise,
 it should return an array holding the strings "S1" and "S2" that represent "x" and "y" in the normal string, in that order.
 If the pattern doesn't contain any "x" or "y"s, the respective letter should be represented by an empty string in the final array
 that you return.
 You can assume that there will never be more than one pair of strings "S1" and "S2" that appropriately represent "x" and
 "y" in the normal string.
"""

# By getting first position of y and extending along the string
# Time: (n^2 * m) | Space: O(n + m)
####################################
# Generate a new pattern which always starts with x. (If the pattern start with y, then swap all x and y).
# We have to keep track on whether we did this switch or not.
# Count how many times x and y appear in the pattern.
# Example:
#   pattern: xxyxxy
#   string : gogopowerrangergogopowerranger
#   result : ["go", "powerranger"]
# New pattern = [x, x, y, x, x, y]
# occurrence = { "x" : 4, "y" : 2 }
# Start with length of x = 1.
# If len(x) = 1, then the first y position = 2 (i.e., xxy) [
# We should get the starting index of y -> first y positions * length of x (if x = 3, then y index = 2 * 3 = 6)
# With len(x) = 1, we can get the len(y) from len(string). i.e., (len(string) - (len(x) * number of occurrence)) / number of y
# len(y) = (30 - 1 * 4) / 2 = 13 (if len(y) is decimal, then it's invalid, and we continue with next iteration)
# Use the lengths & indices to get the x and y substring from original string
# If x = 1, then x = "g", y = "gopowerranger". Appy these in pattern and check whether it matches with original string.
# If it doesn't match, increment the value of x and repeat the same steps.
# If it matches, check whether we swapped x & y to form the new pattern.
# If it's swapped, return [y, x] else, return [x, y]
#
# If len(x) = 2, then y index = 2 * 2 = 4
# len(y) = (30 - 2 * 4) / 2 = 11
# From len(x), we get x = "go"
# From y index and len(y), we get y = "powerranger"
# Apply these to new pattern and check whether it matches with original string.
# It actually matches, so we return ["go", "powerranger"]
#
#
# check if len(pattern) > len(string)
#   return empty list (invalid)
# Get the new pattern --> get_new_pattern(pattern)
# Check the first letter of original and new pattern. If they are same, then we did not switched x & y. If they are different,
#   then we switched x & y. --> did_switch
# Initialize counts = dictionary with x & y as keys and 0 as values.
# Get the x, y count & first y position --> get_count_and_first_y_pos(new_pattern, counts)
# If there is 'y' in pattern
#   Loop through the string from 1 till end --> length of x
#       Get length of y from len(string) and length of x
#       If y length <= 0, or it has decimal values
#           continue
#       Get the y index
#       Get x by slicing the string with x length
#       Get y by slicing from y index till y length
#       Apply x & y in pattern and get the matching string
#       If the matching string  == original stirng
#           If we switched x & y
#               return [y, x]
#           else
#               return [x, y]
# else
#   Get the length of x = len(string) / number of x
#   Set x = string[:x length]
#   Apply x in pattern and get the matching string
#   If matching string == original string
#       If we switched x & y
#           return ["", x]
#       else
#           return [x, ""]
#
# Declare a function --> get_new_pattern(pattern)
#   Get the pattern_letters as list(patterns)
#   If the first letter is x (if pattern start with x)
#       return pattern_letters
#   else
#       Loop through every letter in pattern_letters
#       If current letter is x
#           Update it to y
#       else
#           Update it to x
#   return pattern_letters
#
# Declare a function --> get_count_and_first_y_pos(pattern, counts)
#   Initialize first_y_pos = Null
#   Loop through every letter in patter
#       Increment the value against the letter in counts dictionary
#       If letter = y and first_y_pos is Null (Seeing y for the first time in pattern)
#           Set first_y_pos = current index
#   return first_y_pos
####################################


def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    new_pattern = get_new_pattern(pattern)
    did_switch = new_pattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    first_y_pos = get_count_and_first_y_pos(new_pattern, counts)
    if counts["y"] != 0:
        for len_of_x in range(1, len(string)):
            len_of_y = (len(string) - len_of_x * counts["x"]) / counts["y"]
            if len_of_y <= 0 or len_of_y % 1 != 0:
                continue
            len_of_y = int(len_of_y)
            y_index = first_y_pos * len_of_x
            x = string[:len_of_x]
            y = string[y_index:y_index + len_of_y]
            matching_string = map(lambda char: x if char == "x" else y, new_pattern)
            if string == "".join(matching_string):
                if did_switch:
                    return [y, x]
                else:
                    return [x, y]
    else:
        len_of_x = len(string) / counts["x"]
        if len_of_x % 1 == 0:
            len_of_x = int(len_of_x)
            x = string[:len_of_x]
            matching_string = map(lambda char: x, new_pattern)
            if string == "".join(matching_string):
                if did_switch:
                    return ["", x]
                else:
                    return [x, ""]
    return []


def get_new_pattern(pattern):
    pattern_letters = list(pattern)
    if pattern[0] == "x":
        return pattern_letters
    else:
        for index in range(len(pattern_letters)):
            if pattern_letters[index] == "x":
                pattern_letters[index] = "y"
            else:
                pattern_letters[index] = "x"
    return pattern_letters


def get_count_and_first_y_pos(pattern, counts):
    first_y_pos = None
    for index, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and first_y_pos is None:
            first_y_pos = index
    return first_y_pos
