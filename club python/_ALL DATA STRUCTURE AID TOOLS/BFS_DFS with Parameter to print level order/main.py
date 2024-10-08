from idlelib.tree import TreeNode
from typing import Optional
from collections import deque

class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# runtime: O(h) where h is height of the tree, memory: O(1)
def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # tree is empty
    if root is None:
        root = newNode(val)

    # go to left
    if root and root.val > val:
        if root.left:
            insertIntoBST(root.left, val)
        else:
            root.left = newNode(val)

    # go to right
    if root and root.val < val:
        if root.right:
            insertIntoBST(root.right, val)
        else:
            root.right = newNode(val)

    return root

'''
    1. have a queue1 store a parent
    2. create queue2 to store all the parent child
    3. pop parent from queue1. use the popped parent to get its left and right child and store them in queue2
    4. loop until all parents in queue1 is empty
    5. assign children tp parents (queue1 = queue2[:])
'''
''' show all elements in the same level + transverse bfs '''
'''
       1 
    2     9
  3   4 7   8
'''
# basic bfs level-order transversal
# runtime: O(n), memory: O(n)
def printBFSLevelOrder_ByLevel(root):
    queue = deque()
    queue.appendleft(root)

    while len(queue) != 0:
        temp = deque()

        while len(queue) != 0:
            currNode = queue.pop()
            print(currNode.val, end=" ")

            if currNode.left:
                temp.appendleft(currNode.left)

            if currNode.right:
                temp.appendleft(currNode.right)

        queue = temp


'''
    1. have a recursive call  to imitate stac: memory - O(log(n)) = O(tree's depth)
    2. recursive call on left and right to transverse the whole tree
'''
# basic dfs level-order transversal
# recursion with parameter
# runtime: O(n), memory: O(n)
def printDFSLevelOrder_Recursive(root):
    # {level, [val]}
    data = {}
    def dfs(root, level):
        if level in data:
            data[level].append(root.val)
        else:
            data[level] = [root.val]

        if root.left:
            ''' WRONG: This two lines and the dfs(root.left, level+1) below is different '''
            # level += 1
            # dfs(root.left, level)

            dfs(root.left, level+1)
            # print(level)
        if root.right:
            dfs(root.right, level + 1)

    dfs(root, 0)
    # print(data)

    # runtime: 2log(n)
    for key, value in data.items():
        for v in value:
            print(v, end=" ")

if __name__ == '__main__':
    root1 = newNode(4)
    insertIntoBST(root1, 2)
    insertIntoBST(root1, 7)
    insertIntoBST(root1, 1)
    insertIntoBST(root1, 3)
    insertIntoBST(root1, 5)

    print("\n+=== DFS Recursive  ===\n")
    printDFSLevelOrder_Recursive(root1) # 4 2 7 1 3 5
    print("")

    print("\n+=== BFS By level  ===\n")
    printBFSLevelOrder_ByLevel(root1)  # 4 2 7 1 3 5
    print("")




