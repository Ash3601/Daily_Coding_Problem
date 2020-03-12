# Given a set of distinct positive ints, find largest subset that satisfies i%j = 0 or j%i = 0
# [1,3,5]
#  i j 
#  []
#  3 % 1 == 0:
#     YES -- > [].append(1) --> [1]
# [1,3,5]
#  i   j
#  NO --> Move on 
#  [1,3,5]
#     ij
#     YES [1].append(3)
def largestSubset(array):
    return largestSubsetHelper(array)

def largestSubsetHelper(array):
    currentArray = []
    bestArray = []
    for i in range(len(array)):
        for j in range(len(array)):
            if (array[i] % array[j] == 0 or array[j] % array[i] == 0 ) and array[i] not in currentArray:
                currentArray.append(array[i])
                if len(currentArray) > len(bestArray):
                    bestArray = currentArray
                    currentArray = []
    return bestArray

array = [3,5, 10, 20, 21]
array = [1,3,5]

ans = largestSubset(array)
print (ans)


