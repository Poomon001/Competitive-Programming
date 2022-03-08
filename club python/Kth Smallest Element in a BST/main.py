from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Purpose: Given the root of a binary search tree, and an integer k. Find the kth smallest value
    parameter: Optional[Node] root - a head of BST
             : int k - an integer  
    return: int - the kth smallest value
    Pre-Condition: The number of nodes in the tree is n.
                 : 1 <= k <= n <= 104
                 : 0 <= Node.val <= 104
    Post-Condition: Do not alter the given tree
'''
# Solution 1 - not use BST property
# runtime: O(nlog(n)), memory: O(n)
def kthSmallest_M1(root: Optional[TreeNode], k: int) -> int:
    li = []

    def dfs(root: Optional[TreeNode]):
        if root and root.left:
            dfs(root.left)

        if root and root.right:
            dfs(root.right)

        if root:
            li.append(root.val)

    dfs(root)
    li.sort()

    return li[k - 1]

'''
    Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Purpose: Given the root of a binary search tree, and an integer k. Find the kth smallest value
    parameter: Optional[Node] root - a head of BST
             : int k - an integer  
    return: int - the kth smallest value
    Pre-Condition: The number of nodes in the tree is n.
                 : 1 <= k <= n <= 104
                 : 0 <= Node.val <= 104
    Post-Condition: Do not alter the given tree
'''
# Solution2 - use BST property - in-order transverse will give a sorted array
# runtime: O(n), memory: O(n)
def kthSmallest_M2(root: Optional[TreeNode], k: int) -> int:
    sortedList = []
    # visit left -> node -> right
    def inOrder(root: Optional[TreeNode]):
        if root:
            if root.left:
                inOrder(root.left)

            sortedList.append(root.val)

            if root.right:
                inOrder(root.right)

    inOrder(root)

    return sortedList[k - 1]

'''
    Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Purpose: Given the root of a binary search tree, and an integer k. Find the kth smallest value
    parameter: Optional[Node] root - a head of BST
             : int k - an integer  
    return: int - the kth smallest value
    Pre-Condition: The number of nodes in the tree is n.
                 : 1 <= k <= n <= 104
                 : 0 <= Node.val <= 104
    Post-Condition: Do not alter the given tree
'''
# Solution 3 - improve use BST property solution - in-order transverse will give sorted array + using index
# runtime: O(n), memory: O(height) = O(log(n)) -> stack frame
def kthSmallest_M3(root: Optional[TreeNode], k: int) -> int:
    ans = 0
    index = 0

    # visit left -> node -> right
    def inOrder(root):
        nonlocal ans
        nonlocal index
        if root:
            if root.left:
                inOrder(root.left)

            index += 1
            if index == k:
                ans = root.val

            if root.right:
                inOrder(root.right)

    inOrder(root)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    root3 = TreeNode(1)

    print("\n+=== solution1 ===+\n")
    print(kthSmallest_M1(root1, 1)) # 1
    print(kthSmallest_M1(root2, 3)) # 3
    print(kthSmallest_M1(root2, 6)) # 6
    print(kthSmallest_M1(root2, 1)) # 1
    print(kthSmallest_M1(root3, 1)) # 1

    print("\n+=== solution1 ===+\n")
    print(kthSmallest_M2(root1, 1)) # 1
    print(kthSmallest_M2(root2, 3)) # 3
    print(kthSmallest_M2(root2, 6)) # 6
    print(kthSmallest_M2(root2, 1)) # 1
    print(kthSmallest_M2(root3, 1)) # 1

    print("\n+=== solution1 ===+\n")
    print(kthSmallest_M3(root1, 1)) # 1
    print(kthSmallest_M3(root2, 3)) # 3
    print(kthSmallest_M3(root2, 6)) # 6
    print(kthSmallest_M3(root2, 1)) # 1
    print(kthSmallest_M3(root3, 1)) # 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
