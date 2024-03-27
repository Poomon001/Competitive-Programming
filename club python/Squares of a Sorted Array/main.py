from typing import List

'''
    Link: https://leetcode.com/problems/squares-of-a-sorted-array
    Purpose: Given an integer array nums sorted in non-decreasing order. 
           : Find an array of the squares of each number sorted in non-decreasing order
    parameter: int[] nums - an positive/negative integer array
    return: int[] ans - an array of the squares of each number sorted in non-decreasing order
    Pre-Condition: 1 <= nums.length <= 10^4
                 : -10^4 <= nums[i] <= 10^4
    Post-Condition: none
'''
# DP - runtime: O(n), memory: O(n)
def sortedSquares(nums: List[int]) -> List[int]:
    ans = [0 for _ in nums]

    left = 0
    right = len(nums) - 1
    i = right

    while right >= left:
        if abs(nums[right]) > abs(nums[left]):
            ans[i] = nums[right] * nums[right]
            right -= 1
        else:
            ans[i] = nums[left] * nums[left]
            left += 1
        i -= 1
    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10])) # [0, 1, 9, 16, 100]
    print(sortedSquares([-7,-3,2,3,11])) # [4, 9, 9, 49, 121]
    print(sortedSquares([5])) # [25]
    print(sortedSquares([0,1,2,4])) # [0, 1, 4, 16]
    print(sortedSquares([-10,-3,-1,0])) # [0, 1, 9, 100]

