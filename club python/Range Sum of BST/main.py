# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/range-sum-of-bst/
    Purpose: Find the sum of values of all nodes with a value in the inclusive range [low, high]
    parameter: Optional[TreeNode] root - a root of a binary tree
             : int low - a lower integer
             : int high - a higher integer
    return: int sumNum - the sum of values of all nodes with a value in the inclusive range [low, high]
    Pre-Condition: The number of nodes in the tree is in the range [1, 2 * 104].
                 : 1 <= Node.val <= 105
                 : 1 <= low <= high <= 105
                 : All Node.val are unique.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    sumNum = 0

    def dfs(root):
        nonlocal sumNum
        if low <= root.val <= high:
            sumNum += root.val

        if root and root.left:
            dfs(root.left)

        if root and root.right:
            dfs(root.right)

    dfs(root)
    return sumNum

if __name__ == "__main__":
    root1 = newNode(10)
    root1.left = newNode(5)
    root1.right = newNode(15)
    root1.left.left = newNode(3)
    root1.left.right = newNode(7)
    root1.right.right = newNode(18)

    root2 = newNode(10)
    root2.left = newNode(5)
    root2.right = newNode(15)
    root2.left.left = newNode(3)
    root2.left.right = newNode(7)
    root2.right.left = newNode(13)
    root2.right.right = newNode(18)
    root2.left.left.left = newNode(1)
    root2.left.right.left = newNode(6)

    print(rangeSumBST(root1, 7, 15)) # 32
    print(rangeSumBST(root1, 0, 100))  # 58
    print(rangeSumBST(root1, 0, 1))  # 0
    print(rangeSumBST(root2, 6, 10)) # 23
    print(rangeSumBST(root2, 1, 100))  # 78
    print(rangeSumBST(root2, 1, 2))  # 1







