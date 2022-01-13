# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional
from collections import deque

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

''' example of misuse left and right val that is solved by passing a parameter
    value passing in a parameter will not calculate in this recursion but wait until next recursion '''
# runtime: O(n), memory: O(1)
def sumRootToLeaf_M1(root: Optional[TreeNode]) -> int:
    sumRoot = 0

    def dfs(root, num):
        nonlocal sumRoot

        if root.left:
            ''' this line is incorrect b/c the code add left val before a recursive call, so when returning the num will already be changed '''
            # num = num + str(root.left.val)
            # dfs(root.left, num)
            dfs(root.left, num + str(root.left.val))

        if root.right:
            dfs(root.right, num + str(root.right.val))

        if root and not root.left and not root.right:
            sumRoot += int(num, 2)

    dfs(root, str(root.val))
    return sumRoot

''' example of misuse left and right val that is solved by using root.val '''
# runtime: O(n), memory: O(1)
def sumRootToLeaf_M2(root: Optional[TreeNode]) -> int:
    sumRoot = 0

    def dfs(root, num):
        nonlocal sumRoot

        num = num + str(root.val)

        if root.left:
            ''' this line is incorrect b/c the code add left val before a recursive call, so when returning the num will already be changed '''
            # num = num + str(root.left.val)
            dfs(root.left, num)

        if root.right:
            dfs(root.right, num)

        if root and not root.left and not root.right:
            sumRoot += int(num, 2)

    dfs(root, "")
    return sumRoot

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




