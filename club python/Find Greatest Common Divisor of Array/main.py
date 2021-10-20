from typing import List

'''
    Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
    Purpose: return the greatest common divisor of the smallest number and largest number in nums
    parameter: List[int] nums - a list of integer
    return: int - the greatest common divisor
    Pre-Condition: 2 <= nums.length <= 1000
                 : 1 <= nums[i] <= 1000
    Post-Condition: none
'''
def findGCD(nums: List[int]) -> int:
    nums.sort()
    max = nums[len(nums) - 1]
    min = nums[0]

    # try all possible number range from max to min
    for i in range(max, 0, -1):
        # retrun the highest number that can divide both max and min
        if max % i == min % i == 0:
            return i

if __name__ == '__main__':
    print(findGCD([2,5,6,9,10])) # 2
    print(findGCD([7,5,6,8,3])) # 1
    print(findGCD([3,3])) # 3