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
    Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
    Purpose: Find a sum of all binary left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of all binary left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : Node.val is 0 or 1.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def sumRootToLeaf(root: Optional[TreeNode]) -> int:
    sumRoot = 0

    def dfs(root, num):
        nonlocal sumRoot

        if root.left:
            dfs(root.left, num + str(root.left.val))

        if root.right:
            dfs(root.right, num + str(root.right.val))

        if root and not root.left and not root.right:
            sumRoot += int(num, 2)

    dfs(root, str(root.val))
    return sumRoot

if __name__ == '__main__':
    root1 = newNode(1)
    root1.left = newNode(0)
    root1.right = newNode(1)
    root1.left.left = newNode(0)
    root1.left.right = newNode(1)
    root1.right.left = newNode(0)
    root1.right.right = newNode(1)

    root2 = newNode(0)

    root3 = newNode(1)
    root3.left = newNode(0)
    root3.right = newNode(1)

    root4 = newNode(1)
    root4.left = newNode(0)
    root4.right = newNode(1)
    root4.left.left = newNode(0)

    root5 = newNode(1)
    root5.left = newNode(0)
    root5.right = newNode(1)
    root5.left.left = newNode(0)
    root5.left.right = newNode(0)

    print(sumRootToLeaf(root1)) # 22
    print(sumRootToLeaf(root2)) # 0
    print(sumRootToLeaf(root3)) # 5
    print(sumRootToLeaf(root4)) # 7
    print(sumRootToLeaf(root5))  # 11




