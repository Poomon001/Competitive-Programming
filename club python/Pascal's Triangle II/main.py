from typing import List

'''     
    Link: https://leetcode.com/problems/pascals-triangle-ii/
    Purpose: Find the rowIndexth (0-indexed) row of the Pascal's triangle.
    Parameter: int rowIndex - a number of the indexed row that we want to find
    Returns: array ans - the Pascal;s triangle row at the rowIndex
    Pre-Condition: 1 <= numRows <= 33
    Post-Condition: none
'''

# run-time: O(n^2), memory: O(n)
def getRow(rowIndex: int) -> List[int]:
    prevRow = [1]
    for _ in range(rowIndex):
        row = []
        prev = 0
        for i in range(len(prevRow)):
            value = prevRow[i] + prev
            prev = prevRow[i]
            row.append(value)
        row.append(1)
        prevRow = row[:]

    return prevRow

if __name__ == '__main__':
    print(getRow(0)) # [1]
    print(getRow(1)) # [1, 1]
    print(getRow(2)) # [1, 2, 1]
    print(getRow(3)) # [1, 3, 3, 1]
    print(getRow(4)) # [1, 4, 6, 4, 1]
    print(getRow(5)) # [1, 5, 10, 10, 5, 1]
