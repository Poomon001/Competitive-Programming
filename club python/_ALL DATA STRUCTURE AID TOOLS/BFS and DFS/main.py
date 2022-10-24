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

''' transverse bfs only '''
# basic bfs level-order transversal
# runtime: O(n), memory: O(n)
def printBFSLevelOrder(root):
    if not root:
        return root

    queue = deque()
    queue.append(root)

    while queue:
        child = queue.pop()
        print(child.val, end=" ")
        if child.left:
            queue.appendleft(child.left)
        if child.right:
            queue.appendleft(child.right)




'''
    1. have a recursive call  to imitate stac: memory - O(log(n)) = O(tree's depth)
    2. recursive call on left and right to transverse the whole tree
'''
# basic dfs level-order transversal
# recursion with parameter
# runtime: O(n), memory: O(n)
def printDFSLevelOrder_Recursive(root):
    def dfs(root):
        print(root.val, end = " ")
        if root.left:
            dfs(root.left)

        if root.right:
            dfs(root.right)

    dfs(root)

# basic dfs level-order transversal
# stack and while loop approach
# runtime: O(n), memory: O(n)
def printDFSLevelOrder_Stack_M1(root):
    stack = deque()
    stack.append(root)
    visited = set()

    while stack:
        currNode = stack.pop()
        if currNode not in visited:
            visited.add(currNode)
            print(currNode.val, end=" ")

            if currNode.right:
                stack.append(currNode.right)

            # add all children
            if currNode.left:
                stack.append(currNode.left)

# basic bfs level-order transversal
# runtime: O(n), memory: O(n)
def printBFSLevelOrder_Stack_M2(root):
    if not root:
        return root

    stack = deque()
    stack.append(root)

    while stack:
        child = stack.pop()
        print(child.val, end=" ")
        if child.right:
            stack.append(child.right)
        if child.left:
            stack.append(child.left)


if __name__ == '__main__':
    root1 = newNode(4)
    insertIntoBST(root1, 2)
    insertIntoBST(root1, 7)
    insertIntoBST(root1, 1)
    insertIntoBST(root1, 3)
    insertIntoBST(root1, 5)

    print("\n+=== DFS Recursive  ===\n")
    printDFSLevelOrder_Recursive(root1) # 4 2 1 3 7 5
    print("")

    root2 = newNode(4)
    insertIntoBST(root2, 2)
    insertIntoBST(root2, 7)
    insertIntoBST(root2, 1)
    insertIntoBST(root2, 3)
    insertIntoBST(root2, 5)

    print("\n+=== DFS Stack M1 ===\n")
    printDFSLevelOrder_Stack_M1(root2) # 4 2 1 3 7 5
    print("")

    root3 = newNode(4)
    insertIntoBST(root3, 2)
    insertIntoBST(root3, 7)
    insertIntoBST(root3, 1)
    insertIntoBST(root3, 3)
    insertIntoBST(root3, 5)

    print("\n+=== DFS Stack M2 ===\n")
    printBFSLevelOrder_Stack_M2(root3)  # 4 2 1 3 7 5
    print("")

    root4 = newNode(4)
    insertIntoBST(root4, 2)
    insertIntoBST(root4, 7)
    insertIntoBST(root4, 1)
    insertIntoBST(root4, 3)
    insertIntoBST(root4, 5)

    print("\n+=== BFS By level  ===\n")
    printBFSLevelOrder_ByLevel(root4)  # 4 2 7 1 3 5
    print("")

    root5 = newNode(4)
    insertIntoBST(root5, 2)
    insertIntoBST(root5, 7)
    insertIntoBST(root5, 1)
    insertIntoBST(root5, 3)
    insertIntoBST(root5, 5)

    print("\n+=== BFS Only Transverse  ===\n")
    printBFSLevelOrder(root5)  # 4 2 7 1 3 5
    print("")




