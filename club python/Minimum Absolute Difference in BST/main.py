from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
    Purpose: Find the minimum absolute difference between the values of any two different nodes in the tree, given a root of bst
    parameter: Optional[TreeNode] - a root of bst
    return: int minDiff - the minimum absolute difference between the values of any two different nodes in the tree
    Pre-Condition: The number of nodes in the tree is in the range [2, 104].
                 : 0 <= Node.val <= 105
    Post-Condition: none
'''
# bst property: runtime: O(n), memory: O(log(n))
def getMinimumDifference(root: Optional[TreeNode]) -> int:
    minDiff = inf
    prevVal = None

    # left-root-right
    def inOrder(root):
        nonlocal minDiff, prevVal
        if root.left:
            inOrder(root.left)

        if root:
            if prevVal is not None:
                minDiff = min(minDiff, root.val - prevVal)
            prevVal = root.val

        if root.right:
            inOrder(root.right)

    inOrder(root)

    return minDiff

if __name__ == '__main__':
    root1 = TreeNode(9)
    root1.left = TreeNode(0)

    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right = TreeNode(6)

    root3 = TreeNode(1)
    root3.left = TreeNode(0)
    root3.right = TreeNode(48)
    root3.right.left = TreeNode(12)
    root3.right.right = TreeNode(49)


    print(getMinimumDifference(root1)) # 9
    print(getMinimumDifference(root2))  # 1
    print(getMinimumDifference(root3))  # 1