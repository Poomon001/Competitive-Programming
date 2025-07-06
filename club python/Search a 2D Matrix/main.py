from typing import List

'''
    Link: https://leetcode.com/problems/search-a-2d-matrix
    Purpose: find if a target in 2-d array given the 2-d array of integer sorted from left to right and up to bottom
    parameter: List[List[int] matrix - the sorted 2-d array
             : int target - an integer 
    return: bool - if the targer is in the 2-d array. Otherwise False.
    Pre-Condition: m == matrix.length
                 : n == matrix[i].length
                 : 1 <= m, n <= 100
                 : -10^4 <= matrix[i][j], target <= 10^4
    Post-Condition: none
'''
# 1-level binary search - runtime: O(m + log(n)), memory: O(m)
def searchMatrix_M1(matrix: List[List[int]], target: int) -> bool:
    # check if it is in the correct row
    # then binary search
    targetRow = matrix[0]  # a default for one row

    # determine a trget row
    rowLength = len(matrix[0])
    colLength = len(matrix)
    for i in range(colLength):
        if matrix[i][0] <= target <= matrix[i][rowLength - 1]:
            targetRow = matrix[i]

    # binary search
    left = 0
    right = rowLength - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if targetRow[mid] == target:
            return True

        if target > targetRow[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False

'''
    Link: https://leetcode.com/problems/search-a-2d-matrix
    Purpose: find if a target in 2-d array given the 2-d array of integer sorted from left to right and up to bottom
    parameter: List[List[int] matrix - the sorted 2-d array
             : int target - an integer 
    return: bool - if the targer is in the 2-d array. Otherwise False.
    Pre-Condition: m == matrix.length
                 : n == matrix[i].length
                 : 1 <= m, n <= 100
                 : -10^4 <= matrix[i][j], target <= 10^4
    Post-Condition: none
'''
# 2-level binary search - runtime: O(log(m) + log(n)), memory: O(1)
def searchMatrix_M2(matrix: List[List[int]], target: int) -> bool:
    rowLength = len(matrix[0])
    colLength = len(matrix)
    i = 0  # a default target row

    # binary search to determine the correct row
    left = 0
    right = colLength - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if matrix[mid][0] <= target <= matrix[mid][rowLength - 1]:
            i = mid

        if target > matrix[mid][0]:
            left = mid + 1
        else:
            right = mid - 1

    # binary search to determine the answer from a correct row
    targetRow = matrix[i]
    left = 0
    right = rowLength - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if targetRow[mid] == target:
            return True

        if target > targetRow[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(searchMatrix_M1([
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ], 3)) # True
    print(searchMatrix_M1([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 30)) # True
    print(searchMatrix_M1([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 31)) # False
    print(searchMatrix_M1([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 0)) # False
    print(searchMatrix_M1([[1]], 1)) # True
    print(searchMatrix_M1([[1]], 0)) # False

    print("\n === Solution 2 === \n")
    print(searchMatrix_M2([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 3))  # True
    print(searchMatrix_M2([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 30))  # True
    print(searchMatrix_M2([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 31))  # False
    print(searchMatrix_M2([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ], 0))  # False
    print(searchMatrix_M2([[1]], 1))  # True
    print(searchMatrix_M2([[1]], 0))  # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
