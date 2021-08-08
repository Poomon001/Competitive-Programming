from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    li = [-1, -1]
    for i, num in enumerate(nums):
        li[0] = i
        for j in range(i + 1, len(nums)):
            if (num + nums[j] == target):
                li[1] = j
                return li
    raise Exception("no solution")


def error(num: int, num2: int) -> int:
    x = num/num2
    return x

''' try...except is to indicate run-time error '''
try:
    li = []
    li[1] = 0
except Exception as e:
    print (e)

try:
    error(1,0)
except Exception as e:
    print (e)

''' raise Exception("opp my error") is to indicate your error from a requirement '''
print(twoSum([2,7,11,15], 100))