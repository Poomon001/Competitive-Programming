from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

'''
    Link: https://leetcode.com/problems/binary-tree-right-side-view/
    Purpose: Find the values of the nodes you can see from the right hand-side ordered from top to bottom
    parameter: Optional[TreeNode] root - a root of binary tree
    return: List[int] answer - the values of the nodes you can see from the right hand-side ordered from top to bottom
    Pre-Condition: The number of nodes in the tree is in the range [0, 100].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# BFS: runtime - O(nlog(n)), memory - O(n)
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    answer = []
    queue = deque()
    queue.append(root)
    answer.append(root.val)
    level = 1

    while queue:
        temp = deque()
        while queue:
            currNode = queue.popleft()

            if currNode.right and level == len(answer):
                answer.append(currNode.right.val)

            if currNode.left and level == len(answer):
                answer.append(currNode.left.val)

            if currNode.right:
                temp.append(currNode.right)

            if currNode.left:
                temp.append(currNode.left)

        level += 1
        queue = temp

    return answer

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(rightSideView(root1)) # [1, 3, 4]

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(rightSideView(root2)) # [1, 2]

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.right = TreeNode(5)
    root3.left.left = TreeNode(4)
    print(rightSideView(root3)) # [1, 3, 5]

    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.right = TreeNode(5)
    root4.left.left = TreeNode(4)
    root4.left.left.left = TreeNode(6)
    print(rightSideView(root4)) # [1, 3, 5, 6]

    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.right = TreeNode(5)
    root4.left.left = TreeNode(4)
    root4.left.left.left = TreeNode(6)
    root4.left.right.left = TreeNode(7)
    print(rightSideView(root4)) # [1, 3, 5, 7]


