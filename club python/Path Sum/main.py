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
# runtime: O(n), memory: O(1)
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    sum = 0
    answer = False

    # note: b/c a tree can be empty, we must check if root exist
    if root is None:
        return False

    def dfs(root):
        nonlocal sum
        nonlocal answer

        sum += root.val

        if root.left:
            dfs(root.left)

        if root.right:
            dfs(root.right)

        # check if sum is equal to the targetSum
        if not root.left and not root.right and sum == targetSum:
            answer = True

        sum -= root.val

    dfs(root)
    return answer

# Credit: https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
"""function to insert element in binary tree """
def insert(temp, key):
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)


if __name__ == "__main__":
    root1 = newNode(3)
    root1.left = newNode(9)
    root1.right = newNode(20)
    root1.right.left = newNode(15)
    root1.right.right = newNode(7)

    print(hasPathSum(root1, 3)) # False
    print(hasPathSum(root1, 12)) # True
    print(hasPathSum(root1, 27)) # False

    root2 = newNode(5)
    root2.left = newNode(4)
    root2.right = newNode(8)
    root2.left.left = newNode(11)
    root2.right.left = newNode(13)
    root2.right.right = newNode(4)
    root2.left.left.left = newNode(7)
    root2.left.left.right = newNode(2)
    root2.right.right.right = newNode(1)

    print(hasPathSum(root2, 22))  # True
    print(hasPathSum(root2, 26))  # True
    print(hasPathSum(root2, 4))  # False
    print(hasPathSum(root2, 0))  # False



