# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import List

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
    Purpose: Find a list containing all the integers from two trees sorted in ascending order
    parameter: TreeNode root1 - a root of a binary search tree
             : TreeNode root2 - a root of a binary search tree
    return: List[int] ans - a list containing all the integers from two trees sorted in ascending order
    Pre-Condition: The number of nodes in each tree is in the range [1, 5000].
                 : -10^5 <= Node.val <= 10^5
                 : root1 and root2 are a root of BST
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    def inOrder(root: TreeNode) -> List[int]:
        li = []

        if root and root.left:
            li = li + inOrder(root.left)

        if root:
            li.append(root.val)

        if root and root.right:
            li = li + inOrder(root.right)

        return li

    li1 = inOrder(root1) # O(n)
    li2 = inOrder(root2) # O(n)
    ans = []

    i = 0  # keep track of li1
    j = 0  # keep track of li2

    # O(n)
    while i < len(li1) or j < len(li2):
        # all element in li1 were added
        if i >= len(li1):
            ans.append(li2[j])
            j += 1
            continue

        # all element in li2 were added
        if j >= len(li2):
            ans.append(li1[i])
            i += 1
            continue

        # add lower first
        if li1[i] > li2[j]:
            ans.append(li2[j])
            j += 1
        else:
            ans.append(li1[i])
            i += 1

    return ans

if __name__ == "__main__":
    root1 = newNode(2)
    root1.left = newNode(1)
    root1.right = newNode(4)

    root2 = newNode(1)
    root2.left = newNode(0)
    root2.right = newNode(3)

    root3 = newNode(1)
    root3.right = newNode(8)

    root4 = newNode(8)
    root4.left = newNode(1)

    print(getAllElements(root1, root2)) # [0, 1, 1, 2, 3, 4]
    print(getAllElements(root2, root1)) # [0, 1, 1, 2, 3, 4]
    print(getAllElements(root3, root2)) # [0, 1, 1, 3, 8]
    print(getAllElements(root1, root4)) # [1, 1, 2, 4, 8]
    print(getAllElements(root4, root3)) # [1, 1, 8, 8]


