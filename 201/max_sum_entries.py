def max_sum_entry(array):
    prevIdx = array[0].index(max(array[0]))
    row = 0
    sumValue = 0
    while row < len(array):
        sumValue = sumValue + array[row][prevIdx]
        row += 1
        # prevIdx = prevIdx - 1
        curIdx = prevIdx
        nextIdx = prevIdx + 1
        # if prevIdx < 0:
        # prevIdx = 0
        if row >= len(array):
            break
        if nextIdx >= len(array[row]):
            nextIdx = len(array[row]) - 1
        idx = [array[row][prevIdx], array[row][nextIdx], array[row][curIdx]].index(
            max(array[row][prevIdx], array[row][nextIdx], array[row][curIdx]))
        if idx == 2:
            prevIdx = curIdx
        elif idx == 1:
            prevIdx = nextIdx
    return sumValue


array = [[1, 2], [2, 3, 1], [1, 5, 8, 1]]

# array = [[1, 2], [2, 3, 8], [1, 5, 1, 100]]
ans = max_sum_entry(array)
print(ans)
