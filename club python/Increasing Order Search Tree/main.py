class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def printAnswer(self):
        root = self
        def inOrder(root):
            if root:
                if root.left:
                    inOrder(root.left)

                print(root.val, end=" ")

                if not root.left and root.right:
                    print(None, end=" ")

                if root.right:
                    inOrder(root.right)

        inOrder(root)

'''
    Link: https://leetcode.com/problems/increasing-order-search-tree/
    Purpose: rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, 
           : and every node has no left child and only one right child.
    parameter: TreeNode root - a root of a bst
    return: TreeNode - return a tree that has no left child
    Pre-Condition: The number of nodes in the given tree will be in the range [1, 100].
                 : 0 <= Node.val <= 1000
    Post-Condition: none
'''
def increasingBST(root: TreeNode) -> TreeNode:
    ans = TreeNode(None)
    dummy = ans

    # left base right
    def inOrder(root):
        nonlocal dummy
        if root and root.left:
            inOrder(root.left)

        if root:
            dummy.right = TreeNode(root.val)
            dummy = dummy.right

        if root and root.right:
            inOrder(root.right)

    inOrder(root)

    return ans.right


if __name__ == "__main__":
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.left.left = TreeNode(2)
    root1.left.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    root1.right = TreeNode(6)
    root1.right.right = TreeNode(8)
    root1.right.right.left = TreeNode(7)
    root1.right.right.right = TreeNode(9)
    print(increasingBST(root1).printAnswer())

    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(7)
    print(increasingBST(root2).printAnswer())
