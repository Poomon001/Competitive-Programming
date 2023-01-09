from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
    Purpose: Determine the preorder of binary tree
    parameter: Optional[TreeNode] - root
    return: List[int] - an array of preorder integer
    Pre-Condition: The number of nodes in the tree is in the range [0, 100].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# runtime - O(n), memory - O(n)
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    ans = []

    # pre-order: Node -> left -> right
    def dfs(root):
        if root:
            ans.append(root.val)
        if root and root.left:
            dfs(root.left)
        if root and root.right:
            dfs(root.right)

    dfs(root)
    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root0 = TreeNode(1)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(9)
    root2.right.right = TreeNode(7)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(5)

    root3 = TreeNode(21)
    root3.left = TreeNode(7)
    root3.right = TreeNode(14)
    root3.right.left = TreeNode(2)
    root3.right.right = TreeNode(2)
    root3.left.left = TreeNode(1)
    root3.left.right = TreeNode(1)
    root3.left.left.left = TreeNode(3)
    root3.left.left.right = TreeNode(3)

    print(preorderTraversal(root0)) # [1]
    print(preorderTraversal(root1)) # [1, 2, 3]
    print(preorderTraversal(root2)) # [4, 2, 3, 5, 9, 7]
    print(preorderTraversal(root3)) # [21, 7, 1, 3, 3, 1, 14, 2, 2]
