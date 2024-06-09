from typing import List

'''
    Link: https://leetcode.com/problems/find-the-duplicate-number
    Purpose: Given an array of integers containing n + 1 integers where each integer is in the range [1, n] inclusive.
           : There is only one repeated number in the array, determine this repeated number.
    parameter: int nums - an integers array containing n + 1 integers where each integer is in the range [1, n] inclusive with only one repeated number
    return: int - the repeated number
    Pre-Condition: 1 <= n <= 10^5
                 : nums.length == n + 1
                 : 1 <= nums[i] <= n
                 : All the integers in nums appear only once except for precisely one integer which appears two or more times.
    Post-Condition: none
'''
# math - run time: O(n), memory: O(n)
def findDuplicate_m1(nums: List[int]) -> int:
    # Find the sum value difference between set and list
    # Find the size difference between set and list
    # Find the missing x numbers of a Y integer in set by totalDiff/totalSizeDiff
    # sum(nums) = sum(set) + x*Y
    # x = len(nums) - len(set)
    # (sum(nums) - sum(set)) / (len(nums) - len(set)) = Y
    totalDiff = sum(nums) - sum(set(nums))
    totalSizeDiff = len(nums) - len(set(nums))
    return totalDiff // totalSizeDiff

'''
    Link: https://leetcode.com/problems/find-the-duplicate-number
    Purpose: Given an array of integers containing n + 1 integers where each integer is in the range [1, n] inclusive.
           : There is only one repeated number in the array, determine this repeated number.
    parameter: int nums - an integers array containing n + 1 integers where each integer is in the range [1, n] inclusive with only one repeated number
    return: int - the repeated number
    Pre-Condition: 1 <= n <= 10^5
                 : nums.length == n + 1
                 : 1 <= nums[i] <= n
                 : All the integers in nums appear only once except for precisely one integer which appears two or more times.
    Post-Condition: none
'''
# array - run time: O(n), memory: O(1)
def findDuplicate_m2(nums: List[int]) -> int:
    # [-1,-3,-4,2,2]
    i = 0
    while i < len(nums):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            return abs(nums[i])

        i += 1
    return 0

if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(findDuplicate_m1([1,3,4,2,2])) # 2
    print(findDuplicate_m1([3,1,3,4,2])) # 3
    print(findDuplicate_m1([4, 3, 1, 5, 4, 2, 4, 4]))  # 4
    print(findDuplicate_m1([3,3,3,3,3])) # 3

    print("\n === solution 2 === \n")
    print(findDuplicate_m2([1, 3, 4, 2, 2]))  # 2
    print(findDuplicate_m2([3, 1, 3, 4, 2]))  # 3
    print(findDuplicate_m2([4, 3, 1, 5, 4, 2, 4, 4]))  # 4
    print(findDuplicate_m2([3, 3, 3, 3, 3]))  # 3
