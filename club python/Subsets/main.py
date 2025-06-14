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
# recursive - runtime: O(n*2^n), memory: O(n*2^n) -> we have 2^n subsets each many contain n elements
# eg.      [    ]
#       /          \
#     []          [1]
#   /    \       /    \
# []    [2]    [1]    [1, 2]
def subsets_M1(nums: List[int]) -> List[List[int]]:
    subsets = []
    subset = []

    def backtrack(i):
        # keep tract of leaf nodes
        if i > len(nums) - 1:
            subsets.append(subset[:])
            return

        # include the num[i] recursively
        subset.append(nums[i])
        backtrack(i + 1)

        # exclude the num[i] recursively
        subset.pop()
        backtrack(i + 1)

    backtrack(0)
    return subsets

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
# iterative - runtime: O(n*2^n), memory: O(n*2^n) -> we have 2^n subsets each many contain n elements
# build next subsets on top of the current subsets - eg n = 3
# init:  []
# add 1: [], [1]
# add 2: [], [1], [2], [1, 2]
# add 3: [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
def subsets_M2(nums: List[int]) -> List[List[int]]:
    subsets = [[]]
    for num in nums:
        # build on top of the current subsets
        n = len(subsets)
        for j in range(n):
            subset = subsets[j][:]
            subset.append(num)
            subsets.append(subset)
    return subsets

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
# combine/traditional - runtime: O(n*2^n), memory: O(n*2^n) -> we have 2^n subsets each many contain n elements
#                         []
#               /          |          \
#             [1]         [2]         [3]
#           /     \      /   \         |
#       [1,2]   [1,3]  [2,3]  ×       ×
#        /         |     |
#    [1,2,3]       ×     ×
def subsets_M3(nums: List[int]) -> List[List[int]]:
    subsets = []

    def backtrack(i, subset):
        subsets.append(subset[:])
        for j in range(i, len(nums)):
            subset.append(nums[j])
            backtrack(j + 1, subset)
            subset.pop()

    backtrack(0, [])
    return subsets

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(subsets_M1([1, 2, 3]))  # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    print(subsets_M1([])) # [[]]
    print(subsets_M1([1])) # [[1], []]
    print(subsets_M1([1, 2])) # [[1, 2], [1], [2], []]

    print("\n === solution 2 === \n")
    print(subsets_M2([1, 2, 3]))  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets_M2([]))  # [[]]
    print(subsets_M2([1]))  # [[], [1]]
    print(subsets_M2([1, 2]))  # [[], [1], [2], [1, 2]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
