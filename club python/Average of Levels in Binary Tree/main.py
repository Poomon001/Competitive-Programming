# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List
from collections import deque

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
    Purpose: Find the average value of the nodes on each level in the form of an array
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int[float] answer - the average value of the nodes on each level
    Pre-Condition: The number of nodes in the tree is in the range [1, 10^4].
                 : -2^31 <= Node.val <= 2^31 - 1
    Post-Condition: none
'''
# dfs solution: runtime: O(n) where n is a number of nodes, memory: O(m) where m is the height of the tree
def averageOfLevels_M1(root: Optional[TreeNode]) -> List[float]:
    # {level, [sum, total numbers]}
    data = {} # memory: O(m)
    answer = [] # memory: O(m)
    level = 0
    # find sum of each level
    def dfs(root):
        nonlocal level

        if level not in data.keys():
            # init first sum in the level (0 + curr.val)
            data[level] = [root.val, 1]
        else:
            # increment sum (curr.sum + curr.val)
            data[level] = [data.get(level)[0] + root.val, data.get(level)[1] + 1]

        if root.left is not None:
            level += 1
            dfs(root.left)
            level -= 1

        if root.right is not None:
            level += 1
            dfs(root.right)
            level -= 1

    dfs(root)

    # find an average from sum in each level
    for d in data.values():
        totalSum = d[0]
        totalNum = d[1]
        answer.append(totalSum / totalNum)

    return answer

'''
    Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
    Purpose: Find the average value of the nodes on each level in the form of an array
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: int[float] answer - the average value of the nodes on each level
    Pre-Condition: The number of nodes in the tree is in the range [1, 10^4].
                 : -2^31 <= Node.val <= 2^31 - 1
    Post-Condition: none
'''
# bfs solution: runtime: O(n), memory: O(m) where n is the number of nodes, m is the number of max children nodes
def averageOfLevels_M2(root: Optional[TreeNode]) -> List[float]:
    # store all the current-level parents
    queue = deque()
    answer = []
    queue.appendleft(root)

    # bfs until no parent left
    while len(queue) != 0:
        # store all children of the current-level parents
        temp = deque()
        totalSum = 0
        totalNum = len(queue)

        # find sum of all current-level parents in the queue
        while len(queue) != 0:
            currNode = queue.pop()
            totalSum += currNode.val

            # add a left child of a current parent
            if currNode.left:
                temp.appendleft(currNode.left)

            # add a right child of a current parent
            if currNode.right:
                temp.appendleft(currNode.right)

        # make children to parents
        queue = temp
        answer.append(totalSum/totalNum)

    return answer


if __name__ == "__main__":
    root1 = newNode(3)
    root1.left = newNode(9)
    root1.right = newNode(20)
    root1.right.left = newNode(15)
    root1.right.right = newNode(7)

    root2 = newNode(3)
    root2.left = newNode(9)
    root2.right = newNode(20)
    root2.left.left = newNode(15)
    root2.left.right = newNode(7)

    root3 = newNode(3)

    root4 = newNode(3)
    root4.left = newNode(9)
    root4.right = newNode(20)
    root4.left.left = newNode(15)
    root4.left.right = newNode(7)
    root4.right.left = newNode(1)
    root4.right.right = newNode(9)

    root5 = newNode(3)
    root5.left = newNode(9)
    root5.right = newNode(20)
    root5.left.left = newNode(15)
    root5.left.right = newNode(7)
    root5.right.left = newNode(1)
    root5.right.right = newNode(9)
    root5.right.right.right = newNode(10)
    root5.left.left.right = newNode(15)

    print("\n+==== dfs solution ====+\n")
    print(averageOfLevels_M1(root1)) # [3.00000,14.50000,11.00000]
    print(averageOfLevels_M1(root2))  # [3.00000,14.50000,11.00000]
    print(averageOfLevels_M1(root3))  # [3.00000]
    print(averageOfLevels_M1(root4))  # [3.00000,14.50000,8.00000]
    print(averageOfLevels_M1(root5))  # [3.00000,14.50000,8.00000,12.50000]

    print("\n+==== bfs solution ====+\n")
    print(averageOfLevels_M2(root1))  # [3.00000,14.50000,11.00000]
    print(averageOfLevels_M2(root2))  # [3.00000,14.50000,11.00000]
    print(averageOfLevels_M2(root3))  # [3.00000]
    print(averageOfLevels_M2(root4))  # [3.00000,14.50000,8.00000]
    print(averageOfLevels_M2(root5))  # [3.00000,14.50000,8.00000,12.50000]


