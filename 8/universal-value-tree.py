class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


# Create a tree
root = Node(3)
root.left = Node(2)
root.right = Node(3)
root.right.left = None
root.right.right = Node(2)
root.right.right.left = Node(2)
root.right.right.right = Node(2)


def isUnival(root):
    if root == None:
        return True

    if root.left is not None and root.left.value != root.value:
        return False

    if root.right is not None and root.right.value != root.value:
        return False

    if isUnival(root.left) and isUnival(root.right):
        return True
    return False  # ? False if the values are not consistent


def countUnivalTrees(root):
    if root == None:
        return 0

    total_counts = countUnivalTrees(root.left) + countUnivalTrees(root.right)
    if isUnival(root):
        total_counts += 1
    return total_counts


print(countUnivalTrees(root))
