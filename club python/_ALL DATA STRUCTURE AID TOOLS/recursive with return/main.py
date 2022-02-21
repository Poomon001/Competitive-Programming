# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/sum-of-left-leaves/
    Purpose: Find a sum of left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : -1000 <= Node.val <= 1000
    Post-Condition: none
'''
# use nonlocal: runtime: O(n), memory: O(depth of tree)
def sumOfLeftLeaves_M1(root: Optional[TreeNode]) -> int:
    sum = 0

    def dfs(root: Optional[TreeNode]):
        nonlocal sum
        if root.left:
            # increment sum by a childNode.value if childNode is a left leaf node
            if not root.left.left and not root.left.right:
                sum = sum + root.left.data

            dfs(root.left)

        if root.right:
            dfs(root.right)

    dfs(root)

    return sum

'''
    Link: https://leetcode.com/problems/sum-of-left-leaves/
    Purpose: Find a sum of left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : -1000 <= Node.val <= 1000
    Post-Condition: none
'''
# increment sum: runtime: O(n), memory: O(depth of tree)
def sumOfLeftLeaves_M2(root: Optional[TreeNode]) -> int:
    def dfs(root: Optional[TreeNode]) -> int:
        sum = 0
        if root.left:
            if not root.left.left and not root.left.right:
                sum = sum + dfs(root.left) + root.left.data
            else:
                sum = sum + dfs(root.left)

        if root.right:
            sum = sum + dfs(root.right)

        return sum

    return dfs(root)

# Credit: https://www.geeksforgeeks.org/level-order-tree-traversal/
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

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

    print("M1:", sumOfLeftLeaves_M1(root1)) # 24
    print("M2:",sumOfLeftLeaves_M2(root1)) # 24
    print("+=====+")

    # now 9 is not a leap
    root1.left.right = newNode(3)

    print("M1:", sumOfLeftLeaves_M1(root1)) # 15
    print("M2:",sumOfLeftLeaves_M2(root1)) # 15
    print("+=====+")

    root1.left.left = newNode(10)

    print("M1:",sumOfLeftLeaves_M1(root1)) # 25
    print("M2:",sumOfLeftLeaves_M2(root1)) # 25
    print("+=====+")

    root1.right.right.left = newNode(5)

    print("M1:",sumOfLeftLeaves_M1(root1)) # 30
    print("M2:",sumOfLeftLeaves_M2(root1)) # 30
    print("+=====+")

