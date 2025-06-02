from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def isBalanced_M1(root: Optional[TreeNode]) -> bool:
    ans = True

    def dfs(root: Optional[TreeNode]):
        nonlocal ans
        if not root:
            return 0

        if root:
            left_height = dfs(root.left) + 1
            right_height = dfs(root.right) + 1

            if abs(left_height - right_height) > 1:
                ans = False

        # node's height is the max height of left and right children
        return max(left_height, right_height)

    dfs(root)
    return ans

def isBalanced_M2(root: Optional[TreeNode]) -> bool:
    ans = True

    def dfs(root: Optional[TreeNode], level: int):
        nonlocal ans
        if not root:
            return level

        if root:
            left_height = dfs(root.left, level + 1)
            right_height = dfs(root.right, level + 1)

            if abs(left_height - right_height) > 1:
                ans = False

        # node's height is the max height of left and right children
        return max(left_height, right_height)

    dfs(root, 0)
    return ans

def isBalanced_M3(root: Optional[TreeNode]) -> bool:
    def dfs(root: Optional[TreeNode]):
        if not root:
            return 0

        if root:
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if left_height == -1 or left_height == -1 or abs(left_height - right_height) > 1:
                return -1

        # node's height is the max height of left and right children
        return max(left_height, right_height) + 1

    return dfs(root) != -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root0 = TreeNode(0)

    root1 = TreeNode(0)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)

    root2 = TreeNode(0)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)

    root3 = TreeNode(0)
    root3.left = TreeNode(1)
    root3.right = TreeNode(2)
    root3.left.left = TreeNode(3)
    root3.left.left.left = TreeNode(4)

    root4 = TreeNode(0)
    root4.left = TreeNode(1)
    root4.right = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    root4.right.left = TreeNode(5)

    root5 = TreeNode(0)
    root5.left = TreeNode(1)
    root5.right = TreeNode(2)
    root5.left.left = TreeNode(3)
    root5.left.left.left = TreeNode(4)
    root5.left.right = TreeNode(5)
    root5.right.left = TreeNode(6)

    root6 = TreeNode(0)
    root6.left = TreeNode(1)
    root6.right = TreeNode(2)
    root6.left.left = TreeNode(3)
    root6.left.left.left = TreeNode(4)
    root6.right.right = TreeNode(5)
    root6.right.right.right = TreeNode(6)

    print("\n=== Solution 1 ===\n")
    print(isBalanced_M1(root1)) # True
    print(isBalanced_M1(root2)) # True
    print(isBalanced_M1(root3)) # False
    print(isBalanced_M1(root4)) # False
    print(isBalanced_M1(root5)) # True
    print(isBalanced_M1(root6)) # False

    print("\n=== Solution 2 ===\n")
    print(isBalanced_M2(root1))  # True
    print(isBalanced_M2(root2))  # True
    print(isBalanced_M2(root3))  # False
    print(isBalanced_M2(root4))  # False
    print(isBalanced_M2(root5))  # True
    print(isBalanced_M2(root6))  # False

    print("\n=== Solution 3 ===\n")
    print(isBalanced_M3(root1))  # True
    print(isBalanced_M3(root2))  # True
    print(isBalanced_M3(root3))  # False
    print(isBalanced_M3(root4))  # False
    print(isBalanced_M3(root5))  # True
    print(isBalanced_M3(root6))  # False

