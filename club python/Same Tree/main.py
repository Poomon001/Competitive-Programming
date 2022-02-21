from typing import Optional
from collections import deque
class Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

'''
    Link: https://leetcode.com/problems/same-tree/
    Purpose: Determine if two input tree are the same or not
    parameter: Optional[TreeNode] p - a root of a tree
             : Optional[TreeNode] q - a root of a tree
    return: bool ans - True is they are the same. Otherwise false
    Pre-Condition: The number of nodes in both trees is in the range [0, 100].
                 : -10^4 <= Node.val <= 10^4
    Post-Condition: none
'''
# DFS solution: runtime: O(n), memory: O(depth of tree)
def isSameTree_M1(p: Optional[Node], q: Optional[Node]) -> bool:
    ans = True
    def dfs(p: Optional[Node], q: Optional[Node]) -> bool:
        nonlocal ans
        # check if already check all left and right nodes
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            # check if both tree has the same left structures
            if (p.left and not q.left) or (not p.left and q.left):
                ans = False

            # check if both tree has the same right structures
            if (p.right and not q.right) or (not p.right and q.right):
                ans = False

            if p.left and q.left:
                dfs(p.left, q.left)

            if p.right and q.right:
                dfs(p.right, q.right)
        else:
            ans = False

    dfs(p, q)
    return ans

'''
    Link: https://leetcode.com/problems/same-tree/
    Purpose: Determine if two input tree are the same or not
    parameter: Optional[TreeNode] p - a root of a tree
             : Optional[TreeNode] q - a root of a tree
    return: bool - True is they are the same. Otherwise false
    Pre-Condition: The number of nodes in both trees is in the range [0, 100].
                 : -10^4 <= Node.val <= 10^4
    Post-Condition: none
'''
# BFS solution: runtime: O(n), memory: O(m) where m is a number of elements in a level that contains highest elements
def isSameTree_M2(p: Optional[Node], q: Optional[Node]) -> bool:
    queue = deque()
    queue.append([p, q])
    while queue:
        temp = deque()
        while queue:
            # pop parent node
            curr = queue.popleft() # pair [p, q]
            rootP = curr[0]
            rootQ = curr[1]

            # add children nodes to temp
            if rootP and rootQ and rootP.val == rootQ.val:
                temp.append([rootP.left, rootQ.left])
                temp.append([rootP.right, rootQ.right])

            # check if both trees have the same structure
            elif rootP or rootQ:
                return False

        queue = temp
    return True

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
    root2.right.left = Node(15)
    root2.right.right = Node(7)

    root3 = Node(3)
    root3.left = Node(9)
    root3.right = Node(20)

    root4 = Node(3)
    root4.left = Node(9)
    root4.right = Node(20)

    root5 = Node(3)
    root5.left = Node(9)

    root6 = Node(3)
    root6.left = Node(-9)

    root7 = Node(3)

    root8 = Node(3)
    root8.right = Node(2)

    print("\n+=== DFS solution ===+\n")
    print(isSameTree_M1(root1, root2)) # True
    print(isSameTree_M1(root3, root4)) # True
    print(isSameTree_M1(root5, root6)) # False
    print(isSameTree_M1(root7, root8)) # False

    print("\n+=== BFS solution ===+\n")
    print(isSameTree_M2(root1, root2))  # True
    print(isSameTree_M2(root3, root4))  # True
    print(isSameTree_M2(root5, root6))  # False
    print(isSameTree_M2(root7, root8))  # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
