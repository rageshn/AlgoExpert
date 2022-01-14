"""
   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----

 Almost every digit is associated with some letters in the alphabet; this allows certain phone numbers to spell out
 actual words. For example, the phone number '8464747328' can be written as 'timisgreat'; similarly, the phone number
 '2686463' can be written as 'antoine' or as 'ant6463'.
 It's important to note that a phone number doesn't represent a single sequence of letters, but rather multiple
 combinations of letters. For instance, the digit 2 can represent three different letters (a, b, and c).
 A mnemonic is defined as a pattern of letters, ideas, or associations that assist in remembering something.
 Companies oftentimes use a mnemonic for their phone number to make it easier to remember.
 Given a stringified phone number of any non-zero length, write a function that returns all mnemonics for this
 phone number, in any order.
 For this problem, a valid mnemonic may only contain letters and the digits 0 and 1. In other words, if a digit
 is able to be represented by a letter, then it must be. Digits 0 and 1 are the only two digits that don't have
 letter representations on the keypad.
 Note that you should rely on the keypad illustrated above for digit-letter associations.
"""


# Iterative approach
# Time: O(n) | Space: O(n)
##########################
# Initialize numbers_map = list which holds the characters on the specific index
# Initialize phone_number = convert phone number provided to list of integers
# Set mnemonics = Call generate_mnemonics method by passing index = 0, phone_number, number_map & empty list --> generate_mnemonics(0, phone_number, numbers_map, [])
# return mnemonics
#
# Declare a function --> generate_mnemonics(i, phone_number, numbers_map, mnemonics)
#   Loop till i < length of phone_number
#       Set current_number = Get the ith index value from phone_number
#       Set characters = Get the letters from numbers_map at index current_number
#       If length of mnemonics < 1: (First iteration - Append the characters to empty list)
#           Loop through ever letter in characters
#               Append char to mnemonics list
#       else
#           Set characters_length = length of characters
#           Set mnemonics = mnemonics * characters_length (This will create new array which will hold all possible combinations of current letters)
#           Set mnemonics_length = length of mnemonics list
#           Set set_length = mnemonics_length / characters_length (This will decide the index/mnemonics up to which the current letter can be appended)
#           Set index = 0
#           Loop through every character in characters -> char
#               Set set_last_index = index + set_length
#               Loop till index < set_last_length
#                   Set mnemonics[index] = Append char to mnemonics[index]
#                   Increment index by 1
#       Increment i by 1
#   return mnemonics
##########################

def phoneNumberMnemonics(phoneNumber):
    numbers_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "xwyz"]
    phone_number = list(phoneNumber)
    mnemonics = generate_mnemonics(0, phone_number, numbers_map, [])
    return mnemonics


def generate_mnemonics(i, phone_number, numbers_map, mnemonics):
    while i < len(phone_number):
        current_number = int(phone_number[i])
        characters = numbers_map[current_number]
        if len(mnemonics) < 1:
            for char in characters:
                mnemonics.append(char)
        else:
            characters_length = len(characters)
            mnemonics = mnemonics * characters_length
            mnemonics_length = len(mnemonics)
            set_length = mnemonics_length / characters_length
            index = 0
            for char in characters:
                set_last_index = index + set_length
                while index < set_last_index:
                    mnemonics[index] = mnemonics[index] + char
                    index += 1
        i += 1
    return mnemonics


# Recursive approach
# Time: O(4^n * n) | Space: O(4^n * n)
######################################
# Declare a global map/dictionary DIGIT_LETTERS which holds the number ot letter combinations
# Initialize current_mnemonic = List with length as length of phone number which has 0 as the values
# Initialize mnemonics_found = empty list
# Call get_mnemonics function with index as 0, phone_number, current_mnemonic, mnemonics_found
# return mnemonics_found
#
# Declare a function --> get_mnemonics(index, phone_number, current_mnemonic, mnemonics_found)
#   If index == length of phone number
#       Set mnemonic = "".join(current_mnemonic) append letters in current_mnemonic to a single string
#       Append mnemonic to mnemonics_found list
#   else
#       Set digit = number from phone_number at index
#       Set letters = letters from DIGIT_LETTERS map at digit key
#       Loop through each letter in letters
#           Set current_mnemonic[index] = letter
#           recursively call get_mnemonics with index = index + 1 --> get_mnemonics(index + 1, phone_number, current_mnemonic, mnemonics_found)
######################################


DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def phoneNumberMnemonics(phoneNumber):
    current_mnemonic = ["0"] * len(phoneNumber)
    mnemonics_found = []
    get_mnemonics(0, phoneNumber, current_mnemonic, mnemonics_found)
    return mnemonics_found


def get_mnemonics(index, phone_number, current_mnemonic, mnemonics_found):
    if index == len(phone_number):
        mnemonic = "".join(current_mnemonic)
        mnemonics_found.append(mnemonic)
    else:
        digit = phone_number[index]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            current_mnemonic[index] = letter
            get_mnemonics(index + 1, phone_number, current_mnemonic, mnemonics_found)
