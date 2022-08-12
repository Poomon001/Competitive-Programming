class TreeNode:
    def __init__(self,val=0,right=None, left=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    Purpose: Find the lowest common ancestor (LCA) node of two given nodes in the BST.
    parameter: TreeNode root - a BST 
               TreeNode p - a node 
               TreeNode root - a node 
    return: int - a value of the lowest common ancestor
    Pre-Condition: The number of nodes in the tree is in the range [2, 105].
                 : -109 <= Node.val <= 109
                 : All Node.val are unique.
                 : p != q
                 : p and q will exist in the BST.
'''
# two BST - runtime: O(log(n)), memory: O(log(n))
def lowestCommonAncestor_M1(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
    p1 = set()
    common_p = []
    head = root

    # find parents of p
    while root:
        p1.add(root)
        if root.val > p.val:
            root = root.left

        elif root.val < p.val:
            root = root.right

        elif root.val == p.val:
            break

    root = head

    # find all common parents between p and q
    while root:
        if root in p1:
            common_p.append(root)

        if root.val > q.val:
            root = root.left

        elif root.val < q.val:
            root = root.right

        elif root.val == q.val:
            break

    # return the lowest common parent
    return common_p[-1].val

# use the fact the the root is a value between p and q - runtime: O(log(n)), memory: O(1)
def lowestCommonAncestor_M2(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
    while root:
        if root.val > max(p.val, q.val):
            # decrease the root
            root = root.left
        elif root.val < min(p.val, q.val):
            # increase the root
            root = root.right
        else:
            return root.val

if __name__ == "__main__":
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    root1.right = TreeNode(8)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)

    print("\n+=== solution 1 ===+\n")
    print(lowestCommonAncestor_M1(root1, TreeNode(2), TreeNode(8))) # 6
    print(lowestCommonAncestor_M1(root1, TreeNode(2), TreeNode(4))) # 2
    print(lowestCommonAncestor_M1(root1, TreeNode(2), TreeNode(3))) # 2
    print(lowestCommonAncestor_M1(root1, TreeNode(5), TreeNode(4))) # 4
    print(lowestCommonAncestor_M1(root1, TreeNode(7), TreeNode(9))) # 8

    print("\n+=== solution 2 ===+\n")
    print(lowestCommonAncestor_M2(root1, TreeNode(2), TreeNode(8))) # 6
    print(lowestCommonAncestor_M2(root1, TreeNode(2), TreeNode(4))) # 2
    print(lowestCommonAncestor_M2(root1, TreeNode(2), TreeNode(3))) # 2
    print(lowestCommonAncestor_M2(root1, TreeNode(5), TreeNode(4))) # 4
    print(lowestCommonAncestor_M2(root1, TreeNode(7), TreeNode(9))) # 8