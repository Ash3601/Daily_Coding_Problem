# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

l1 = [1,2,3]
l2 = [4,5,6]
segments = list(zip(l1, l2))

# print (l)


# We will use two loops and check for each and every pair of point 

def isIntersect(p1, p2):
    if (p1[0] < p2[0] and p1[1] > p2[1]) or (p1[0] > p2[0] and p1[1] < p2[1]):
        return True 
    return False 

def getIntersections(p, q):
    segments = list(zip(p, q))
    count = 0
    for i in range(len(segments)):
        for j in range(i):
            p1, p2 = segments[j], segments[i]
            if isIntersect(p1, p2):
                count += 1
    return count 
p = [1,2]
q = [3,4]
count = getIntersections(p, q)
print (count)
