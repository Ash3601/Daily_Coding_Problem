# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                # print('Value Found')
                return True
        # print('Value not found')
        return False

    def remove(self, value, parentNode=None):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # ? Case 1: Node has two children nodes
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinVal()
                    currentNode.right.remove(currentNode.value, currentNode)
                # ? The cases left are the ones with the parent node and without the parent node
                # ? For e.g. the root node of the bst that do not have a parent node
                #! We're gonna do this case later
                # ? Finally to our case in which the parent node is None
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.right

                pass
        return self

    def getMinVal(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

def getCommonSum(bst):
    return getCommonSumHelper(bst, 0, {})
finalArr = []
finalSum = 0
def inorder(bst):
    if bst:
        inorder(bst.left)
        global finalSum
        finalSum += bst.value
        inorder(bst.right)
    return finalSum
    # return sum
    # if bst.left is None and bst.right is None:
    #     return sum += bst.value 
    # inorder(bst.left)
    # inorder(bst.right)
dictionary = {}
def getCommonSumHelper(bst, sum):
    if bst:
        sumSubTree = inorder(bst)
        print ("Sub Tree Sum: ", sumSubTree)
        global dictionary
        if sumSubTree in dictionary.keys():
            dictionary[sumSubTree] += 1
            print ("Sum: ", dictionary[sumSubTree])
        else:
            print ("In else")
            dictionary[sumSubTree] = 0
        global finalSum
        finalSum = 0
        getCommonSumHelper(bst.left, sum)
        getCommonSumHelper(bst.right, sum)
    print (dictionary)
    return dictionary
        # sumRoot = inorder(bst)
        # bst = bst.left
        # sumRight = inorder(bst.left)
        # bst = bst.right
        # sumLeft = inorder(bst.right)
    # if bst:
    #     sum = bst.value + inorder(bst.left) + inorder(bst.right)
    # print (sum)

    

test1 = BST(0).insert(5).insert(0)
print(test1.left.value)
print(test1.right.value)
print(test1.value)
res = getCommonSumHelper(test1, 0)
print ("Final ans", res) 
# sumVal = inorder(test1, 0, [])
# print ("Sum: ",sumVal)
# test1.contains(5)

# test1.contains(50)
