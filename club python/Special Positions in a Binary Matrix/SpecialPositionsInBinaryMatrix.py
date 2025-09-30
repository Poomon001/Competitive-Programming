from collections import defaultdict
from typing import List

'''
    Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/
    Purpose: Find all 1's where other elements in its row and column are 0's in a matrix
    parameter: List[List[int]] mat - n x m matrix
    return: int answer - the number of 1's where other elements in its row and column are 0's
    Pre-Condition: m == mat.length
                 : n == mat[i].length
                 : 1 <= m, n <= 100
                 : mat[i][j] is either 0 or 1.
    Post-Condition: none
'''
# hashtable - runtime: O(n^2), memory: O(n)
def numSpecial(mat: List[List[int]]) -> int:
    # (x, y), (0, 0), (2, 1), (0, 2)
    # (x, y), (0, 0), (1, 1), (2, 2)

    # only count the entry if it has no repeat x and y
    x_to_count = defaultdict(int)  # {x, count}
    y_to_count = defaultdict(int)  # {y, count}
    answer = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            entry = mat[i][j]
            if entry == 1:
                x_to_count[j] += 1
                y_to_count[i] += 1

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            entry = mat[i][j]
            if entry == 1:
                if x_to_count[j] == 1 and y_to_count[i] == 1:
                    answer += 1
    return answer
if __name__ == '__main__':
    print(numSpecial(
        [
            [1,0,0],
            [0,0,1],
            [1,0,0]
        ]
    )) # 1

    print(numSpecial(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    )) # 3

    print(numSpecial(
        [
            [1, 0, 0],
        ]
    )) # 1

    print(numSpecial(
        [
            [1],
        ]
    )) # 1