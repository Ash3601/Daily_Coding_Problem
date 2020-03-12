def lis(sequence):
    # We have to use dp
    ss = len(sequence) * [1]  # sub sequence

    for i in range(1, len(sequence)):
        for j in range(0, i):
            currentIdx = i
            idx = j
            currentNum = sequence[currentIdx]
            numToCheck = sequence[idx]
            # we have to check if the currentNum is greater than the numToCheck
            if currentNum > numToCheck:
                ss[currentIdx] = max(ss[idx] + 1, ss[currentIdx])
        # ss[currentIdx] = resValue + 1
    print(ss)


sequence = [1, 2, 0, 3, 4]
lis(sequence)
