# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional
from collections import deque

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
    Purpose: Find a sum of all binary left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of all binary left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : Node.val is 0 or 1.
    Post-Condition: none
'''
# runtime: O(n), memory: O(depth of tree)
def sumRootToLeaf_M1(root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(root: Optional[TreeNode], bits: str) -> int:
        nonlocal ans
        # if None
        if not root:
            return

            # if leaf
        if not root.left and not root.right:
            ans += int(bits + str(root.val), 2)

        dfs(root.left, bits + str(root.val))
        dfs(root.right, bits + str(root.val))

    dfs(root, "")
    return ans


'''
    Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
    Purpose: Find a sum of all binary left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of all binary left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : Node.val is 0 or 1.
    Post-Condition: none
'''
# runtime: O(n), memory: O(depth of tree)
def sumRootToLeaf_M2(root: Optional[TreeNode]) -> int:
    sumRoot = 0

    def dfs(root, num):
        nonlocal sumRoot

        num = num + str(root.val)

        if root.left:
            dfs(root.left, num)

        if root.right:
            dfs(root.right, num)

        # leaf node
        if root and not root.left and not root.right:
            sumRoot += int(num, 2)

    dfs(root, "")
    return sumRoot

'''
    Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
    Purpose: Find a sum of all binary left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of all binary left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : Node.val is 0 or 1.
    Post-Condition: none
'''
# runtime: O(n), memory: O(depth of tree)
def sumRootToLeaf_M3(root: Optional[TreeNode]) -> int:
    def dfs(root: Optional[TreeNode], bits: str) -> int:
        # if None
        if not root:
            return 0

        # if leaf
        if not root.left and not root.right:
            return int(bits + str(root.val), 2)

        return dfs(root.left, bits + str(root.val)) + dfs(root.right, bits + str(root.val))

    return dfs(root, "")

'''
    Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
    Purpose: Find a sum of all binary left leaves
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int sum - a sum of all binary left leaves
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : Node.val is 0 or 1.
    Post-Condition: none
'''
# ADVANCED math - runtime: O(n), memory: O(depth of tree)
def sumRootToLeaf_M4(root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(root: Optional[TreeNode], curr_sum: str) -> int:
        nonlocal ans
        # if None
        if not root:
            return

            # 1 0 1 = (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = (1)*2*2 + (0)*2 + (1)
        curr_sum = curr_sum * 2 + root.val

        # if leaf
        if not root.left and not root.right:
            ans += curr_sum

        dfs(root.left, curr_sum)
        dfs(root.right, curr_sum)

    dfs(root, 0)
    return ans

if __name__ == '__main__':
    root1 = newNode(1)
    root1.left = newNode(0)
    root1.right = newNode(1)
    root1.left.left = newNode(0)
    root1.left.right = newNode(1)
    root1.right.left = newNode(0)
    root1.right.right = newNode(1)

    root2 = newNode(0)

    root3 = newNode(1)
    root3.left = newNode(0)
    root3.right = newNode(1)

    root4 = newNode(1)
    root4.left = newNode(0)
    root4.right = newNode(1)
    root4.left.left = newNode(0)

    root5 = newNode(1)
    root5.left = newNode(0)
    root5.right = newNode(1)
    root5.left.left = newNode(0)
    root5.left.right = newNode(0)

    print("\n+=== Solution1 ===+\n")
    print(sumRootToLeaf_M1(root1)) # 22
    print(sumRootToLeaf_M1(root2)) # 0
    print(sumRootToLeaf_M1(root3)) # 5
    print(sumRootToLeaf_M1(root4)) # 7
    print(sumRootToLeaf_M1(root5))  # 11

    print("\n+=== Solution2 ===+\n")
    print(sumRootToLeaf_M2(root1))  # 22
    print(sumRootToLeaf_M2(root2))  # 0
    print(sumRootToLeaf_M2(root3))  # 5
    print(sumRootToLeaf_M2(root4))  # 7
    print(sumRootToLeaf_M2(root5))  # 11

    print("\n+=== Solution3 ===+\n")
    print(sumRootToLeaf_M3(root1))  # 22
    print(sumRootToLeaf_M3(root2))  # 0
    print(sumRootToLeaf_M3(root3))  # 5
    print(sumRootToLeaf_M3(root4))  # 7
    print(sumRootToLeaf_M3(root5))  # 11

    print("\n+=== Solution4 ===+\n")
    print(sumRootToLeaf_M4(root1))  # 22
    print(sumRootToLeaf_M4(root2))  # 0
    print(sumRootToLeaf_M4(root3))  # 5
    print(sumRootToLeaf_M4(root4))  # 7
    print(sumRootToLeaf_M4(root5))  # 11




