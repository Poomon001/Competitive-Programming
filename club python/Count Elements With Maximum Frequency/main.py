from typing import List
from collections import Counter

'''
    Link: https://leetcode.com/problems/count-elements-with-maximum-frequency
    Purpose: Given an positive integer array. Count the integers, having the same frequency and their frequency is the maximum 
    parameter: int[] nums - an positive integer array
    return: int - the total elements, having the same frequency and their frequency is the maximum
    Pre-Condition: 1 <= nums.length <= 100
                 : 1 <= nums[i] <= 100
    Post-Condition: none
'''
# DP - runtime: O(n), memory: O(n)
def maxFrequencyElements(nums: List[int]) -> int:
    numsToFreq = Counter(nums)
    maxFreq = max(numsToFreq.values())
    total = list(numsToFreq.values()).count(maxFreq)

    return total * maxFreq


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maxFrequencyElements([1,2,2,3,1,4])) # 4 (1, 1, 2, 2)
    print(maxFrequencyElements([1,2,3,4,5])) # 5 (1, 2, 3, 4, 5)
    print(maxFrequencyElements([1])) # 1 (1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
