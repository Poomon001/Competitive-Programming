from typing import List
from collections import Counter
'''
    Link: https://leetcode.com/problems/longest-harmonious-subsequence/
    Purpose: Given an integer array nums, Find the longest sequences of two numbers
           : where the different between two numbers is exact 1.
    parameter: List[int] nums - a list of numbers
    return: int maxSeq -  the longest sequences of two numbers where the different between two numbers is exact 1.
    Pre-Condition: 1 <= nums.length <= 2 * 104
                 : -10^9 <= nums[i] <= 10^9
    Post-Condition: none
'''
# Hashtable - runtime: O(n), space: O(n)
def findLHS_M1(nums: List[int]) -> int:
    numToCount = Counter(nums)
    maxSeq = 0

    for num, count in numToCount.items():
        if num + 1 in numToCount:
            candidate = numToCount[num] + numToCount[num + 1]
            maxSeq = max(maxSeq, candidate)

    return maxSeq

'''
    Link: https://leetcode.com/problems/longest-harmonious-subsequence/
    Purpose: Given an integer array nums, Find the longest sequences of two numbers
           : where the different between two numbers is exact 1.
    parameter: List[int] nums - a list of numbers
    return: int maxSeq -  the longest sequences of two numbers where the different between two numbers is exact 1.
    Pre-Condition: 1 <= nums.length <= 2 * 104
                 : -10^9 <= nums[i] <= 10^9
    Post-Condition: none
'''
# Sort and Hashtable - runtime: O(nlogn), space: O(n)
def findLHS_M2(nums: List[int]) -> int:
    numToCount = Counter(nums)
    li = []

    for num, count in numToCount.items():
        li.append((num, count))

    li.sort()

    left = 0
    right = 1
    count = 0
    maxCount = 0
    while right < len(li):
        if li[left][0] + 1 == li[right][0]:
            count = li[left][1] + li[right][1]
        left += 1
        right += 1
        maxCount = max(maxCount, count)

    return maxCount

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(findLHS_M1([1,3,2,2,5,2,3,7])) # [3,2,2,2,3] = 5
    print(findLHS_M1([1,2,3,4]))  # [1,2], [2,3], or [3,4] = 2
    print(findLHS_M1([1,1,1,1]))  # [] = 0
    print(findLHS_M1([3,2]))  # [3,2] = 2
    print(findLHS_M1([1]))  # [] = 0

    print("\n === Solution 2 === \n")
    print(findLHS_M2([1, 3, 2, 2, 5, 2, 3, 7]))  # [3,2,2,2,3] = 5
    print(findLHS_M2([1, 2, 3, 4]))  # [1,2], [2,3], or [3,4] = 2
    print(findLHS_M2([1, 1, 1, 1]))  # [] = 0
    print(findLHS_M2([3, 2]))  # [3,2] = 2
    print(findLHS_M2([1]))  # [] = 0