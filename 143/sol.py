rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]

rect = dict(rectangles)
# print(rectangles[0]['top_left'])


def compare_rects(rectangles):
    for i in range(len(rectangles)):
        for j in range(1, len(rectangles)):
            p1x, p1y = rectangles[i]['top_left']
            p1x = p1x + rectangles[i]['dimensions'][1]
            p1y = p1y + rectangles[i]['dimensions'][0]
            p2x, p2y = rectangles[j]['top_left']

            if (p2x < p1x) or (p2x > p1x):
                print(i + 1, j + 1)
                return True
            elif (p2y < p1y) or (p2y > p1y):
                print(i + 1, j + 1)
                return True
    return False


print(compare_rects(rectangles))
