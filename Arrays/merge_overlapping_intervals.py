"""
 Write a function that takes in a non-empty array of arbitrary integers, merges any overlapping intervals, and returns
 the new interval in no particular order.
 Each interval "interval" is an array of two integers, with interval[0] as start of the interval and interval[1] as end
 of the interval.
 Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping.
 However, [1, 6] and [6, 7] are indeed overlapping.
 Also note that the start of any particular interval will always be less than or equal to the end of the interval.
"""


# Iterative approach
# Time: O(n*log(n)) | Space: O(n)
##################################
# Sort the intervals based on the start value
# Initialize all_intervals to array of 0.
# Loop through every intervals
#   Get the current interval from intervals and previous interval values from all_intervals
#   If previous interval's end value is >= current interval's start value
#       Set the interval in all_interval as [previous interval start value, max(end value of previous interval, end value of current interval)
#   else
#       Add current interval to all_intervals
# return all_intervals
###################################


def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    all_intervals = [0 for index in range(0, len(intervals))]
    interval_count = 0
    for index in range(0, len(intervals)):
        current_interval = intervals[index]
        if index > 0:
            prev_interval = all_intervals[interval_count - 1]
            if prev_interval[1] >= current_interval[0]:
                all_intervals[interval_count - 1] = [prev_interval[0], max(prev_interval[1], current_interval[1])]
            else:
                all_intervals[interval_count] = current_interval
                interval_count += 1
        else:
            all_intervals[interval_count] = current_interval
            interval_count += 1

    result = []
    for interval in all_intervals:
        if type(interval) == list:
            result.append(interval)
    return result


def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals





