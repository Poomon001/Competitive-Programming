from collections import Counter
from idlelib.tree import TreeNode
from typing import Optional


class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree
    Purpose: Find the number of pseudo-palindromic paths going from the root node to leaf nodes
    parameter: Optional[TreeNode] root - a root of a binary search tree
    return: int pseudoPalindromic - the number of pseudo-palindromic paths going from the root node to leaf nodes
    Pre-Condition: The number of nodes in the tree is in the range [1, 10^3].
                 : 1 <= Node.val <= 9
    Post-Condition: none
'''
def pseudoPalindromicPaths(root: Optional[TreeNode]) -> int:
    pathToLeaf = []
    pseudoPalindromic = 0

    def dfs(root):
        nonlocal pseudoPalindromic
        pathToLeaf.append(root.val)

        if not root.left and not root.right:
            numToFreq = Counter(pathToLeaf)
            odd = 0
            for _, freq in numToFreq.items():
                if freq % 2 != 0:
                    odd += 1
            pseudoPalindromic += 0 if odd > 1 else 1

        if root.left:
            dfs(root.left)
            pathToLeaf.pop()

        if root.right:
            dfs(root.right)
            pathToLeaf.pop()

    dfs(root)
    return pseudoPalindromic


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = newNode(2)
    root1.left = newNode(1)
    root1.right = newNode(1)

    root2 = newNode(2)
    root2.left = newNode(3)
    root2.right = newNode(1)
    root2.left.left = newNode(3)
    root2.left.right = newNode(1)
    root2.right.right = newNode(1)

    root3 = newNode(2)
    root3.left = newNode(1)
    root3.right = newNode(1)
    root3.left.left = newNode(1)
    root3.left.right = newNode(3)
    root3.left.right.left = newNode(1)

    print(pseudoPalindromicPaths(root1)) # 0
    print(pseudoPalindromicPaths(root2)) # 2
    print(pseudoPalindromicPaths(root3)) # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
