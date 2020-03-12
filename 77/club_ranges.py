# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].


# [(1, 3), (5, 8), (4, 10), (20, 25)]
# [(1,3), ()]

def clubRanges(ranges):
    idx = 1
    n = len(ranges)
    while idx < len(ranges):
        if ranges[idx - 1][1] > ranges[idx][0]:
            ranges = getNewRange(ranges, idx)
            idx = 0
        idx += 1
    return ranges


def getNewRange(ranges, i):
    nosList = []
    for num in ranges[i - 1]:
        nosList.append(num)
    for num in ranges[i]:
        nosList.append(num)
    minNum = min(nosList)
    maxNum = max(nosList)
    print(minNum, maxNum)
    newRanges = (minNum, maxNum)
    del ranges[i]
    ranges[i - 1] = newRanges
    return ranges


ranges = [(1, 3), (5, 8), (4, 10), (20, 25)]
# ranges = [(1, 3), (2, 10), (50, 55), (3, 5)]
ranges.sort(key=lambda x: (x[0], x[1]))
print('Ranges', ranges)
print(clubRanges(ranges))
