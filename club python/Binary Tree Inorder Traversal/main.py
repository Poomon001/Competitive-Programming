from idlelib.tree import TreeNode
from typing import List, Optional

class BSTNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    '''     
        Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
        Purpose: Return the inorder traversal of its nodes' values.
        Parameter: none
        Returns: : List[int] element - an inorder traversal
        Pre-Condition: The number of nodes in the tree is in the range [0, 100].
                     : -100 <= Node.val <= 100
        Post-Condition: none
    '''
    # runtime: O(n), memory: O(1)
    # left -> node -> right
    def inorderTraversal(self) -> List[int]:
        # returned list doesn't count toward memory
        element = []

        # add left
        if self.left:
            # bebugView = self.left.val
            element += self.left.inorderTraversal()

        # add base case node
        # bebugView = self.val
        element.append(self.val)

        # add left
        if self.right:
            # bebugView = self.right.val
            element += self.right.inorderTraversal()

        return element


    def add_child(self, data):
        # case 1: data is already exist then done need to add
        if data == self.val:
            return

        # case 2: data is less than curr data then go to left child
        if data < self.val:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BSTNode(data)

        # case 3: data is greater than curr data then go to right child
        if data > self.val:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BSTNode(data)


if __name__ == '__main__':
    root = BSTNode(10)
    root.add_child(15)
    root.add_child(14)
    root.add_child(7)
    root.add_child(100)
    print(root.inorderTraversal())
