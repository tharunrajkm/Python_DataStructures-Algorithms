#Given a binary tree, check whether it’s a binary search tree or not.
# solution- If a tree is a binary search tree, then traversing the tree inorder should lead to sorted order of the values in the tree.
#  So, we can perform an inorder traversal and check whether the node values are sorted or not.
 
class BinaryTree(object):

    def __init__(self,rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key





tree_vals = []

def inorder(tree):
    if tree == None:
        return

    else:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)
        





r = BinaryTree(8)
r.insertLeft(7)
r.insertRight(11)


inorder(r)
print(sort_check(tree_vals))
