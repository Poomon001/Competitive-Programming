from typing import List

'''
    Link: https://leetcode.com/problems/find-the-middle-index-in-array
    Purpose: Find the leftmost index where the sum of integers to its left equals to the sum of right integers to its right
    parameter: List[int] - a list of integer
    return: int middle - the leftmost index
    Pre-Condition: 1 <= nums.length <= 100
                 : -1000 <= nums[i] <= 1000
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def findMiddleIndex(nums: List[int]) -> int:
    left = 0
    right = sum(nums)
    middle = -1

    for i in range(len(nums)):
        right = right - nums[i]

        if left == right:
            return i

        left += nums[i]

    return middle

if __name__ == '__main__':
    print(findMiddleIndex([2,3,-1,8,4])) # 3
    print(findMiddleIndex([1,-1,4])) # 2
    print(findMiddleIndex([0, 1, 0, -1])) # 0
    print(findMiddleIndex([2,-5,9])) # -1
