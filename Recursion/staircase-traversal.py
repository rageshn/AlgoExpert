"""
 You're given two positive integers representing the height of a staircase and the maximum number of steps that you can
 advance up the staircase at a time. Write a function that returns the number of ways in which you can climb the
 staircase.
 For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways.
 You could take 1 step, 1 step, then 1 step, you could also take 1 step, then 2 steps, and you could take
 2 steps, then 1 step.
 Note that maxSteps <= height will always be true.
"""


# Recursive approach
# Time: O(k^n) | Space: O(n)
############################
# This approach recursively calls the steps required from 0 and moves upwards till the height of the steps.
# For each step, we have to sum the previous 'n' step values, where n = max_steps
#
# Declare a function --> ways_to_top(height, max_steps)
#   If height <= 1 (For 0 & 1, it has only one way)
#       return 1
#   Initialize number_of_ways = 1
#   Loop the steps from 1 till height --> step
#       Set number_of_ways = number_of_ways + ways_to_top(height - step, max_steps)
#   return number_of_ways
############################


def staircaseTraversal(height, maxSteps):
    return ways_to_top(height, maxSteps)


def ways_to_top(height, max_steps):
    if height <= 1:
        return 1

    number_of_ways = 0
    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += ways_to_top(height - step, max_steps)
    return number_of_ways


# Recursive approach with results stored in dictionary
# Time: O(n * k) | Space: O(n)
###############################
# This also uses the same recursive approach, but it stores number of ways in a dictionary. While recomputing, it just
# returns the number of ways from dictionary instead of recomputing all the values.
#
# Initialize memoize = {0: 1, 1: 1} --> number of ways you can climb 0 and 1 steps
# return the output of ways_to_top method, by passing height, maxSteps and memoize
#
# Declare a function --> ways_to_top(height, max_steps, memoize)
#   If height is already available in memoize
#       return memoize[height]
#   Initialize number_of_ways = 0
#   Loop the steps from 1 till height --> step
#       Set number_of_ways = number_of_ways + ways_to_top(height - step, max_steps)
#   Add height and number of ways to memoize dictionary
#   return number_of_ways
###############################


def staircaseTraversal(height, maxSteps):
    memoize = {0: 1, 1: 1}
    return ways_to_top(height, maxSteps, memoize)


def ways_to_top(height, max_steps, memoize):
    if height in memoize:
        return memoize[height]

    number_of_ways = 0
    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += ways_to_top(height - step, max_steps, memoize)

    memoize[height] = number_of_ways
    return number_of_ways


# Dynamic programming
# Time: O(n * k) | Space: O(n)
##########################
# This approach maintains a list of integers, in which index is the height and value represents the number of ways
# to climb that height.
#
# Initialize ways_to_top = list with length as height + 1 and value as 0
# Set ways_to_top[0] and ways_to_top[1] = 1 . This indicates, number of ways to climb 0 and 1 steps.
#
# Loop the heights list from 2 till height + 1 --> current_height
#   Initialize step = 1
#   Loop till step <= maxSteps and step <= current_height
#       Set ways_to_top[current_height] = ways_to_top[current_height] + ways_to_top[current_height - step]
#       Increment step by 1
#       The way to reach the current step is number of ways to get from the previous step and the step number of stairs behind.
# return ways_to_top[height]
##########################


def staircaseTraversal(height, maxSteps):
    ways_to_top = [0 for _ in range(height + 1)]
    ways_to_top[0] = 1
    ways_to_top[1] = 1

    for current_height in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= current_height:
            ways_to_top[current_height] = ways_to_top[current_height] + ways_to_top[current_height - step]
            step += 1
    return ways_to_top[height]


# Sliding window
# Time: O(n) | Space: O(n)
##########################
# With sliding window approach, we can have a window of length maxSteps, which moves along the height and calculates the
# number of ways to climb the steps.
# When we move to each step, we remove the value from the start of the window and add the value at the end of the window.
#
# Initialize current_number_of_ways = 0
# Initialize ways_to_top = [1] (ways to climb 0 steps)
# Iterate through the steps from 1 till height + 1 (Including height) --> current_height
#   Set start_of_window = current_height - maxSteps - 1
#   Set end_of_window = current_height - 1
#   If start_of_window >= 0
#       Set current_number_of_ways -= ways_to_top[start_of_window] (remove the previous start index from the window)
#   Set current_number_of_ways += ways_to_top[end_of_window] (add the next element to the end of the window)
#   Append current_number_of_ways to ways_to_top
# return ways_to_top[height]
##########################


def staircaseTraversal(height, maxSteps):
    current_number_of_ways = 0
    ways_to_top = [1]
    for current_height in range(1, height + 1):
        start_of_window = current_height - maxSteps - 1
        end_of_window = current_height - 1
        if start_of_window >= 0:
            current_number_of_ways -= ways_to_top[start_of_window]

        current_number_of_ways += ways_to_top[end_of_window]
        ways_to_top.append(current_number_of_ways)
    return ways_to_top[height]
