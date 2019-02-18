"""
Example of kd_tree construction.
"""
import numpy as np
from copy import copy, deepcopy
T = np.array([[2,3], [5,4], [9,6], [4,7], [8,1], [7,2]])

class BinaryTree():
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        self.visited = 0

    def insertLeft(self, left):
        self.leftChild = BinaryTree(left)
        print('insert left')

    def insertRight(self, right):
        self.rightChild = BinaryTree(right)
        print('insert right')


def compare(new, binarytree):
    binarytree = deepcopy(binarytree)
    if new[1] < binarytree.key[1]:
        print('27 : new[1] {:} < binarytree.key[1] {:}'.format(new[1], binarytree.key[1]))
        if binarytree.leftChild == None:
            binarytree.insertLeft(new)
        elif binarytree.leftChild.key[1] < new[1]:
            print('31 : new[1] {:} > binarytree.leftChild.key[1] {:}'.format(new[1], binarytree.leftChild.key[1]))
            binarytree.leftChild.insertRight(new)
        else:

            binarytree.leftChild = compare(new, binarytree.leftChild)

    elif new[1] > binarytree.key[1]:
        print('38 : new[1] {:} > binarytree.key[1] {:}'.format(new[1], binarytree.key[1]))
        if binarytree.rightChild == None:
            print('r == None.')
            binarytree.insertRight(new)
        elif binarytree.rightChild.key[1] > new[1]:
            print('43 : new[1] {:} < binarytree.rightChild.key[1] {:}'.format(new[1], binarytree.rightChild.key[1]))
            binarytree.rightChild.insertLeft(new)
        else:
            binarytree.rightChild = compare(new, binarytree.rightChild)
    return binarytree

binarytree = BinaryTree([5,5])
for i,t in enumerate(T):
    print(i, '|', t)
    binarytree = compare(t, binarytree)

print('===sorting=====')
# TODO： 有没有什么stack，queue的说法呢？

def sort(sorted,binarytree):

    if binarytree.leftChild is not None:
        print('l')
        sort(sorted, binarytree.leftChild)
        binarytree.leftChild = None
        sort(sorted, binarytree)

    if binarytree.visited == 0:
        sorted.append(binarytree.key)
        binarytree.visited = 1

    if binarytree.rightChild is not None:
        print('r')
        sort(sorted, binarytree.rightChild)
        binarytree.rightChild = None
        sort(sorted, binarytree)

sorted = []
sort(sorted,binarytree)
print(sorted)