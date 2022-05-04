from typing import List, Optional
from collections import deque
class TreeNode:
    # constructor
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # print tree level-order: runtime - O(n), memory - O(n)
    def printTree(self):
        root = self
        queue = deque()
        queue.append(root)
        printable = [root.val]
        while queue:
            temp = deque()
            while queue:
                curr = queue.popleft()
                if curr.left:
                    printable.append(curr.left.val)
                    temp.append(curr.left)
                else:
                    printable.append(None)

                if curr.right:
                    printable.append(curr.right.val)
                    temp.append(curr.right)
                else:
                    printable.append(None)
            queue = temp

        print(printable)

'''
    Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    Purpose: Build a height-balanced binary search tree from a assending order list
    parameter: List[int] nums - an integer
    return: Optional[TreeNode]: root
    Pre-Condition: 1 <= nums.length <= 10^4
                 : -10^4 <= nums[i] <= 10^4
                 : nums is sorted in a strictly increasing order.
    Post-Condition: none
'''

# recursive: runtime - O(n), memory - O(log(n))
def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    # middle element is the root
    def BST(nums: List[int]):
        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        middle = left + (right - left) // 2

        root = TreeNode(nums[middle])
        root.left = BST(nums[:middle])
        root.right = BST(nums[middle + 1:])

        return root

    return BST(nums)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    sortedArrayToBST([-10,-3,0,5,9]).printTree() # [0, -10, 5, None, -3, None, 9, None, None, None, None]
    sortedArrayToBST([1]).printTree() # [1, None, None]
    sortedArrayToBST([1,2]).printTree() # [1, None, 2, None, None]
    sortedArrayToBST([1,2,3,4,5]).printTree() # [3, 1, 4, None, 2, None, 5, None, None, None, None]
    sortedArrayToBST([1, 2, 3, 4, 5,6]).printTree() # [3, 1, 5, None, 2, 4, 6, None, None, None, None, None, None]
