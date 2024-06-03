# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List
from collections import deque

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/invert-binary-tree/
    Purpose: Invert Binary Tree
    parameter: Optional[TreeNode] root - a root of a completed binary tree
    return: Optional[TreeNode] root - an inverted of the binary tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 100].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# dfs - runtime: O(n), memory: O(log(n))
def invertTree_m1(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(root):
        if root:
            dummy = root.left
            root.left = root.right
            root.right = dummy
        if root and root.left:
            dfs(root.left)
        if root and root.right:
            dfs(root.right)

    dfs(root)
    return root

'''
    Link: https://leetcode.com/problems/invert-binary-tree/
    Purpose: Invert Binary Tree
    parameter: Optional[TreeNode] root - a root of a completed binary tree
    return: Optional[TreeNode] root - an inverted of the binary tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 100].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# bfs maintain level order - runtime: O(n), memory: O(log(n))
def invertTree_m2(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root
    queue = deque()
    queue.append(root)

    while queue:
        temp = deque() # help clearly maintain level order
        while queue:
            child = queue.popleft()

            dummy = child.left
            child.left = child.right
            child.right = dummy

            if child.right:
                temp.appendleft(child.right)
            if child.left:
                temp.appendleft(child.left)
        queue = temp
    return root

'''
    Link: https://leetcode.com/problems/invert-binary-tree/
    Purpose: Invert Binary Tree
    parameter: Optional[TreeNode] root - a root of a completed binary tree
    return: Optional[TreeNode] root - an inverted of the binary tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 100].
                 : -100 <= Node.val <= 100
    Post-Condition: none
'''
# bfs easy but not maintain level order - runtime: O(n), memory: O(log(n))
def invertTree_m3(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        left = node.left
        right = node.right
        node.left = right
        node.right = left

        if left:
            queue.append(left)

        if right:
            queue.append(right)

    return root


# Credit: https://www.geeksforgeeks.org/level-order-tree-traversal/
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)

# Credit: https://www.geeksforgeeks.org/level-order-tree-traversal/
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)

# Credit: https://www.geeksforgeeks.org/level-order-tree-traversal/
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

# Credit: https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
"""function to insert element in binary tree """
def insert(temp, key):
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)


if __name__ == "__main__":
    root1 = newNode(4)
    root1.left = newNode(2)
    root1.right = newNode(7)
    root1.left.left = newNode(1)
    root1.left.right = newNode(3)
    root1.right.left = newNode(6)
    root1.right.right = newNode(9)

    root2 = newNode(2)
    root2.left = newNode(1)
    root2.right = newNode(3)

    root3 = newNode(2)

    print("\n+=== test cases ===+\n")
    print(printLevelOrder(root1)) # 4 2 7 1 3 6 9
    print(printLevelOrder(root2)) # 2 1 3
    print(printLevelOrder(root3))  # 2

    print("\n+=== DFS solution ===+\n")
    print(printLevelOrder(invertTree_m1(root1)))  # 4 7 2 9 6 3 1
    print(printLevelOrder(invertTree_m1(root2)))  # 2 3 1
    print(printLevelOrder(invertTree_m1(root3)))  # 2

    print("\n+=== BFS solution 1 ===+\n")
    root4 = newNode(4)
    root4.left = newNode(2)
    root4.right = newNode(7)
    root4.left.left = newNode(1)
    root4.left.right = newNode(3)
    root4.right.left = newNode(6)
    root4.right.right = newNode(9)
    print(printLevelOrder(invertTree_m2(root4)))  # 4 7 2 9 6 3 1

    root5 = newNode(2)
    root5.left = newNode(1)
    root5.right = newNode(3)
    print(printLevelOrder(invertTree_m2(root5)))  # 2 3 1

    root6 = newNode(2)
    print(printLevelOrder(invertTree_m2(root6)))  # 2

    print("\n+=== BFS solution 2 ===+\n")
    print(printLevelOrder(invertTree_m3(root4)))  # 4 7 2 9 6 3 1
    print(printLevelOrder(invertTree_m3(root5)))  # 2 3 1
    print(printLevelOrder(invertTree_m3(root6)))  # 2



