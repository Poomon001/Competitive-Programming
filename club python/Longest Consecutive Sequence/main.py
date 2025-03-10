from typing import List

'''
    Link: https://leetcode.com/problems/longest-consecutive-sequence
    Purpose: Determine the length of the longest consecutive elements sequence.
    parameter: List[int] nums - a list of integers
    return: int -  the length of the longest consecutive elements sequence.
    Pre-Condition: 0 <= nums.length <= 10^5
                 : -10^9 <= nums[i] <= 10^9
    Post-Condition: none
'''
# sort - runtime: O(nlogn), memory: O(n)
def longestConsecutive_M1(nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort()
    goble_longest = 0
    local_longest = 0
    i = 0
    j = 1
    if len(nums) < 1:
        return len(nums)

    while j < len(nums):
        if nums[j] - nums[i] == 1:
            local_longest += 1  #
        else:
            goble_longest = max(local_longest, goble_longest)
            local_longest = 0
        i += 1
        j += 1

    return max(local_longest, goble_longest) + 1

'''
    Link: https://leetcode.com/problems/longest-consecutive-sequence
    Purpose: Determine the length of the longest consecutive elements sequence.
    parameter: List[int] nums - a list of integers
    return: int -  the length of the longest consecutive elements sequence.
    Pre-Condition: 0 <= nums.length <= 10^5
                 : -10^9 <= nums[i] <= 10^9
    Post-Condition: none
'''
# Pick root - runtime: O(n), memory: O(n)
def longestConsecutive_M2(nums: List[int]) -> int:
    longest = 0
    nums = set(nums)

    for num in nums:
        # if the current number is the start
        if num - 1 not in nums:
            length = 1

            # check if the next element is in the sequence
            while num + length in nums:
                length += 1

            longest = max(longest, length)

    return longest


if __name__ == '__main__':
    print("\n=== Solution 1 ===\n")
    print(longestConsecutive_M1([100, 4, 200, 1, 3, 2]))  # 4
    print(longestConsecutive_M1([1, 0, 1, 2]))  # 3
    print(longestConsecutive_M1([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(longestConsecutive_M1([]))  # 0

    print("\n=== Solution 2 ===\n")
    print(longestConsecutive_M2([100,4,200,1,3,2])) # 4
    print(longestConsecutive_M2([1,0,1,2])) # 3
    print(longestConsecutive_M2([0,3,7,2,5,8,4,6,0,1])) # 9
    print(longestConsecutive_M2([])) # 0
