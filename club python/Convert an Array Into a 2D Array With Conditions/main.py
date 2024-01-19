from collections import Counter
from typing import List

'''
    Link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
    Purpose: Create a 2D array from an integer array satisfying the following conditions:
           : 1. The 2D array should contain only the elements of the array nums.
           : 2. Each row in the 2D array contains distinct integers.
           : 3. The number of rows in the 2D array should be minimal.
    parameter: int[] nums - an array of integers
    return: int[][] ans - a 2D array satisfying the conditions
    Pre-Condition: 1 <= nums.length <= 200
                 : 1 <= nums[i] <= nums.length
    Post-Condition: none
'''
# hashtable: runtime: O(n), memory: O(n)
def findMatrix(nums: List[int]) -> List[List[int]]:
    numToFreq = Counter(nums)
    maxRow = max(numToFreq.values())
    ans = [[] for _ in range(maxRow)]

    for key, value in numToFreq.items():
        for i in range(0, value):
            ans[i].append(key)

    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findMatrix([1,3,4,1,2,3,1])) # [[1, 3, 4, 2], [1, 3], [1]]
    print(findMatrix([2,1,1])) # [[2, 1], [1]]
    print(findMatrix([100])) # [[100]]

