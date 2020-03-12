# min num of intervals to be removed to make the rest of intervals non-overlapping 
def solution(intervals):
    intervals.sort(key = lambda x: x[0])
    return getMinIntervals(intervals)

def overlapping(prev, next):
    if prev[1] > next[0]:
        return True 
    return False


def getMinIntervals(intervals):
    removals = 0
    if len(intervals) is 1:
        return 0 
    
    i = 1 
    while i < len(intervals):
        intervalPrev = intervals[i - 1]
        intervalNext = intervals[i]
        if overlapping(intervalPrev, intervalNext):
            removals += 1
            intervals.pop(i)
        else: 
            i += 1
    return removals

intervals = [(7,9), (2,4), (5,8)]
intervals = [(2,7), (3,9), (5,8), (6,9)]
print (solution(intervals))

    