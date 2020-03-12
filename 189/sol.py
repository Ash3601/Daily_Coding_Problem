input = [1, 2, 3, 4, 2, 3, 4, 5, 6, 7, 3, 4]
# input = [5, 1, 3, 5, 2, 3, 4, 1]
tmp_list = []
max = 0

for i in input:
    if i not in tmp_list:
        tmp_list.append(i)
    else:
        max = len(tmp_list) if len(tmp_list) > max else max
        tmp_list = [i]

print(max if max >= len(tmp_list) else len(tmp_list))


class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i], current)
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i], current)
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


test1 = BinaryTree(1)
test1.insert([2])


def callback(node):
    print(node.value)


def iterativeInOrderTraversal(tree, callback):
    cur = tree
    pn = cur.parent

    while cur is not None:
        while cur.parent is pn:
            if cur.left is None and cur.right is None:

                callback(cur)
                if (pn is None):
                    exit()
                pn = cur
                cur = cur.parent
                break
            if cur.left is None:
                callback(cur)
                # print(cur.value)
                cur = cur.right
                pn = cur.parent
                continue
            cur = cur.left
            pn = cur.parent
        while cur.right is pn:
            pn = cur
            cur = cur.parent
            if cur is None:
                exit()
        while pn is cur.left and cur.right is None:
            callback(cur)
            # print(cur.value)
            pn = cur
            cur = cur.parent
            # continue
        if cur.right is not None:
            callback(cur)
            # print(cur.value)
            pn = cur
            cur = cur.right


iterativeInOrderTraversal(test1, callback)
