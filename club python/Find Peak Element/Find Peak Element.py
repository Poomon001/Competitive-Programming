from typing import List

'''
    Link: https://leetcode.com/problems/word-break/
    Purpose: Find a peak element if the element is greater than their two adjacent neighbors 
    parameter: List[int] nums - a list of numbers
    return: int - an index of a peak element
    Pre-Condition: 1 <= nums.length <= 1000
                 : -2^31 <= nums[i] <= 2^31 - 1
                 : nums[i] != nums[i + 1] for all valid i.
    Post-Condition: none
'''
# binary search - runtime: O(log(n)), memory: O(1)
def findPeakElement(nums: List[int]) -> int:
    # a reverse include 0th index in answers e.g 3, 2, 1, 0 where 3 > NULL and 3 > 2
    # a non-reverse include nth index in answers e.g 0, 1, 2, 3 where 3 > 2 and 3 > NULL
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if mid - 1 > 0 and mid + 1 < len(nums) - 1:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    findPeakElement([1, 2, 3, 1]) # 2
    findPeakElement([6,5,4,3,2,3,2]) # 0
    findPeakElement([1,2,1,3,1,6,1]) # 3
    findPeakElement([1]) # 1
    findPeakElement([1,2]) # 1
    findPeakElement([2,1]) # 0
    findPeakElement([1,2,1,3,5,6,7]) # 6
    findPeakElement([1,2,1,3,5,6,4]) # 5