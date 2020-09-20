"""
Given an array of integers and an integer,
Write a function that moves all instances of that integer in the array to the end of the array and returns the array.
The function should perform this in place adn doesn't need to maintain the order of other integers.
"""


# Two pointer approach
# Time: O(n) | Space: O(1)
###########################
# Initialize left_index to 0
# Loop the list backwards with currPointer variable
#     if array[currPointer] is not the number to move
#         while left_index < currPointer and array[left_index] is not number to move
#             Increment left_index
#         if left_index < currPointer and array[left_index] = number to move
#             swap the elements at left_index and currPointer
#             Increment left_index
#     else pass
# return array
###########################

def moveElementToEnd(array, toMove):
    left_index = 0

    for currPointer in range(len(array) - 1, 0, -1):
        if array[currPointer] != toMove:
            while array[left_index] != toMove and left_index < currPointer:
                left_index += 1
            if left_index < currPointer and array[left_index] == toMove:
                # swap left_index and current pointer
                array[left_index], array[currPointer] = array[currPointer], array[left_index]
                left_index += 1
        else:
            pass
    return array


def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array
