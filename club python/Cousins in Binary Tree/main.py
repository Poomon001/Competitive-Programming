# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode():
    # Credit: https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Link: https://leetcode.com/problems/cousins-in-binary-tree/
    Purpose: Find if 2 given nodes are cousins. 
           : Two nodes of a binary tree are cousins if they have the same depth with different parents.
    parameter: Optional[TreeNode] root - a root of binary tree
             : int x - fist node integer
             : int y - second node integer
    return: bool - true if they are cousins. Otherwise false.
    Pre-Condition: The number of nodes in the tree is in the range [2, 100].
                 : 1 <= Node.val <= 100
                 : Each node has a unique value.
                 : x != y
                 : x and y are exist in the tree.
    Post-Condition: none
'''
# runtime: O(n), memory: O(depth of tree)
def isCousins(root: Optional[TreeNode], x: int, y: int) -> bool:
    infoX = []
    infoY = []
    def dfs(root: Optional[TreeNode], x: int, y:int, parent: int, depth: int) -> List:
        if root is None:
            return

        if root.val == x:
            infoX.append(depth)
            infoX.append(parent)

        if root.val == y:
            infoY.append(depth)
            infoY.append(parent)


        dfs(root.left, x, y, root.val, depth + 1)
        dfs(root.right, x, y, root.val, depth + 1)

    dfs(root, x, y, None, 0)

    return infoX[1] != infoY[1] and infoX[0] == infoY[0]

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.right = newNode(8)
    root.left.left = newNode(4)
    root.right.right = newNode(7)

    print(isCousins(root, 4, 3)) # false
    print(isCousins(root, 4, 8)) # false
    print(isCousins(root, 2, 3)) # false
    print(isCousins(root, 4, 7)) # true
    print(isCousins(root, 7, 8)) # true


