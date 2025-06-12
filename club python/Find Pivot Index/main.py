from typing import List

'''
    Link: https://leetcode.com/problems/find-pivot-index
    Purpose: Find the pivot index where
           : The sum of all the numbers to the left of the index is equal to the sum of all the numbers to the index's right.
           : If the index is on the left most of the array, then the left sum is 0
           : If no such index exists, return -1
    parameter: List[int] - list of numbers
    return: int - the pivot index
    Pre-Condition: 1 <= nums.length <= 10^4
                 : -1000 <= nums[i] <= 1000
    Post-Condition: none
'''
def pivotIndex(nums: List[int]) -> int:
    right = sum(nums)
    left = 0
    prev = 0

    if left == right and len(nums) == 1:
        return 0

    for i in range(len(nums)):
        right = right - nums[i]
        left = left + prev
        prev = nums[i]
        if left == right:
            return i

    return -1

if __name__ == '__main__':
    print(pivotIndex([95, 91, 92, 93, 94, 88, 96]))  # 3
    print(pivotIndex([1,7,3,6,5,6])) # 3
    print(pivotIndex([1,2,3])) # -1
    print(pivotIndex([2,1,-1])) # 0
    print(pivotIndex([7])) # 0
