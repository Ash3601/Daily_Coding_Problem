# You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

# For example, given the following table:

# cba
# daf
# ghi
# This is not ordered because of the a in the center. We can remove the second column to make it ordered:

# ca
# df
# gi
# So your function should return 1, since we only needed to remove 1 column.

# As another example, given the following table:

# abcdef
# Your function should return 0, since the rows are already ordered (there's only one row).

# As another example, given the following table:

# zyx
# wvu
# tsr
# Your function should return 3, since we would need to remove all the columns to order it.


def removeCols(matrix):
    N = len(matrix[0])  # rows
    M = len(matrix)  # cols

    if N == 0 and M == 0:
        return
    if N == 1 or M == 1:
        return 0

    colToRemove = 0

    # iterate over the cols
    for col in range(M):
        for row in range(1, N):
            second = matrix[row][col]
            first = matrix[row - 1][col]
            if second < first:
                colToRemove += 1
                break
    return colToRemove


matrix = [
    ['c', 'b', 'a'],
    ['d', 'a', 'f'],
    ['g', 'h', 'i'],

]
matrix = [
    ['c', 'b', 'a']
]

matrix = [
    ['z', 'y', 'x'],
    ['w', 'v', 'u'],
    ['t', 's', 'r'],

]
print(removeCols(matrix))
