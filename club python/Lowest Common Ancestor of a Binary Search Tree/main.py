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
# brute force - runtime: O(n), memory: O(n)
def lowestCommonAncestor_M1(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
    # LCA node is the last node that has a value between p and q inclusively in bst
    parents = []

    def dfs(root):
        if root:
            if p.val < root.val < q.val or q.val < root.val < p.val or root.val == q.val or root.val == p.val:
                parents.append(root)

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

    dfs(root)

    return parents[0].val


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
# two BST - runtime: O(log(n), memory: O(log(n))
def lowestCommonAncestor_M2(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
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
# use bst iteratively (can iterate through bst only) - runtime: O(log(n)), memory: O(1)
def lowestCommonAncestor_M3(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
    # LCA node is the first node that has a value between p and q inclusively in bst
    while root:
        if root.val > p.val and root.val > q.val:
            # decrease the root
            root = root.left
        elif root.val < p.val and root.val < q.val:
            # increase the root
            root = root.right
        else:
            return root.val

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
# use bst recursively - runtime: O(log(n)), memory: O(1)
def lowestCommonAncestor_M4(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
    # LCA node is the first node that has a value between p and q inclusively in bst
    lca = root

    def dfs(root):
        nonlocal lca
        if root:
            lca = root
            if root.val < p.val and root.val < q.val:
                # need to search on high side (right)
                dfs(root.right)
            elif root.val > p.val and root.val > q.val:
                # need to search on lower side (left)
                dfs(root.left)
            else:
                # two value split (we are at the middle), this is answer
                return

    dfs(root)

    return lca.val

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

    print("\n+=== solution 3 ===+\n")
    print(lowestCommonAncestor_M3(root1, TreeNode(2), TreeNode(8)))  # 6
    print(lowestCommonAncestor_M3(root1, TreeNode(2), TreeNode(4)))  # 2
    print(lowestCommonAncestor_M3(root1, TreeNode(2), TreeNode(3)))  # 2
    print(lowestCommonAncestor_M3(root1, TreeNode(5), TreeNode(4)))  # 4
    print(lowestCommonAncestor_M3(root1, TreeNode(7), TreeNode(9)))  # 8

    print("\n+=== solution 4 ===+\n")
    print(lowestCommonAncestor_M4(root1, TreeNode(2), TreeNode(8)))  # 6
    print(lowestCommonAncestor_M4(root1, TreeNode(2), TreeNode(4)))  # 2
    print(lowestCommonAncestor_M4(root1, TreeNode(2), TreeNode(3)))  # 2
    print(lowestCommonAncestor_M4(root1, TreeNode(5), TreeNode(4)))  # 4
    print(lowestCommonAncestor_M4(root1, TreeNode(7), TreeNode(9)))  # 8