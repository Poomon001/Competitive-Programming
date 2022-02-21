# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/count-complete-tree-nodes/
    Purpose: Count all nodes in a completed tree 
    parameter: Optional[TreeNode] root - a root of a completed binary tree
    return: int count - number of all nodes in the tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 5 * 104].
                 : 0 <= Node.val <= 5 * 104
                 : The tree is guaranteed to be complete.
    Post-Condition: none
'''
# runtime: O(n), memory: O(depth of tree)
def countNodes(root):
    count = 0

    def dfs(root):
        if root is None:
            return

        nonlocal count
        count += 1

        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return count

if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)

    print(countNodes(root)) # 3

    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)

    print(countNodes(root)) # 6

    root.right.right = newNode(7)

    print(countNodes(root)) # 7
