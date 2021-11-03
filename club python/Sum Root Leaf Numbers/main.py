# Python program to insert element in binary tree
from idlelib.tree import TreeNode
from typing import Optional, List

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
    Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
    Purpose: Return the total sum of all root-to-leaf numbers
           : a root-to-leaf numbers is a number formed by concating all digits from root to leaf
    parameter: Optional[TreeNode] root: a root of binary tree
    return: int sum - the total sum of all root-to-leaf numbers
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : 0 <= Node.val <= 9
                 : The depth of the tree will not exceed 10.
    Post-Condition: none
'''
# runtime: best/average/worse O(n)/O(n)/O(n^2), space: O(1)
def sumNumbers_M1(root: Optional[TreeNode]) -> int:
    sum = 0
    nums = [] # store all possible numbers
    num = "" # to store concating digits from root to leap node

    def dfs(root: Optional[TreeNode]):
        nonlocal num
        # adding digit until reach null
        if root is not None:
            num += str(root.data)

        # collect a num (from concat digits) at leap node to a list
        if root.left is None and root.right is None:
            nums.append(int(num))
            return

        # pop 1 digit when transversing back by 1 node
        if root.left:
            dfs(root.left)
            num = num[:-1]

        # pop 1 digit when transversing back by 1 node
        if root.right:
            dfs(root.right)
            num = num[:-1]

    dfs(root)

    # find sum in the number list
    for n in nums:
        sum += n
    return sum

'''
    Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
    Purpose: Return the total sum of all root-to-leaf numbers
           : a root-to-leaf numbers is a number formed by concating all digits from root to leaf
    parameter: Optional[TreeNode] root: a root of binary tree
    return: int sum - the total sum of all root-to-leaf numbers
    Pre-Condition: The number of nodes in the tree is in the range [1, 1000].
                 : 0 <= Node.val <= 9
                 : The depth of the tree will not exceed 10.
    Post-Condition: none
'''
# runtime: O(n), space: best/average/worse O(1)/O(1)/O(n)
def sumNumbers_M2(root: Optional[TreeNode]) -> int:
    sum = 0
    nums = [] # store all possible numbers
    num = [] # a list of digits to store concating digits from root to leap node

    def dfs(root: Optional[TreeNode]):
        # adding digit until reach null
        if root is not None:
            num.append(str(root.data))

        # collect a num (from concat digits) at leap node to a list
        if root.left is None and root.right is None:
            nums.append(toNumber(num))
            return

        # pop 1 digit when transversing back by 1 node
        if root.left:
            dfs(root.left)
            num.pop()

        # pop 1 digit when transversing back by 1 node
        if root.right:
            dfs(root.right)
            num.pop()

    dfs(root)

    # find sum from the number list
    for n in nums:
        sum += n

    return sum

'''
    Purpose: Find concat a list of digits to a number
    parameter: List[int] nums: a list of digit(s)
    return: int - a number
    Pre-Condition: none
    Post-Condition: none
'''
# runtime: best/average/worse O(1)/O(1)/O(n) -> relative to the question, space: O(1)
def toNumber(nums: List[int]) -> int:
    number = ""
    for n in nums:
        number += n

    return int(number)

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
    root1.left = newNode(9)
    root1.right = newNode(0)
    root1.left.left = newNode(5)
    root1.left.right = newNode(1)

    root2 = newNode(1)
    root2.left = newNode(2)
    root2.right = newNode(3)

    root3 = newNode(1)
    root3.left = newNode(0)

    print("\n+===== method 1 =====+\n")
    print(sumNumbers_M1(root1))
    print(sumNumbers_M1(root2))
    print(sumNumbers_M1(root3))

    print("\n+===== method 2 =====+\n")
    print(sumNumbers_M2(root1))
    print(sumNumbers_M2(root2))
    print(sumNumbers_M2(root3))





