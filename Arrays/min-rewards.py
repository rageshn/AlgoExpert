"""
 Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores
 on the final exam in a particular order (not necessarily sorted), and you want to reward your students.
 You decide to do so fairly by giving them arbitrary rewards following two rules:
 1. All students must receive at least one reward.
 2. Any given student must receive strictly more rewards than an adjacent student
    (a student immediately to the left or to the right) with a lower score
    and must receive strictly fewer rewards than an adjacent student with a higher score.
 Write a function that takes in a list of scores and returns the minimum number of rewards
 that you must give out to students to satisfy the two rules.
 You can assume that all students have different scores; in other words, the scores are all unique.
"""


# Back track method
# Time: O(n^2) | Space: O(n)
#############################
# Initialize rewards as 1 for all scores
# Loop every element of the array
#   Initialize j as previous index
#   If current score > previous score
#       Update reward = previous reward + 1
#   else
#       Move back till scores[j] > scores[j+1]
#           Update reward = max of current reward and (previous reward + 1)
#
# return sum(rewards)
#############################


def minRewards(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)


# Local minimum and local maximum method
# Time: O(n) | Space: O(n)
###########################
# Initialize rewards a array of 1s
# Get all local minimum indexes from scores --> getLocalMinIndexes(scores)
# From every local minimum
#   Expand to left and right and update the rewards --> expandFromLocalMin(localMinIndex, scores, rewards)
# return sum(rewards)
#
# Declare a function --> getLocalMinIndexes(array)
#   If array has only one element, return that element
#   Initialize localMinIndexes as empty array
#   Loop through the scores
#       If current element is the first element and current element < next element
#           Append current index to localMinIndexes
#       If current element is the last element and current element < previous element
#           Append current index to localMinIndexes
#       If the current element is first or last element and not less than adjacent element
#           continue
#       If the current element is less than previous and next element
#           Append current index to localMinIndexes
#   return localMinIndexes
#
# Declare a function --> expandFromLocalMin(localMinIndex, scores, rewards)
#   -- Traverse to left of local Minimum
#   Assign left = local minimum index - 1
#   while left >= 0 and current score < score to right
#       update rewards[left] = max of current reward & (reward to right + 1)
#       Decrement left by 1
#
#   -- Traverse to right of local minimum
#   Assign right = local minimum index + 1
#   while right < len(scores) and current score > score to its left
#       update rewards[right] = reward of previous element + 1
#       Increment right by 1
###########################


def minRewards(scores):
    rewards = [1] * len(scores)
    localMinIndexes = getLocalMinIndexes(scores)
    for localMinIndex in localMinIndexes:
        expandFromLocalMin(localMinIndex, scores, rewards)
    return sum(rewards)


def getLocalMinIndexes(array):
    if len(array) == 1:
        return [0]
    localMinIndexes = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            localMinIndexes.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:
            localMinIndexes.append(i)
        if i == 0 and i == len(array) - 1:
            continue

        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            localMinIndexes.append(i)

    return localMinIndexes


def expandFromLocalMin(localMinIndex, scores, rewards):
    left = localMinIndex - 1
    while left >= 0 and scores[left] > scores[left + 1]:
        rewards[left] = max(rewards[left], rewards[left + 1] + 1)
        left -= 1
    right = localMinIndex + 1
    while right < len(scores) and scores[right] > scores[right - 1]:
        rewards[right] = rewards[right - 1] + 1
        right += 1


# Two pass method
# Time: O(n) | Space: O(n)
###########################
# Initialize rewards as array of 1s for all scores
# Loop through the array from left to right
#   If current element > previous element
#       Update reward = previous reward + 1
#
# Loop through the array from right to left
#   If current element > previous element
#       Update reward = max of current reward and (previous reward + 1)
#
# return sum(rewards)
###########################


def minRewards(scores):
    rewards = [1] * len(scores)
    for index, value in enumerate(scores):
        if index > 0:
            if value > scores[index - 1]:
                rewards[index] = rewards[index - 1] + 1

    index = len(scores) - 1
    for value in scores[::-1]:
        if index < len(scores) - 1:
            if value > scores[index + 1]:
                rewards[index] = max(rewards[index], rewards[index + 1] + 1)
        index -= 1

    min_rewards = sum(rewards)
    return min_rewards

