from typing import List

'''
    Link: https://leetcode.com/problems/house-robber
    Purpose: Given an integer array nums representing the amount of money of each house, 
           : find the maximum amount of money you can rob without robbing adjacent houses
    parameter: int[] nums - an array of integers representing the amount of money of each house
    return: int currMaxMoney - the maximum amount of money you can rob without robbing adjacent houses
    Pre-Condition: 1 <= nums.length <= 100
                 : 0 <= nums[i] <= 400
    Post-Condition: none
'''
# DP - runtime: O(n), memory: O(1)
if __name__ == '__main__':
    def rob(nums: List[int]) -> int:
        currMaxMoney = 0
        prevMaxMoney = 0

        # pick either:
        # 1. the curr highest, OR
        # 2. the curr value(may or may not contain the prev adjacent value) + the prev highest(guarantee not contain the prev adjacent value)
        for num in nums:
            temp = currMaxMoney
            currMaxMoney = max(currMaxMoney, num + prevMaxMoney)
            prevMaxMoney = temp

        return currMaxMoney

if __name__ == "__main__":
    print(rob([1,400,100,10,100])) # 500
    print(rob([2])) # 2
    print(rob([2, 7])) # 7
    print(rob([2, 7, 9])) # 11
    print(rob([1,2,3,1])) # 4
    print(rob([2,7,9,3,1])) # 12
    print(rob([40, 10, 100, 100])) # 140
    print(rob([1, 5, 1, 400, 100, 200])) # 605
