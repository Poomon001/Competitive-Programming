from typing import List

'''
    Link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
    Purpose: Find the maximum length of a subarray that appears in both arrays.
    Parameter: List[int] nums1 - a list of integers
             : List[int] nums2 - a list of integers
    return: int maxLength - the maximum length of a subarray
    Pre-Condition: 1 <= nums1.length, nums2.length <= 1000
                 : 0 <= nums1[i], nums2[i] <= 100
    Post-Condition: None
'''
# dfs - runtime: O(n*m), memory: O(n*m)
def findLength(nums1: List[int], nums2: List[int]) -> int:
    board = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]
    maxLength = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if nums2[i - 1] == nums1[j - 1]:
                board[i][j] = board[i - 1][j - 1] + 1
            else:
                board[i][j] = 0

            maxLength = max(board[i][j], maxLength)

    return maxLength


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findLength([1,2,3,2,1], [1,2,3,2,1])) # 5
    print(findLength([1, 2, 3, 2, 1], [3,2,1,4,7])) # 3
    print(findLength([3,2,1,4,7], [1, 2, 3, 2, 1])) # 3
    print(findLength([0,0,0,0,0], [0,0,0,0,0])) # 5
    print(findLength([1, 1, 1, 1, 1], [1])) # 1
