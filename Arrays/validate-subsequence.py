"""
Given two non-empty array of integers, write a function that determines whether the second array is a sub sequence of the first one.
"""


# Basic approach
# Time: O(n^2) | Space: O(n)
#############################
# If the array length and subsequence array length <= 1, and the elements are same then return True.
# Initialize seq index to 0 and is_subseq to to empty list.
# Loop through the elements in sub sequence
#    Set X to current element
#    Initialize next sequence index to 0
#    Check whether X is available in array between seq index and last element -> Returns the index in which the element exists (next sequence index)
#        If the element exists, append 1 to is_subseq, else append 0
#    Set seq index to next sequence index + 1
# If is_subseq has 0, return False
# return True
#############################

def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(array) == 1 and len(sequence) == 1:
        if sequence[0] == array[0]:
            return True

    seq_index = 0
    is_subseq = []
    for val in sequence:
        seq_index_next = 0
        try:
            seq_index_next = array.index(val, seq_index, len(array))
            if seq_index_next > seq_index:
                is_subseq.append(1)
        except ValueError as e:
            is_subseq.append(0)
            pass
        seq_index = seq_index_next + 1

    if 0 in is_subseq:
        return False
    return True


# Looping array once
# Time: O(n) | Space: O(1)
############################
# Initialize two pointers arrIndex and seqIndex = 0, referring to array and sequence respectively.
# Loop through array and subsequence
# Check if subsequence[seqIndex] == array[arrIndex]
#     If yes, then increment seqIndex by 1
#     Else, increment arrIndex by 1
# If seqIndex == len(subsequence), return True. Else return False
############################

def isValidSubsequence(array, sequence):
    # Write your code here.
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


# Above solution with for loop
# Time: O(n) | Space: O(1)
############################
# Initialize seqIndex = 0
# Loop through every element in array
#    If sequence[seqIndex] == current element
#        Increment seqIndex by 1
#    If seqIndex == len(sequence), break the loop. Must be added first so that the index check wont throw exception
# Check the same condition and return True
############################

def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

