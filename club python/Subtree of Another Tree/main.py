from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(root1, root2):
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1 and root2:
            if root1.val != root2.val:
                return False
            if not isSameTree(root1.left, root2.left) or not isSameTree(root1.right, root2.right):
                return False
        return True

    def dfs(root, subRoot):
        if subRoot is None and root is None:
            return True
        if root and subRoot and root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        if root and dfs(root.left, subRoot) or root and dfs(root.right, subRoot):
            return True
        return False

    return dfs(root, subRoot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = TreeNode(4)
    root1.left = TreeNode(4)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.right = TreeNode(5)

    sub_root1 = TreeNode(4)
    sub_root1.left = TreeNode(1)
    sub_root1.right = TreeNode(2)

    non_sub_root1 = TreeNode(4)
    non_sub_root1.left = TreeNode(2)
    non_sub_root1.right = TreeNode(1)

    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)

    sub_root2 = TreeNode(2)
    sub_root2.left = TreeNode(0)

    print(isSubtree(root1, sub_root1)) # True
    print(isSubtree(root1, non_sub_root1)) # False
    print(isSubtree(root2, sub_root2))  # True
    print(isSubtree(root2, sub_root1))  # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
