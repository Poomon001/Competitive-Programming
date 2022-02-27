from typing import List

'''
    Link: https://leetcode.com/problems/first-missing-positive/
    Purpose: Given an unsorted integer array nums, return the smallest missing positive integer.
    parameter: List[int] nums - a list of integer
    return: int - a smallest positive missing integer
    Pre-Condition: 1 <= nums.length <= 5 * 10^5
                 : -2^31 <= nums[i] <= 2^31 - 1
    Post-Condition: none
'''
# runtime: O(n), memory: O(1) (input doesnt count)
def firstMissingPositive(nums: List[int]) -> int:
    smallest = 1
    nums = set(nums)
    # find the smallest
    for i in range(1, len(nums) + 2):
        if i not in nums:
            smallest = i
            break

    smallest = 1 if smallest < 0 else smallest

    return smallest

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(firstMissingPositive([-1,-2,-3])) # 1
    print(firstMissingPositive([1, 1, 2, 4, 3, 6])) # 5
    print(firstMissingPositive([1,2,0])) # 3
    print(firstMissingPositive([3,4,-1,1])) # 2
    print(firstMissingPositive([7,8,9,11,12])) # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
