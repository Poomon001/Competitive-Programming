# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional
from collections import deque

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/symmetric-tree/
    Purpose: Determine if a tree is symmertric (mirror image)
    parameter: Optional[TreeNode] root - a root of a BST
    return: boolean - true if a tree is symmetric. Otherwise, false.
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def isSymmetric(root: Optional[TreeNode]) -> bool:
    left = []
    right = []

    # get left side
    def dfsLeft(root):
        if root.left:
            left.append(root.left.val)
            dfsLeft(root.left)
        else:
            left.append(None)

        if root.right:
            left.append(root.right.val)
            dfsLeft(root.right)
        else:
            left.append(None)

    # get right side
    def dfsRight(root):
        if root.right:
            right.append(root.right.val)
            dfsRight(root.right)
        else:
            right.append(None)

        if root.left:
            right.append(root.left.val)
            dfsRight(root.left)
        else:
            right.append(None)

    dfsLeft(root)
    dfsRight(root)

    return left == right

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = newNode(1)
    root1.left = newNode(2)
    root1.right = newNode(2)
    root1.left.left = newNode(3)
    root1.left.right = newNode(4)
    root1.right.left = newNode(4)
    root1.right.right = newNode(3)

    root2 = newNode(1)
    root2.left = newNode(2)
    root2.right = newNode(2)
    root2.left.right = newNode(3)
    root2.right.right = newNode(3)

    root3 = newNode(3)

    root4 = newNode(1)
    root4.left = newNode(2)
    root4.right = newNode(2)
    root4.left.left = newNode(3)
    root4.left.right = newNode(4)
    root4.right.left = newNode(0)
    root4.right.right = newNode(3)

    print(isSymmetric(root1)) # true
    print(isSymmetric(root2)) # false
    print(isSymmetric(root3)) # true
    print(isSymmetric(root4)) # false

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
