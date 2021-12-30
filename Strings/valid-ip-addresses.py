"""
 You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible
 IP addresses that can be created by inserting three "." in the string.
 An IP address is a sequence of four positive integers that are separated by "." s, where each individual integer
 is within the range 0 - 255 inclusive.
 An IP address isn't valid if any of the individual integers contains leading 0s. For example, "192.168.0.1" is a
 valid ip address, but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and "01". Another example
 of valid ip address is "99.1.1.10"; conversely, "991.1.1.10" isn't valid, because "991" is greater than 255.
 Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses
 can be created from the string, your function should return an empty list.
"""

# Using 3 for loops
# Time: O(1) | Space: O(1)
##########################
# This approach splits the string into 4 parts and loops each part to check whether it's valid or not.
# Whenever a valid ip address is found, it will be added to the final list and returned.
#
# Initialize a list in_address_found which will hold all the vlaid ip addresses
#   Loop through the first 4 characters in the string (range started from 1, because the first "." should be placed
#   (after the first position in the string, and we can't have "." with empty string. min(len(string), 4) is used
#   so that the code won't throw out of bounds exception)
#       Initialize ip_address_parts as list of 4 empty strings, each denoting an octet in ip address.
#       Assign the ip_address_parts[0] as the string till index "i". i.e., first octet
#       If the ip_address_parts[0] (first octet) is not valid --> is_valid(ip_address_parts[0])
#           continue
#       Loop through the string from the next index of "i" & next 3 characters
#           Assign the ip_address_parts[1] as the string from i till j
#           If the ip_Address_parts[1] (second octet) is not valid --> is_valid(ip_address_parts[1])
#               continue
#           Loop the string from the next index of "j" & next 3 characters
#               Assign ip_address_parts[2] as the string from j till k
#               Assign ip_address_parts[3] as the string from k till end
#               If ip_address_parts[2] (third octet) and ip_address_parts[3] are both valid
#                   Concatenate all values in ip_address_parts with "." and add it to in_address_found list
#   return in_address_found
#
# Declare a function --> is_valid(string)
#   Convert the string to integer (str_to_int). This removes any 0 in the front.
#   If the str_to_int > 255
#       return False
#   if the length of original string and str_to_int are equal
#       return True
#   else
#       return False
##########################


def validIPAddresses(string):
    ip_addresses_found = []

    for i in range(1, min(len(string), 4)):  # Index starts with 1 because we can't have "." with empty string. i.e., 1.111 & not .1111
        ip_address_parts = ["", "", "", ""]

        ip_address_parts[0] = string[:i]
        if not is_valid(ip_address_parts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            ip_address_parts[1] = string[i:j]
            if not is_valid(ip_address_parts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                ip_address_parts[2] = string[j:k]
                ip_address_parts[3] = string[k:]

                if is_valid(ip_address_parts[2]) and is_valid(ip_address_parts[3]):
                    ip_addresses_found.append(".".join(ip_address_parts))

    return ip_addresses_found


def is_valid(string):
    str_as_int = int(string)  # Removes 0 in front, if any
    if str_as_int > 255:
        return False

    return len(string) == len(str(str_as_int))  # check for leading 0
