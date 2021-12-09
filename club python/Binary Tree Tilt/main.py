# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# helper function to find sum of all children nodes
def sumChildren(root):
    diffVal = root.val
    if root and root.left:
        diffVal += sumChildren(root.left)

    if root and root.right:
        diffVal += sumChildren(root.right)

    return diffVal

'''
    Link: https://leetcode.com/problems/binary-tree-tilt/
    Purpose: Determine the sum of every tree node's tilt.
           : The tilt of a tree node is the absolute difference between the sum of all left subtree node values 
           : and all right subtree node values. If node doesn't have a child, child will be 0.
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int diffVal - the tilt of a tree node
    Pre-Condition: The number of nodes in the tree is in the range [0, 104].
                 : -1000 <= Node.val <= 1000
    Post-Condition: none
'''
# runtime: O(n^2), memory: O(1)
def findTilt_M1(root: Optional[TreeNode]) -> int:
    diffVal = 0

    def dfs(root):
        nonlocal diffVal
        leftVal = 0
        rightVal = 0
        if root and root.left:
            leftVal = sumChildren(root.left)

        if root and root.right:
            rightVal = sumChildren(root.right)

        diffVal += abs(leftVal - rightVal)

        if root and root.left:
            dfs(root.left)

        if root and root.right:
            dfs(root.right)

    dfs(root)
    return diffVal

'''
    Link: https://leetcode.com/problems/binary-tree-tilt/
    Purpose: Determine the sum of every tree node's tilt.
           : The tilt of a tree node is the absolute difference between the sum of all left subtree node values 
           : and all right subtree node values. If node doesn't have a child, child will be 0.
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int diffVal - the tilt of a tree node
    Pre-Condition: The number of nodes in the tree is in the range [0, 104].
                 : -1000 <= Node.val <= 1000
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def findTilt_M2(root: Optional[TreeNode]) -> int:
    diffVal = 0
    sumChildren = 0

    def dfs(root):
        nonlocal diffVal
        nonlocal sumChildren
        leftVal = 0
        rightVal = 0

        if root and root.left:
            dfs(root.left)
            leftVal = root.left.val + sumChildren

        if root and root.right:
            dfs(root.right)
            rightVal = root.right.val + sumChildren

        sumChildren = leftVal + rightVal
        diffVal += abs(leftVal - rightVal)

    dfs(root)

    return diffVal

if __name__ == "__main__":
    root1 = newNode(1)
    root1.left = newNode(2)
    root1.right = newNode(3)

    root2 = newNode(4)
    root2.left = newNode(2)
    root2.right = newNode(9)
    root2.right.right = newNode(7)
    root2.left.left = newNode(3)
    root2.left.right = newNode(5)

    root3 = newNode(21)
    root3.left = newNode(7)
    root3.right = newNode(14)
    root3.right.left = newNode(2)
    root3.right.right = newNode(2)
    root3.left.left = newNode(1)
    root3.left.right = newNode(1)
    root3.left.left.left = newNode(3)
    root3.left.left.right = newNode(3)

    print("\n+==== M1 ====+\n")
    print(findTilt_M1(root1))  # 1
    print(findTilt_M1(root2))  # 15
    print(findTilt_M1(root3))  # 9

    print("\n+==== M2 ====+\n")
    print(findTilt_M2(root1)) # 1
    print(findTilt_M2(root2)) # 15
    print(findTilt_M2(root3)) # 9



