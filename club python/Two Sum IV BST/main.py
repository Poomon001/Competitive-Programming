from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

'''
    Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
    Purpose: Determine if BST contain a pair of integer whose sum is a target
    parameter: Optional[TreeNode] root - a binary search tree
             : int k - a target integer
    return: bool - true if the pair exist. Otherwise false
    Pre-Condition: The number of nodes in the tree is in the range [1, 104].
                 : -10^4 <= Node.val <= 10^4
                 : root is guaranteed to be a valid binary search tree.
                 : -10^5 <= k <= 10^5
    Post-Condition: none
'''
# dfs - runtime: O(n), memory: O(n)
def findTarget_m1(root: Optional[TreeNode], k: int) -> bool:
    # {k - number}
    pair = set()
    ans = False

    def dfs(root):
        nonlocal ans
        diff = k - root.val

        if root.val in pair:
            ans = True
            return
        else:
            pair.add(diff)

        if root and root.left:
            dfs(root.left)

        if root and root.right:
            dfs(root.right)

    dfs(root)
    return ans

# use inOrder transversal property - runtime: O(n), memory: O(n)
def findTarget_m2(root: Optional[TreeNode], k: int) -> bool:
    members = []

    # left -> node -> right
    def inOrder(root):
        if root and root.left:
            inOrder(root.left)

        members.append(root.val)

        if root and root.right:
            inOrder(root.right)

    inOrder(root)

    i = 0
    j = len(members) - 1
    while i < j:
        if members[i] + members[j] > k:
            j -= 1
        elif members[i] + members[j] < k:
            i += 1
        else:
            return True

    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right = TreeNode(6)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(0)

    root3 = TreeNode(1)
    root3.right = TreeNode(9)
    print("\n+=== solution 1 ===+\n")
    print(findTarget_m1(root1, 9)) # True
    print(findTarget_m1(root1, 28)) # False
    print(findTarget_m1(root1, 5)) # True


    print(findTarget_m1(root2, 0)) # False
    print(findTarget_m1(root2, 1)) # False

    print(findTarget_m1(root3, 10)) # True
    print(findTarget_m1(root3, -10)) # False

    print("\n+=== solution 2 ===+\n")
    print(findTarget_m2(root1, 9)) # True
    print(findTarget_m2(root1, 28)) # False
    print(findTarget_m2(root1, 5)) # True

    print(findTarget_m2(root2, 0)) # False
    print(findTarget_m2(root2, 1)) # False

    print(findTarget_m2(root3, 10)) # True
    print(findTarget_m2(root3, -10)) # False
