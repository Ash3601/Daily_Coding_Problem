# https://www.geeksforgeeks.org/a-product-array-puzzle/


def solution(arr):
    res = 1
    out = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j != i:
                res = res * arr[j]
        out.append(res)
        res = 1
    print(out)


l = [1, 2, 3, 4, 5]
solution(l)
