def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0]) # sorting intervals
    merged = [] # empty list to hold the result
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval) # If there is no overlap, the current interval is added to the merged list
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            #update the end of the last merged interval to the larger end of the last interval and the current interval,
            #ensuring that the combined interval covers both ranges.
    return merged # return merged list.

print(merge_intervals([[1, 3], [2, 4], [6, 8]]))
