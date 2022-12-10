from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Link: https://leetcode.com/problems/leaf-similar-trees/
    Purpose: Determine if the all leaves of the first tree are the same as the second tree (both value and order)
    parameter: Optional[TreeNode] - root
             : Optional[TreeNode] - root
    return: bool - true if sm=ame. Otherwise false
    Pre-Condition: The number of nodes in each tree will be in the range [1, 200].
                 : Both of the given trees will have values in the range [0, 200].
    Post-Condition: none
'''
# runtime - O(n), memory - O(log(n))
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    sequence = []

    def dfs(root):
        if root and not root.left and not root.right:
            sequence.append(root.val)

        if root and root.left:
            dfs(root.left)

        if root and root.right:
            dfs(root.right)

    dfs(root1)
    sequence2 = sequence[:]
    sequence = []
    dfs(root2)

    return sequence == sequence2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    ''' same root'''

    root2 = TreeNode(4)
    root2.left = TreeNode(10)
    root2.right = TreeNode(1)
    root2.right.left = TreeNode(9)
    root2.right.right = TreeNode(8)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(20)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(4)

    ''' differnt order leafs'''

    root3 = TreeNode(4)
    root3.left = TreeNode(10)
    root3.right = TreeNode(1)
    root3.right.left = TreeNode(8)
    root3.right.right = TreeNode(9)
    root3.left.left = TreeNode(6)
    root3.left.right = TreeNode(20)
    root3.left.right.left = TreeNode(7)
    root3.left.right.right = TreeNode(4)

    ''' extra leaf '''
    root4 = TreeNode(4)
    root4.left = TreeNode(10)
    root4.right = TreeNode(1)
    root4.right.left = TreeNode(8)
    root4.right.right = TreeNode(-1)
    root4.right.right.left = TreeNode(10)
    root4.right.right.right = TreeNode(9)
    root4.left.left = TreeNode(6)
    root4.left.right = TreeNode(20)
    root4.left.right.left = TreeNode(7)
    root4.left.right.right = TreeNode(4)

    ''' missing leaf '''
    root5 = TreeNode(4)
    root5.left = TreeNode(10)
    root5.right = TreeNode(1)
    root5.right.right = TreeNode(9)
    root5.left.left = TreeNode(6)
    root5.left.right = TreeNode(20)
    root5.left.right.left = TreeNode(7)
    root5.left.right.right = TreeNode(4)

    print(leafSimilar(root1, root1)) # True
    print(leafSimilar(root1, root2))  # True
    print(leafSimilar(root1, root3))  # False
    print(leafSimilar(root1, root4))  # False
    print(leafSimilar(root1, root5))  # False
