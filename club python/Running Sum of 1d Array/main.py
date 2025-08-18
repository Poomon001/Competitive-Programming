from typing import List

'''
    Link: https://leetcode.com/problems/running-sum-of-1d-array/
    Purpose: Find a running sum of an array
    parameter: List[int] nums - an integer list
    return: List[int] answer: a list of running sum
    Pre-Condition: 1 <= nums.length <= 1000
                 : -10^6 <= nums[i] <= 10^6
    Post-Condition: none
'''
# array prefix - runtime: O(n), space: O(1)
def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(runningSum([1,2,3,4])) # [1, 3, 6, 10]
    print(runningSum([1,1,1,1,1])) # [1, 2, 3, 4, 5]
    print(runningSum([3,1,2,10,1])) # [3, 4, 6, 16, 17]
    print(runningSum([0,0,-2,-5,-1,10])) # [0, 0, -2, -7, -8, 2]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
