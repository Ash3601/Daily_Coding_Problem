# array rotation in place

# Time Complexity: O(n * k)


def rotateByOne(array):
    size = len(array) - 1
    lastVar = array[-1]
    while size > 0:
        array[size] = array[size - 1]
        size -= 1
    array[0] = lastVar


def rotateByK(array, k):
    while k > 0:
        rotateByOne(array)
        k -= 1
    return array


array = [1, 2, 3, 4, 5]
k = 2
rotateByK(array, k)
print(array)
