from typing import List

'''
    Link: https://leetcode.com/problems/minimum-falling-path-sum
    Purpose: the minimum sum of any falling path through matrix
           : A falling path is the next row that is either directly below or diagonally left/right
    parameter: int - the minimum sum of any falling path
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: n == matrix.length == matrix[i].length
                 : 1 <= n <= 100
                 : -100 <= matrix[i][j] <= 100
    Post-Condition: none
'''
# DP approach: runtime: O(n^2), memory: O(n^2)
def minFallingPathSum_M1(matrix: List[List[int]]) -> int:
    minimizationTable = [[0 for _ in matrix] for _ in matrix]  # create a cache table

    # add the first row of matrix to minimizationTable
    for j in range(len(matrix[0])):
        minimizationTable[0][j] = matrix[0][j]

    # build minimizationtable:
    # formula -> minimizationTable[n][m] =
    #               matrix[n][m] + min(minimizationTable[n-1][m-1], minimizationTable[n-1][m], minimizationTable[n-1][m+1])
    for i in range(1, len(matrix[0])):
        for j in range(0, len(matrix[i])):
            if j - 1 < 0:
                minimizationTable[i][j] = matrix[i][j] + min(minimizationTable[i - 1][j],
                                                             minimizationTable[i - 1][j + 1])
            elif j + 1 > len(matrix[0]) - 1:
                minimizationTable[i][j] = matrix[i][j] + min(minimizationTable[i - 1][j - 1],
                                                             minimizationTable[i - 1][j])
            else:
                minimizationTable[i][j] = matrix[i][j] + min(minimizationTable[i - 1][j - 1],
                                                             minimizationTable[i - 1][j],
                                                             minimizationTable[i - 1][j + 1])

    return min(minimizationTable[len(matrix) - 1])

'''
    Link: https://leetcode.com/problems/minimum-falling-path-sum
    Purpose: the minimum sum of any falling path through matrix
           : A falling path is the next row that is either directly below or diagonally left/right
    parameter: int - the minimum sum of any falling path
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: n == matrix.length == matrix[i].length
                 : 1 <= n <= 100
                 : -100 <= matrix[i][j] <= 100
    Post-Condition: none
'''
# in-place DP approach: runtime: O(n^2), memory: O(1)
def minFallingPathSum_M2(matrix: List[List[int]]) -> int:
    # build minimizationtable by keeping the current value + the optimal value
    # minimizationTable[n][m] = matrix[n][m] + min(minimizationTable[n-1][m-1], minimizationTable[n-1][m], minimizationTable[n-1][m+1])
    for i in range(1, len(matrix[0])):
        for j in range(0, len(matrix[i])):
            if j - 1 < 0:
                matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j], matrix[i - 1][j + 1])
            elif j + 1 > len(matrix[0]) - 1:
                matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j - 1], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i][j] + min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])

    return min(matrix[len(matrix) - 1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === solution 1 ===\n")
    print(minFallingPathSum_M1([[2, 0, 3, -10], [6, 5, 4, -20], [7, 0, 9, 0], [-100, 8, 9, 100]])) # -106
    print(minFallingPathSum_M1([[2, 1, 3],[6, 5, 4],[7, 8, 9]])) # 13
    print(minFallingPathSum_M1([[2, 1], [6, 5]])) # 6
    print(minFallingPathSum_M1([[-19, 57],[-40, -5]])) # -59
    print(minFallingPathSum_M1([[-5]])) # -5

    print("\n === solution 2 ===\n")
    print(minFallingPathSum_M2([[2, 0, 3, -10], [6, 5, 4, -20], [7, 0, 9, 0], [-100, 8, 9, 100]]))  # -106
    print(minFallingPathSum_M2([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # 13
    print(minFallingPathSum_M2([[2, 1], [6, 5]]))  # 6
    print(minFallingPathSum_M2([[-19, 57], [-40, -5]]))  # -59
    print(minFallingPathSum_M2([[-5]]))  # -5
