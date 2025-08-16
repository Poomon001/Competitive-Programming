from typing import List

'''
    Link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/
    Purpose: Find the maximum possible number of the same element after performing at most k operations.
           : k operation to add 1 for k times to the elements
    parameter: List[str] numss - a list of numbers
             : int k - a number of operation
    return: int max_freq - the maximum possible number of the same element after performing at most k operations.
    Pre-Condition: 1 <= nums.length <= 10^5
                 : 1 <= nums[i] <= 10^5
                 : 1 <= k <= 10^5
    Post-Condition: none
'''
# sliding window - runtime: O(nlogn), space: O(1)
def maxFrequency(nums: List[int], k: int) -> int:
    # nums[right] * len(nums[left:right]) = total ideal sum of all same freq from left to right
    # sum([left:right]) + k = what we actually have
    # So, nums[right] * len([left:right]) == sum([left:right]) + k
    # [1, 1, 1, 2, 4], k = 5
    #  l        r
    # we have (1 + 1 + 1 + 2) + (k=2) = 7
    # we need [2, 2, 2, 2] = 2 * 4 = 8

    nums.sort()
    max_freq = 0
    left = 0
    total = 0

    for right in range(len(nums)):
        total += nums[right]
        # what we have < actual needed
        while total + k < (right - left + 1) * nums[right]:
            # cannot grow further, need to shrink
            total -= nums[left]
            left += 1
        max_freq = max(max_freq, right - left + 1)
    return max_freq


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maxFrequency([1,4,8,13], 5)) # 2
    print(maxFrequency([1,2,4], 5)) # 3
    print(maxFrequency([3,9,6], 2)) # 1
