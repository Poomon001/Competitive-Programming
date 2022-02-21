from typing import Optional
from collections import deque
class Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

'''
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Purpose: Determine the depth of a tree
    parameter: Optional[TreeNode] root - a root of a tree
    return: int - a depth of a tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 104].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# recursive non-local solution: runtime: O(n), memory: O(depth of tree)
def maxDepth_M1(root: Optional[Node]) -> int:
    depth = 0
    maxDepth = 0

    def dfs(root):
        nonlocal depth
        nonlocal maxDepth

        if root:
            depth += 1
            maxDepth = max(maxDepth, depth)

        if root and root.left:
            dfs(root.left)
            depth -= 1

        if root and root.right:
            dfs(root.right)
            depth -= 1

    dfs(root)
    return maxDepth

'''
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Purpose: Determine the depth of a tree
    parameter: Optional[TreeNode] root - a root of a tree
    return: int - a depth of a tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 104].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# recursive passing parameter solution: runtime: O(n), memory: O(log(n))
def maxDepth_M2(root: Optional[Node]) -> int:
    maxDepth = 0

    def dfs(root, depth):
        nonlocal maxDepth
        if root:
            if not root.left and not root.right:
                maxDepth = max(maxDepth, depth)

            if root.left:
                dfs(root.left, depth + 1)

            if root.right:
                dfs(root.right, depth + 1)

    dfs(root, 1)
    return maxDepth

'''
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Purpose: Determine the depth of a tree
    parameter: Optional[TreeNode] root - a root of a tree
    return: int - a depth of a tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 104].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# recursive return solution: runtime: O(n), memory: O(log(n))
def maxDepth_M3(root: Optional[Node]) -> int:
    def dfs(root, depth):

        if root:
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            return max(left, right)

        return depth

    return dfs(root, 0)

'''
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Purpose: Determine the depth of a tree
    parameter: Optional[TreeNode] root - a root of a tree
    return: int - a depth of a tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 104].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# stack iteration solution: runtime: O(n), memory: O(log(n))
def maxDepth_M4(root: Optional[Node]) -> int:
    # {parent node, level}
    stack = deque()
    stack.append([root, 1])
    visited = set()
    maxDepth = 0

    if not root:
        return 0

    while stack:
        currNode,depth = stack.pop()

        if currNode not in visited:
            visited.add(currNode)

            if not currNode.left and not currNode.right:
                maxDepth = max(depth, maxDepth)
            else:
                # add {children, their level (currLevel + 1)}
                if currNode.right:
                    stack.append([currNode.right, depth+1])

                if currNode.left:
                    stack.append([currNode.left, depth+1])

    return maxDepth


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = Node(3)
    root1.left = Node(9)
    root1.right = Node(20)
    root1.right.left = Node(15)
    root1.right.right = Node(7)

    root2 = Node(3)
    root2.left = Node(9)
    root2.right = Node(20)
    root2.left.left = Node(15)
    root2.left.right = Node(7)

    root3 = Node(1)
    root3.left = Node(2)

    root4 = Node(1)
    root4.left = Node(7)
    root4.left.left = Node(2)
    root4.left.left.left = Node(0)
    root4.left.left.left.left = Node(9)
    root4.left.left.left.left.left = Node(8)
    root4.left.left.left.left.left.left = Node(5)

    print("\n+=== recursive non-local solution ===+\n")
    print(maxDepth_M1(root1))  # 3
    print(maxDepth_M1(root2))  # 3
    print(maxDepth_M1(root3))  # 2
    print(maxDepth_M1(root4))  # 7

    print("\n+=== recursive passing parameter solution ===+\n")
    print(maxDepth_M2(root1))  # 3
    print(maxDepth_M2(root2))  # 3
    print(maxDepth_M2(root3))  # 2
    print(maxDepth_M2(root4))  # 7

    print("\n+=== recursive return solution ===+\n")
    print(maxDepth_M3(root1))  # 3
    print(maxDepth_M3(root2))  # 3
    print(maxDepth_M3(root3))  # 2
    print(maxDepth_M3(root4))  # 7

    print("\n+=== stack iteration solution ===+\n")
    print(maxDepth_M4(root1)) # 3
    print(maxDepth_M4(root2)) # 3
    print(maxDepth_M4(root3))  # 2
    print(maxDepth_M4(root4))  # 7


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
