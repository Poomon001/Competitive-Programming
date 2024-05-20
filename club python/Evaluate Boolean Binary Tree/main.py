from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

'''
    Link: https://leetcode.com/problems/evaluate-boolean-binary-tree
    Purpose: Find the boolean evaluation of the full binary tree where
           : 1. Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True
           : 2. Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND
    parameter: Optional[TreeNode] root - a root of full binary tree
    return: bool - evaluation of the tree
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : 0 <= Node.val <= 3
                 : Every node has either 0 or 2 children.
                 : Leaf nodes have a value of 0 or 1.
                 : Non-leaf nodes have a value of 2 or 3.
    Post-Condition: none
'''
# post order: runtime: O(n), memory: O(n)
def evaluateTree_M1(root: Optional[TreeNode]) -> bool:
    dic = {0: False, 1: True}
    computationLine = []

    # post order: left > right > root
    def postOrder(root: Optional[TreeNode]):
        # visit left
        if root and root.left:
            postOrder(root.left)

        # visit right
        if root and root.right:
            postOrder(root.right)

        # visit root
        if root:
            if 2 <= root.val <= 3:
                # current val is an operation
                node1 = computationLine.pop()
                node2 = computationLine.pop()
                if root.val == 2:
                    computationLine.append(node1 or node2)
                else:
                    computationLine.append(node1 and node2)
            else:
                # current val is boolean value
                computationLine.append(dic[root.val])

    postOrder(root)
    return computationLine.pop()

'''
    Link: https://leetcode.com/problems/evaluate-boolean-binary-tree
    Purpose: Find the boolean evaluation of the full binary tree where
           : 1. Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True
           : 2. Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND
    parameter: Optional[TreeNode] root - a root of full binary tree
    return: bool - evaluation of the tree
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : 0 <= Node.val <= 3
                 : Every node has either 0 or 2 children.
                 : Leaf nodes have a value of 0 or 1.
                 : Non-leaf nodes have a value of 2 or 3.
    Post-Condition: none
'''
# recursive: runtime: O(n), memory: O(n)
def evaluateTree_M2(root: Optional[TreeNode]) -> bool:
    dic = {0: False, 1: True}

    def recursive(root):
        if root.val == 1 or root.val == 0:
            return dic[root.val]
        elif root.val == 2:
            return recursive(root.left) or recursive(root.right)
        elif root.val == 3:
            return recursive(root.left) and recursive(root.right)

    return recursive(root)

if __name__ == '__main__':
    root0 = TreeNode(0)

    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(0)

    root2 = TreeNode(3)
    root2.left = TreeNode(1)
    root2.right = TreeNode(0)

    root3 = TreeNode(2)
    root3.left = TreeNode(1)
    root3.right = TreeNode(3)
    root3.right.left = TreeNode(0)
    root3.right.right = TreeNode(1)

    root4 = TreeNode(2)
    root4.left = TreeNode(1)
    root4.right = TreeNode(3)
    root4.right.left = TreeNode(3)
    root4.right.right = TreeNode(1)
    root4.right.left.left = TreeNode(0)
    root4.right.left.right = TreeNode(0)

    root5 = TreeNode(2)
    root5.left = TreeNode(0)
    root5.right = TreeNode(3)
    root5.right.left = TreeNode(3)
    root5.right.right = TreeNode(1)
    root5.right.left.left = TreeNode(0)
    root5.right.left.right = TreeNode(0)

    print("\n === solution 1 === \n")
    print(evaluateTree_M1(root0)) # False
    print(evaluateTree_M1(root1)) # True
    print(evaluateTree_M1(root2)) # False
    print(evaluateTree_M1(root3)) # True
    print(evaluateTree_M1(root4)) # True
    print(evaluateTree_M1(root5))  # False

    print("\n === solution 2 === \n")
    print(evaluateTree_M2(root0)) # False
    print(evaluateTree_M2(root1)) # True
    print(evaluateTree_M2(root2)) # False
    print(evaluateTree_M2(root3)) # True
    print(evaluateTree_M2(root4)) # True
    print(evaluateTree_M2(root5)) # False
