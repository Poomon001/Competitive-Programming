from typing import List

'''
    Link: https://leetcode.com/problems/subsets/
    Purpose: Find all subsets.
    parameter: List[int] nums - a list of numbers
    return: List[List[int]] - all subsets in nums
    Pre-Condition: 1 <= nums.length <= 10
                 : -10 <= nums[i] <= 10
                 : All the numbers of nums are unique.
    Post-Condition: none
'''
# backtracking solution - runtime: O(n*2^n), memory: O(n*2^n) -> we have 2^n subsets each many contain n elements
# eg.      [1, 2]
#       /          \
#     [1]          []
#   /    \       /    \
# [1, 2]  [1]  [2]    []
def subsets(nums: List[int]) -> List[List[int]]:
    subsets = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            subsets.append(subset[:])
            return

        # include the num[i] recursively
        subset.append(nums[i])
        dfs(i + 1)

        # exclude the num[i] recursively
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return subsets

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(subsets([1, 2, 3]))  # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    print(subsets([])) # [[]]
    print(subsets([1])) # [[1], []]
    print(subsets([1, 2])) # [[1, 2], [1], [2], []]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
