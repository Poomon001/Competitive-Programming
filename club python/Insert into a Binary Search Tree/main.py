# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List
from collections import deque

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
    Purpose: Insert an integer into a BST
    parameter: Optional[TreeNode] root - a root of a BST
             : int val - an integer
    return: Optional[TreeNode] root - a root of an updated BST
    Pre-Condition: The number of nodes in the tree will be in the range [0, 104].
                 : -10^8 <= Node.val <= 10^8
                 : All the values Node.val are unique.
                 : -10^8 <= val <= 10^8
                 : It's guaranteed that val does not exist in the original BST.
    Post-Condition: none
'''
# runtime: O(h) where h is the height of the tree, memory: O(1)
def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # tree is empty
    if root is None:
        root = newNode(val)

    # go to left
    if root and root.val > val:
        if root.left:
            insertIntoBST(root.left, val)
        else:
            root.left = newNode(val)

    # go to right
    if root and root.val < val:
        if root.right:
            insertIntoBST(root.right, val)
        else:
            root.right = newNode(val)

    return root

# basic bfs level-order transversal
# runtime: O(n), memory: O(n)
def printBFSLevelOrder(root):
    queue = deque()
    queue.appendleft(root)

    while len(queue) != 0:
        temp = deque()

        while len(queue) != 0:
            currNode = queue.pop()
            print(currNode.val, end=" ")

            if currNode.left:
                temp.appendleft(currNode.left)

            if currNode.right:
                temp.appendleft(currNode.right)

        queue = temp

# basic dfs level-order transversal
# runtime: O(n), memory: O(n)
def printDFSLevelOrder(root):
    # {level, [val]}
    data = {}
    def dfs(root, level):
        if level in data:
            data[level].append(root.val)
        else:
            data[level] = [root.val]

        if root.left:
            ''' WRONG: This two lines and the dfs(root.left, level+1) below is different '''
            # level += 1
            # dfs(root.left, level)

            dfs(root.left, level+1)
            # print(level)

        if root.right:
            dfs(root.right, level+1)

    dfs(root, 0)
    # print(data)

    # runtime: 2log(n)
    for key, value in data.items():
        for v in value:
            print(v, end=" ")


if __name__ == '__main__':
    root = newNode(4)
    insertIntoBST(root, 2)
    insertIntoBST(root, 7)
    insertIntoBST(root, 1)
    insertIntoBST(root, 3)
    insertIntoBST(root, 5)

    printBFSLevelOrder(root)
    print("")
    printDFSLevelOrder(root)





