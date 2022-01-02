"""
 Write a function that takes in two strings: a main string and a potential substring of the main string.
 The function should return a version of the main string with every instance of the substring in it wrapped between
 underscores.
 If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores
 relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the
 rightmost substring. If the main string doesn't contain the other string at all, the function should return
 the main string intact.
"""

# By finding substring indices
# Time: O(n + m) | Space: O(n)
##############################
# In this we split the problem to three parts
#   1. Get all substring locations in the string as intervals [start, end]
#   2. Merge all overlapping intervals
#   3. Apply underscores around start and stop indices
#
# Get all substring locations --> get_substring_locations(string, substring)
# Get merged intervals --> get_collapsed_locations(substring_locations)
# Get the underscored string using merged intervals --> get_underscored_string(string, collapsed_locations)
# return underscored string
#
# Declare a function --> get_substring_locations(string, substring)
#   Initialize next_index = 0
#   Initialize substring_length = len(substring)
#   Initialize locations = [] This hold all the locations of substring
#   Loop till next_index is less than length of string
#       Assign next_index = Index of substring, starting from next_index
#       If next_index = -1 (substring is not available)
#           break
#       Append the start and end index of substring as [next_index, next_index + substring length]
#       Increment next_index by 1
#   return locations
#
# Declare a function --> get_collapsed_locations(substring_locations)
#   If the substring_locations is empty
#       return substring_locations
#   Initialize result = [substring_locations[0]] Start with first location in the locations array
#   Initialize previous interval = result[0]
#   Loop through substring_locations array from 1 till the end --> i
#       Set current_interval = substring_locations[i]
#       If current_interval[0] (start) <= previous_interval[1] (end) - overlapping intervals
#           Set previous_interval[1] = current_interval[1] (Update end value)
#       else
#           Append current_interval to result list
#           Set previous_interval = current_interval
#   return result
#
# Declare a function --> get_underscored_string(string, locations)
#   Initialize result = []
#   Initialize location_index = 0
#   Initialize string_index = 0
#   Initialize in_between_underscores = False (This is to indicate that we are currently inbetween the location intervals)
#   Initialize i = 0
#   Loop till string_index < string length and location_index < locations length
#       If string_index == locations[location_index][i] --> We reached a index in locations interval; i indicates start or stop
#           Append "_" to result
#           Swap the value of in_between_underscores (True if False & False if True)
#           If not in_between_underscores
#               Increment location_index by 1
#           Swap the value of i (0 if 1, 1 if 0)
#       Append letter at string[string_index] to result
#       Increment string_index by 1
#   if location_index < length of locations list:
#       Append "_" to result list
#   else if string_index < len(string):
#       Append all characters from string_index till end to result list
#   return result
##############################


def underscorifySubstring(string, substring):
    substring_locations = get_substring_locations(string, substring)
    collapsed_locations = get_collapsed_locations(substring_locations)
    underscored_string = get_underscored_string(string, collapsed_locations)
    return underscored_string


def get_substring_locations(string, substring):
    next_index = 0
    substring_length = len(substring)
    locations = []
    while next_index < len(string):
        next_index = string.find(substring, next_index)
        if next_index == -1:
            break
        locations.append([next_index, next_index + substring_length])
        next_index += 1
    return locations


def get_collapsed_locations(substring_locations):
    if not len(substring_locations):
        return substring_locations

    result = [substring_locations[0]]
    previous_interval = result[0]

    for i in range(1, len(substring_locations)):
        current_interval = substring_locations[i]
        if current_interval[0] <= previous_interval[1]:
            previous_interval[1] = current_interval[1]
        else:
            result.append(current_interval)
            previous_interval = current_interval
    return result


def get_underscored_string(string, locations):
    result = []
    location_index = 0
    string_index = 0
    in_between_underscores = False
    i = 0
    while string_index < len(string) and location_index < len(locations):
        if string_index == locations[location_index][i]:
            result.append("_")
            in_between_underscores = not in_between_underscores
            if not in_between_underscores:
                location_index += 1
            i = 0 if i == 1 else 1
        result.append(string[string_index])
        string_index += 1

    if location_index < len(locations):
        result.append("_")
    elif string_index < len(string):
        result.append(string[string_index:])
    return "".join(result)
