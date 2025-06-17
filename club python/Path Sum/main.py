# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/path-sum/
    Purpose: Determine if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    parameter: Optional[TreeNode] root - a root of a binary tree
             : targetSum - int: an integer target
    return: bool answer -  return true if the tree has a root-to-leaf path such that adding up all the values along     
          : the path equals targetSum. Otherwise return false.
    Pre-Condition: The number of nodes in the tree is in the range [0, 5000].
                 : -1000 <= Node.val <= 1000
                 : -1000 <= targetSum <= 1000
    Post-Condition: none
'''
# dfs with nonlocal - runtime: O(n), memory: O(depth of tree)
def hasPathSum_M1(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    ans = False

    def dfs(root, targetSum):
        nonlocal ans
        if not root.left and not root.right and targetSum == 0:
            ans = True
            return

        if root.left:
            dfs(root.left, targetSum - root.left.val)

        if root.right:
            dfs(root.right, targetSum - root.right.val)

    dfs(root, targetSum - root.val)
    return ans

'''
    Link: https://leetcode.com/problems/path-sum/
    Purpose: Determine if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    parameter: Optional[TreeNode] root - a root of a binary tree
             : targetSum - int: an integer target
    return: bool answer -  return true if the tree has a root-to-leaf path such that adding up all the values along     
          : the path equals targetSum. Otherwise return false.
    Pre-Condition: The number of nodes in the tree is in the range [0, 5000].
                 : -1000 <= Node.val <= 1000
                 : -1000 <= targetSum <= 1000
    Post-Condition: none
'''
# dfs without nonlocal - runtime: O(n), memory: O(depth of tree)
def hasPathSum_M2(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    def dfs(root, targetSum):
        if root:
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                return True

            return dfs(root.left, targetSum) or dfs(root.right, targetSum)

        return False

    return dfs(root, targetSum)

if __name__ == "__main__":
    root1 = newNode(3)
    root1.left = newNode(9)
    root1.right = newNode(20)
    root1.right.left = newNode(15)
    root1.right.right = newNode(7)

    root2 = newNode(5)
    root2.left = newNode(4)
    root2.right = newNode(8)
    root2.left.left = newNode(11)
    root2.right.left = newNode(13)
    root2.right.right = newNode(4)
    root2.left.left.left = newNode(7)
    root2.left.left.right = newNode(2)
    root2.right.right.right = newNode(1)

    print("\n === Solution 1 === \n")
    print(hasPathSum_M1(root1, 3))  # False
    print(hasPathSum_M1(root1, 12))  # True
    print(hasPathSum_M1(root1, 27))  # False
    print(hasPathSum_M1(root2, 22))  # True
    print(hasPathSum_M1(root2, 26))  # True
    print(hasPathSum_M1(root2, 4))  # False
    print(hasPathSum_M1(root2, 0))  # False

    print("\n === Solution 2 === \n")
    print(hasPathSum_M2(root1, 3))  # False
    print(hasPathSum_M2(root1, 12))  # True
    print(hasPathSum_M2(root1, 27))  # False
    print(hasPathSum_M2(root2, 22))  # True
    print(hasPathSum_M2(root2, 26))  # True
    print(hasPathSum_M2(root2, 4))  # False
    print(hasPathSum_M2(root2, 0))  # False


