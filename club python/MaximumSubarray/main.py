from typing import NewType
from typing import List


li1 = [-10, -2, 1, 10, -1, 3] # 13
li2 = [0] # 0
li3 = [-2,1,-3,4,-1,2,1,-5,4] # 6
li4 = [5,4,-1,7,8] #23

'''
    Link: https://leetcode.com/problems/maximum-subarray/
    Purpose: find the contiguous subarray which has the largest sum.
    Parameter: list - a list of numbers
    return: int - the the largest sum in the contiguous subarray
    Pre-Condition : array is not empty
    Post-Condition: O(n^2)
'''
# runtime: O(n^2), memory: O(1)
def maxSubArrayBruteForce(nums: List[int]) -> int:
    # assume array is not empty
    maxSum = nums[0]
    for i in range(0, len(nums)):
        sum = 0
        # find highest sum in contiguous subarray
        for j in range(i, len(nums)):
            sum = sum + nums[j]
            if sum > maxSum:
                maxSum = sum

    return maxSum


'''
    Link: https://leetcode.com/problems/maximum-subarray/
    Purpose: find the contiguous subarray which has the largest sum.
    Parameter: list - a list of numbers
    return: int - the the largest sum in the contiguous subarray
    Pre-Condition : array is not empty
    Post-Condition: O(n)
'''
# KadaneAlgo (take the current highest value: max(currNum, prevSum + currNum))
# runtime: O(n), memory: O(1)
def maxSubArrayKadaneAlgo(nums: List[int]) -> int:
    maxSum = nums[0]
    maxCurr = nums[0]

    ''' 
        From KadaneAlgo the max sum in contiguous subarray is either 
        "nums[i]" or "nums[i] + previous max sum of all prior elements to nums[i]" 
    '''
    for i in range(1, len(nums)):
        # find curr max sum
        maxCurr = max(nums[i], maxCurr+nums[i])

        # find global max sum
        maxSum = max(maxCurr, maxSum)
    return maxSum


print("\n+==== Bruteforce ====+\n")
print(maxSubArrayBruteForce(li1)) # 13
print(maxSubArrayBruteForce(li2)) # 0
print(maxSubArrayBruteForce(li3)) # 6
print(maxSubArrayBruteForce(li4)) # 23

print("\n+==== KadanAlgo ====+\n")
print(maxSubArrayKadaneAlgo(li1)) # 13
print(maxSubArrayKadaneAlgo(li2)) # 0
print(maxSubArrayKadaneAlgo(li3)) # 6
print(maxSubArrayKadaneAlgo(li4)) # 23