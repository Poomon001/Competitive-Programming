from typing import List
'''
    Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
    Purpose: Find the minimum number that can sum the each element in an array (eleement-by-element) 
           : that never produces a result of less than 1
    parameter: List[int] nums - a list of integer
    return: int - the minimum number
    Pre-Condition: 1 <= nums.length <= 100
                 : -100 <= nums[i] <= 100
    Post-Condition: none
'''
# find the minimum number that can go though the array and produce a result that never less than 1
def minStartValue(nums: List[int]) -> int:
    minimum = nums[0]
    curr = 0

    # find the minimum result from all sum steps
    for num in nums:
        curr = num + curr
        minimum = min(minimum, curr)

    # if minimum is negative or 0 then it away from 1 by (minimum*-1)+1
    # if minimum is positive then we know we can start at 1
    return (minimum*-1)+1 if minimum < 0 else 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minStartValue([-3,2,-3,4,2])) # 5
    print(minStartValue([1,2])) # 1
    print(minStartValue([1,-2,-3])) # 5
    print(minStartValue([-3, -2, -3, -4, -2])) #15
    print(minStartValue([3, 2, 3, 4, 2])) #1
    print(minStartValue([3, 2, 3, 4, 2, 0])) #1
    print(minStartValue([2,3,5,-5,-1])) #1


