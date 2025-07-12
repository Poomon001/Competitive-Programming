from typing import List

'''
    Link: https://leetcode.com/problems/intersection-of-multiple-arrays
    Purpose: Find the list of integers that are present in all lists, sorted in ascending order.
    parameter: List[List[int]] - an array of integer lists
    return: List[int] - the list of integers that are present in all lists, sorted in ascending order.
    Pre-Condition: 1 <= nums.length <= 1000
                 : 1 <= sum(nums[i].length) <= 1000
                 : 1 <= nums[i][j] <= 1000
                 : All the values of nums[i] are unique.
    Post-Condition: none
'''
# bst property: runtime: O(n), memory: O(log(n))
def intersection(nums: List[List[int]]) -> List[int]:
    numToFreq = {}
    for li in nums:
        for num in li:
            numToFreq[num] = numToFreq.get(num, 0) + 1

    return sorted([key for key, value in numToFreq.items() if value == len(nums)])

if __name__ == '__main__':
    print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # [3,4]
    print(intersection([[1, 2, 4], [1, 2, 4], [1, 2, 4]]))  # [1,2,4]
    print(intersection([[1], [1, 2, 3, 4], [2]]))  # []
    print(intersection([[1,2,3],[4,5,6]])) # []
    print(intersection([[1, 2, 3]]))  # [1,2,3]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
