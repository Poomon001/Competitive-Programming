from typing import List

'''     
    Link: https://leetcode.com/problems/rotate-image/
    Purpose: Find a rotation the matrix by 90 degrees (clockwise).
    Parameter: List[List[int]] matrix - a 2D array of integers (size n x n)
    Returns: : List[List[int]] matrix - a 2D array of integers rotated 90 degree clockwise (size n x n)
    Pre-Condition: matrix.length == n
                : matrix[i].length == n
                : 1 <= n <= 20
                : -1000 <= matrix[i][j] <= 1000
    Post-Condition: Must not allocate new array.
                  : Everything must be done in the given matrix
                  : returned answer must be the given matrix
'''
# solution from observing the answers: runtime: O(n^2), memory:O(1)
def rotate(matrix: List[List[int]]) -> List[List[int]]:
    # optional to make it easier to vitualize the question
    matrix.reverse()
    index = len(matrix)

    for i in range(index):
        # to keep track of the extended block
        k = index
        for j in range(index):
            # first iteration we want to extend new blocks to the list
            if i == 0:
                matrix.append([matrix[i][j]])
            # other iterations we just want to append element to the new blocks
            else:
                matrix[k].append(matrix[i][j])
            k += 1

    # remove the original blocks to get the answer
    for i in range(index):
        matrix.pop(0)

    return matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
    print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(rotate([[1]])) # [[1]]
    print(rotate([[1,2],[3,4]])) # [[3,1],[4,2]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
