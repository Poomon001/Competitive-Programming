from typing import List
'''
    Link: https://leetcode.com/problems/remove-element/
    Purpose: Remove all target val in an array nums in-place and return the total number of non-val in the array.
    parameter: List[int] nums - a list of integers
             : int val - an integer
    return: int i - total number of non-val in the array.
    Pre-Condition: 0 <= nums.length <= 100
                 : 0 <= nums[i] <= 50
                 : 0 <= val <= 100
    Post-Condition: none
'''
# two poi: O(n), memory: O(1)
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    ans = 0
    for j in range(len(nums)):
        if i < j and nums[j] != val:
            nums[i], nums[j] = nums[j], nums[i]

        while i < len(nums) and nums[i] != val:
            i += 1
    return i

if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    print(removeElement(nums1, 3)) # 2
    print(nums1) # [2, 2, 3, 3]

    nums2 = [0,1,2,2,3,0,4,2]
    print(removeElement(nums2, 2)) # 5
    print(nums2) # [0, 1, 3, 0, 4, 2, 2, 2]

    nums3 = [3, 2]
    print(removeElement(nums3, 3)) # 1
    print(nums3) # [2, 3]

    nums4 = [3,3]
    print(removeElement(nums4, 3)) # 0
    print(nums4) # [3, 3]

    nums5 = [0,1,2,5,2,3,0,4,2]
    print(removeElement(nums5, 2)) # 6
    print(nums5) # [0, 1, 5, 3, 0, 4, 2, 2, 2]