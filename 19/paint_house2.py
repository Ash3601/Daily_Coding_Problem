def minimizeColorCost(given_array):

    results = []
    findMinCost(given_array, results, 0, 0, -1)
    return min(results)


def helper(given_array, results, curr_house, prev_color, curr_cost, curr_sequence):

    if curr_house == len(given_array):
        results.append((curr_cost, curr_sequence))
        return
    for i in range(0, len(given_array[0])):
        if i != prev_color:
            helper(given_array, results, curr_house + 1, i,
                   given_array[curr_house][i] + curr_cost, curr_sequence + str(i))


def findMinCost(cost_matrix, results, curr_houses, curr_cost, prev_color_index):
    if curr_houses == len(cost_matrix):
        results.append(curr_cost)
        return
    for i in range(0, len(cost_matrix[0])):
        if i != prev_color_index:
            findMinCost(cost_matrix, results, curr_houses + 1,
                        cost_matrix[curr_houses][i] + curr_cost, i)


# arr = [[1, 2, 3, 4], [1, 2, 1, 0], [6, 1, 1, 5], [2, 3, 5, 5]]
arr = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
# arr = [[1, 2, 3], [1, 4, 6]]
print(minimizeColorCost(arr))
