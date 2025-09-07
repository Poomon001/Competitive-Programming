from collections import deque, defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

'''
    Link: https://leetcode.com/problems/reorganize-string
    Purpose: Find the level order traversal of its nodes' values.
    parameter: Optional[TreeNode] root - a root node
    return: List[List[int]] - the level order traversal of its nodes' values
    Pre-Condition: The number of nodes in the tree is in the range [0, 2000].
                 : -1000 <= Node.val <= 1000
    Post-Condition: none
'''
# basic bfs level-order transversal
# runtime: O(n), memory: O(n)
def levelOrder_bfs(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    answer = []
    queue = deque()
    queue.append(root)
    while queue:
        level = []
        temp = deque()
        while queue:
            curr = queue.popleft()
            level.append(curr.val)

            if curr.left:
                temp.append(curr.left)
            if curr.right:
                temp.append(curr.right)
        queue = temp
        answer.append(level[:])

    return answer

'''
    Link: https://leetcode.com/problems/reorganize-string
    Purpose: Find the level order traversal of its nodes' values.
    parameter: Optional[TreeNode] root - a root node
    return: List[List[int]] - the level order traversal of its nodes' values
    Pre-Condition: The number of nodes in the tree is in the range [0, 2000].
                 : -1000 <= Node.val <= 1000
    Post-Condition: none
'''
# basic dfs level-order transversal
# runtime: O(n), memory: O(n)
def levelOrder_dfs(root: Optional[TreeNode]) -> List[List[int]]:
    # {level, []}
    level_to_elements = defaultdict(list)  # create a dict with empty list as a default

    def dfs(root, level):
        if root:
            level_to_elements[level].append(root.val)

            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

    dfs(root, 0)
    return [elements for _, elements in level_to_elements.items()]



def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # tree is empty
    if root is None:
        root = TreeNode(val)

    # go to left
    if root and root.val > val:
        if root.left:
            insertIntoBST(root.left, val)
        else:
            root.left = TreeNode(val)

    # go to right
    if root and root.val < val:
        if root.right:
            insertIntoBST(root.right, val)
        else:
            root.right = TreeNode(val)

    return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = TreeNode(4)
    insertIntoBST(root1, 2)
    insertIntoBST(root1, 7)
    insertIntoBST(root1, 1)
    insertIntoBST(root1, 3)
    insertIntoBST(root1, 5)

    root2 = TreeNode(4)

    root3 = TreeNode(4)
    insertIntoBST(root3, 10)
    insertIntoBST(root3, 7)

    root4 = TreeNode(4)
    insertIntoBST(root4, 2)
    insertIntoBST(root4, 7)

    print("\n+=== DFS Recursive  ===\n")
    print(levelOrder_dfs(root1))  # [[4], [2, 7], [1, 3, 5]]
    print(levelOrder_dfs(root2))  # [[4]]
    print(levelOrder_dfs(root3))  # [[4], [10], [7]]
    print(levelOrder_dfs(root4))  # [[4], [2, 7]]
    print("")

    print("\n+=== BFS By level  ===\n")
    print(levelOrder_bfs(root1))  # [[4], [2, 7], [1, 3, 5]]
    print(levelOrder_bfs(root2))  # [[4]]
    print(levelOrder_bfs(root3))  # [[4], [10], [7]]
    print(levelOrder_bfs(root4))  # [[4], [2, 7]]
    print("")
