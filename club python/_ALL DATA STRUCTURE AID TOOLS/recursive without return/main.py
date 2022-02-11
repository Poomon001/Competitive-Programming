# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/count-complete-tree-nodes/
    Purpose: Count all nodes in a completed tree 
    parameter: Optional[TreeNode] root - a root of a completed binary tree
    return: int count - number of all nodes in the tree
    Pre-Condition: The number of nodes in the tree is in the range [0, 5 * 104].
                 : 0 <= Node.val <= 5 * 104
                 : The tree is guaranteed to be complete.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def swap(root: Optional[TreeNode]):
        if root:
            print("data1", "None" if root is None else root.data)
            dummy = root.left

            root.left = root.right
            root.right = dummy
        else:
            print("data2", "None" if root is None else root.data)
            return

        swap(root.left)
        print("data3", "None" if root is None else root.data)
        swap(root.right)
        print("data4", "None" if root is None else root.data)

    swap(root)
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

    print(printLevelOrder(root1)) # 4 2 7 1 3 6 9
    print(printLevelOrder(invertTree(root1))) # 4 7 2 9 6 3 1

