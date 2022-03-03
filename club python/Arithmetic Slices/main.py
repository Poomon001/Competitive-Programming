from typing import List

'''
    Link: https://leetcode.com/problems/arithmetic-slices/
    Purpose: Find the number of arithmetic subarrays of nums
           : An integer array is called arithmetic if it consists of at least three elements 
             and if the difference between any two consecutive elements is the same.
           : For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
    parameter: List[int] nums - a list of integer
    return: int total - the number of arithmetic subarrays of nums
    Pre-Condition: 1 <= nums.length <= 5000
                 : -1000 <= nums[i] <= 1000
    Post-Condition: none
'''
# dynamic programming solution - use the result from a smaller sub-problem to solve the larger problem
# runtime: O(n), memory: O(1)
def numberOfArithmeticSlices(nums: List[int]) -> int:
    # sequence of 3 = (0) + (1)
    # sequence of 4 = (0 + 1) + (2)
    # sequence of 5 = (0 + 1 + 2) + (3)
    # sequence of 6 = (0 + 1 + 2 + 3) + (4)
    # note that it is (previous answer) + (Nth term)

    # keep track of total answer
    total = 0

    # keep track of Nth term
    N = 1

    if len(nums) < 3:
        return 0

    # keep track of difference
    diff = nums[1] - nums[0]

    for i in range(len(nums)-1):
        # if the difference is same, add 1 Nth term
        if diff == nums[i + 1] - nums[i]:
            N += 1
        # otherwise, set a new difference, reset Nth term to 1, and add 1 Nth term for the current number pair
        else:
            diff = nums[i + 1] - nums[i]
            N = 1
            N += 1

        # when find 3 or more Arithmetic subarray, do: answer = (previous answer) + (Nth term)
        if N >= 3:
            total = total + (N - 2)

    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(numberOfArithmeticSlices([1])) # 0
    print(numberOfArithmeticSlices([1, 2])) # 0
    print(numberOfArithmeticSlices([1, 2, 3])) # 1
    print(numberOfArithmeticSlices([1, 2, 3, 4])) # 3
    print(numberOfArithmeticSlices([1, 2, 3, 4, 5])) # 6
    print(numberOfArithmeticSlices([1, 2, 3, 4, 5, 6])) # 10
    print(numberOfArithmeticSlices([1, 2, 3, 4, 5, 7, 20, 22, 24, 26, 28])) # 12
    print(numberOfArithmeticSlices([1, 2, 3, 4, 5, 7, 9, 11, 13, 15])) # 16
    print(numberOfArithmeticSlices([1, 1, 1, 1, 1])) # 6
    print(numberOfArithmeticSlices([1, 5, 6, 10, 11, 15, 20, 21])) # 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
