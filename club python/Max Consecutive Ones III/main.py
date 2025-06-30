from typing import List

'''
    Link: https://leetcode.com/problems/max-consecutive-ones-iii
    Purpose: Find the maximum number of consecutive 1's in the array if you can flip at most k 0's
    parameter: List[int] - nums: a list of binary number.
    return: int maxCount - Return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
    Pre-Condition: 1 <= nums.length <= 105
                 : nums[i] is either 0 or 1.
                 : 0 <= k <= nums.length
    Post-Condition: none
'''

# sliding window: runtime O(n), memory O(1)
def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    right = 0
    maxCount = 0

    while right < len(nums):
        if nums[right] == 0:
            while k < 1:
                # slide the left until k is available then move on
                if nums[left] == 0:
                    k += 1
                left += 1
            k -= 1
        right += 1

        maxCount = max(maxCount, right - left)
    return maxCount


if __name__ == '__main__':
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 3)) # 10
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 0)) # 4
    print(longestOnes([0,1,0,0], 0)) # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
