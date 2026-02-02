from typing import List

'''
    Link: https://leetcode.com/problems/spiral-matrix/
    Purpose: Given an m x n matrix, Find all elements of the matrix in spiral order.
    parameter: List[List[int]] matrix - a matrix of integer
    return: List[int] ans - the matrix in spiral order
    Pre-Condition: m == matrix.length
                 : n == matrix[i].length
                 : 1 <= m, n <= 10
                 : -100 <= matrix[i][j] <= 100
    Post-Condition: none
'''
# Array - runtime: O(n*m), memory: O(1)
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # [0][0], [0][1], [0][2], -> increase col
    # [1][2], [2][2] -> increase row
    # [2][1], [2][0] -> decrease col
    # [1][0] -> decrease row
    # [1][1] -> increase col
    # ...

    ans = []
    top_boundary = 0
    bottom_boundary = len(matrix) - 1
    left_boundary = 0
    right_boundary = len(matrix[0]) - 1
    m = len(matrix)
    n = len(matrix[0])

    while len(ans) < n * m:
        # left → right
        j = left_boundary
        while j <= right_boundary:
            ans.append(matrix[top_boundary][j])
            j += 1
        top_boundary += 1

        # top → bottom
        i = top_boundary
        while i <= bottom_boundary:
            ans.append(matrix[i][right_boundary])
            i += 1
        right_boundary -= 1

        if len(ans) == n * m:
            return ans

        # right → left
        j = right_boundary
        while j >= left_boundary:
            ans.append(matrix[bottom_boundary][j])
            j -= 1
        bottom_boundary -= 1

        # bottom → top
        i = bottom_boundary
        while i >= top_boundary:
            ans.append(matrix[i][left_boundary])
            i -= 1
        left_boundary += 1

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(spiralOrder([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(spiralOrder([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print(spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ])) # [1, 2, 3, 4, 8, 12, 16, 20, 24, 23, 22, 21, 17, 13, 9, 5, 6, 7, 11, 15, 19, 18, 14, 10]
    print(spiralOrder([[1]])) # [1]
    print(spiralOrder([
        [7],
        [9],
        [6]
    ])) # [7, 9, 6]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
