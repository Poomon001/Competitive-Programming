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
    # row 0
    ans = [1]
    # store previous row
    temp = []

    # get thought each row index
    for i in range(rowIndex):
        prev = 0
        # create a new row from the previous row (temp)
        for j in range(len(temp)):
            ans[j] = temp[j] + prev
            prev = temp[j]

        # at the end of the list we append 1
        ans.append(1)

        # set curr row to prev row
        temp = ans[:]

    return ans

if __name__ == '__main__':
    print(getRow(0)) # [1]
    print(getRow(1)) # [1, 1]
    print(getRow(2)) # [1, 2, 1]
    print(getRow(3)) # [1, 3, 3, 1]
    print(getRow(4)) # [1, 4, 6, 4, 1]
    print(getRow(5)) # [1, 5, 10, 10, 5, 1]
