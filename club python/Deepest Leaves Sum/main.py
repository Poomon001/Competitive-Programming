from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

'''
    Link: https://leetcode.com/problems/deepest-leaves-sum/
    Purpose: Find a sum of all node in the deepest level
    parameter: Optional[TreeNode] root - a root of BST
    return: int deepestSum - a sum of all nodes in the deepest level
    Pre-Condition: The number of nodes in the tree is in the range [1, 104].
                 : 1 <= Node.val <= 100
    Post-Condition: none
'''
# BFS - runtime: O(n), memory: O(n)
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    queue = deque()
    queue.append(root)
    deepestSum = 0

    while queue:
        temp = deque()
        currSum = 0
        while queue:
            curr = queue.popleft()

            if curr.left:
                temp.append(curr.left)
                currSum += curr.left.val

            if curr.right:
                temp.append(curr.right)
                currSum += curr.right.val

        # reset deepestSum if there is a node in a deeper level
        if currSum != 0:
            deepestSum = currSum

        queue = temp

    return deepestSum

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.left.left.left = TreeNode(7)
    root1.right.right = TreeNode(6)
    root1.right.right.right = TreeNode(8)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)

    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.right.right = TreeNode(6)

    print(deepestLeavesSum(root1)) # 15
    print(deepestLeavesSum(root2))  # 1
    print(deepestLeavesSum(root3))  # 5
    print(deepestLeavesSum(root4))  # 6
