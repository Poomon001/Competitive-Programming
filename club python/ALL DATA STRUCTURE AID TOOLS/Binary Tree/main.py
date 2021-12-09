# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    root1 = newNode(3)
    root1.left = newNode(9)
    root1.right = newNode(20)
    root1.right.left = newNode(15)
    root1.right.right = newNode(7)
