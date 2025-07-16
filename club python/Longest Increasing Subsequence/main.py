from typing import List

'''     
    Link: https://leetcode.com/problems/longest-increasing-subsequence/
    Purpose: Given an integer array nums, find the length of the longest strictly increasing subsequence.
    Parameter: List[str] nums - a list of integers
    Returns: int - the length of the longest strictly increasing subsequence.
    Pre-Condition: 1 <= nums.length <= 2500
                 : -10^4 <= nums[i] <= 10^4
    Post-Condition: none
'''
def lengthOfLIS(nums: List[int]) -> int:
    # think about the combination answers of the curr number
    # optimal dp[i] = max(any previous number's total that is less than dp[i]) + 1
    dp = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        curr = nums[i]
        maxi = 0
        for j in range(i):
            if curr > nums[j]:
                maxi = max(maxi, dp[j] + 1)
                dp[i] = maxi

    return max(dp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
    print(lengthOfLIS([10,-9,2,5,3,7,0,18]))  # 5
    print(lengthOfLIS([0,1,0,3,2,3]))  # 4
    print(lengthOfLIS([7,7,7,7,7]))  # 1
    print(lengthOfLIS([2,5,3,7,6,1,9]))  # 4
    print(lengthOfLIS([2]))  # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
