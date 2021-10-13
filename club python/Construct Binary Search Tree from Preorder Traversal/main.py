from idlelib.tree import TreeNode
from typing import List, Optional
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    '''     
        Purpose: Construct a list from a tree to check if a tree valid (format: pre-order)
        Parameter: none
        Returns: List[int] ele - a list of number in a tree in a format of Pre-order
        Pre-Condition: none
        Post-Condition: none
    '''

    # run-time: O(n), memory: O(1)
    def pre_order_traversal(self) -> List[int]:
        elem = [] # doesnt count b/c it is a return

        # root -> left -> right
        # base case
        # bebugView = self.data
        elem.append(self.data)

        if self.left:
            # bebugView = self.left.data;
            elem += self.left.pre_order_traversal()

        if self.right:
            # bebugView = self.right.data;
            elem += self.right.pre_order_traversal()

        return elem

'''     
    Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
    Purpose: Construct the binart search tree and return its root from a given pre-order array
    Parameter: List[int] preorder - a list of numbers (in a format of preorder)
    Returns: Optional[TreeNode] root - A root of the tree
    Pre-Condition: 1 <= preorder.length <= 100
                 : 1 <= preorder[i] <= 108
                 : All the values of preorder are unique.
    Post-Condition: none
'''
# run-time: O(nlog(n)), memory: O(1)
def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    root = None

    # loop through each element and add them one by one to a tree
    for data in preorder:
        root = add_child(root, data)
    return root

'''     
    Purpose: Add an int to a BST
    Parameter: Optional[TreeNode] root - A root of the tree
             : int data - a number to insert
    Returns: Optional[TreeNode] root - A root of the tree
    Pre-Condition: none
    Post-Condition: none
'''
# run-time: O(log(n)), memory: O(1)
def add_child(root: Optional[TreeNode], data: int) -> Optional[TreeNode]:
    # case 1: tree is empty then we create a new tree
    if root == None:
        root = BSTNode(data)
    # case 2: data is less than the curr nodeTree data then we add to the left
    elif root.data > data:
        root.left = add_child(root.left, data)
    # case 3: data is more than the curr nodeTree data then we add to the right
    elif root.data < data:
        root.right = add_child(root.right, data)
    return root


if __name__ == "__main__":
    root = bstFromPreorder([8,5,1,7,10,12])
    print(root.pre_order_traversal()) # [8, 5, 1, 7, 10, 12]

    root = bstFromPreorder([1,3])
    print(root.pre_order_traversal()) # [1, 3]