from typing import NewType
from typing import List

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
        "nums[i]" or "nums[i] + previous max sum of contiguous subarray to nums[i-1]" 
    '''
    for i in range(1, len(nums)):
        # find curr max sum
        maxCurr = max(nums[i], maxCurr+nums[i])

        # find global max sum
        maxSum = max(maxCurr, maxSum)
    return maxSum

'''
    Link: https://leetcode.com/problems/maximum-subarray/
    Purpose: find the contiguous subarray which has the largest sum.
    Parameter: list - a list of numbers
    return: int - the the largest sum in the contiguous subarray
    Pre-Condition : array is not empty
    Post-Condition: O(n)
'''
# Greedy
# runtime: O(n), memory: O(1)
def maxSubArrayGreedyAlgo(nums: List[int]) -> int:
    # keep selecting any localSum with positive value
    # update maxSum each iteration
    maxSum = 0
    localSum = 0
    isAllNegative = True
    for num in nums:
        if num >= 0:
            isAllNegative = False  # need to pick one num if all nums are negatives

        if localSum + num >= 0:
            localSum += num
        else:
            localSum = 0
        maxSum = max(maxSum, localSum)
    return maxSum if not isAllNegative else max(nums)

if __name__ == "__main__":
    li1 = [-10, -2, 1, 10, -1, 3]  # 13
    li2 = [0]  # 0
    li3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6
    li4 = [5, 4, -1, 7, 8]  # 23
    li5 = [-15, -14, -11, -10, -98, 0]  # 0
    li6 = [-15, -14, -11, -10, -98]  # -10

    print("\n+==== Bruteforce ====+\n")
    print(maxSubArrayBruteForce(li1)) # 13
    print(maxSubArrayBruteForce(li2)) # 0
    print(maxSubArrayBruteForce(li3)) # 6
    print(maxSubArrayBruteForce(li4)) # 23
    print(maxSubArrayBruteForce(li5))  # 0
    print(maxSubArrayBruteForce(li6))  # -10

    print("\n+==== KadanAlgo ====+\n")
    print(maxSubArrayKadaneAlgo(li1)) # 13
    print(maxSubArrayKadaneAlgo(li2)) # 0
    print(maxSubArrayKadaneAlgo(li3)) # 6
    print(maxSubArrayKadaneAlgo(li4)) # 23
    print(maxSubArrayKadaneAlgo(li5))  # 0
    print(maxSubArrayKadaneAlgo(li6))  # -10

    print("\n+==== Greedy ====+\n")
    print(maxSubArrayGreedyAlgo(li1)) # 13
    print(maxSubArrayGreedyAlgo(li2)) # 0
    print(maxSubArrayGreedyAlgo(li3)) # 6
    print(maxSubArrayGreedyAlgo(li4)) # 23
    print(maxSubArrayGreedyAlgo(li5))  # 0
    print(maxSubArrayGreedyAlgo(li6))  # -10