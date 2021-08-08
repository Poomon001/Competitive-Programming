from typing import List

'''
     Purpose: Indices of the two numbers such that they add up to target
     Parameter: array - a list of integer
               : int - the target number
    Returns: array - indices of two numbers such that they add up to target
    Pre-Condition: there is always one exactly solution in the input array
    Post-Condition: none
'''
def twoSum(nums: List[int], target: int) -> List[int]:
    li = [-1, -1]
    for i, num in enumerate(nums):
        li[0] = i
        for j in range(i + 1, len(nums)):
            if (num + nums[j] == target):
                li[1] = j
                return li
    raise Exception("no solution")

''' raise Exception("opp my error") is to indicate your error from a requirement '''
print(twoSum([2,7,11,15], 9))
print(twoSum([2,7,11,15], 17))
print(twoSum([2,7,11,15], 100))