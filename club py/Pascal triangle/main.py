from typing import List

'''     
    Link: https://leetcode.com/problems/pascals-triangle/
    Purpose: Find all the first numRows of Pascal's triangle.
    Parameter: int numRows - The number of row in Pascal's triangle
    Returns: 2D array outer - All the first numRows of Pascal's triangle
    Pre-Condition: 1 <= numRows <= 30
    Post-Condition: none
'''
def pascalTriangle(numRows:int) -> List:
    # allocate outer array space where size = numRows: [[], [], [], ...]
    outer = [[]]*numRows

    for i in range(numRows):
        # allocate inner array space where size = augmented by 1 every iteration (a property of pascal triangle): [[0], [0, 0], [0, 0, 0], ...]
        outer[i] = [0]*(i+1)

        for j in range(i+1):
            # assign "1" at the beginning and the end of each inner array
            if j == 0 or j == i:
                outer[i][j] = 1
            # assign the value in the previous outer array [i-1] of the current element [j] + the previous element [j-1] (this refer to the previous outer array)
            else:
                outer[i][j] = outer[i-1][j-1] + outer[i-1][j]

    return outer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(pascalTriangle(1))
    print(pascalTriangle(4))
    print(pascalTriangle(5))
    print(pascalTriangle(6))
    print(pascalTriangle(20))
    print(pascalTriangle(21))