from typing import List

'''
    Link: https://leetcode.com/problems/valid-sudoku
    Purpose: Determine if 9 x 9 sudoku board is valid. Conditions:
           : 1. Each row must contain the digits 1-9 without repetition.
           : 2. Each column must contain the digits 1-9 without repetition.
           : 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    parameter: List[List[str]] board - a sudoku board
    return: bool - True if valid; otherwise, false
    Pre-Condition: board.length == 9
                 : board[i].length == 9
                 : board[i][j] is a digit 1-9 or '.'.
    Post-Condition: none
'''
# hash to gridIndex - runtime: O(4n^2), space: O(n^2)
def isValidSudoku_M1(board: List[List[str]]) -> bool:
    indexToRow = {i: [] for i in range(9)}
    indexToColumn = {i: [] for i in range(9)}
    indexToGrid = {i: [] for i in range(9)}

    # { (i, j), gridIndex }
    keyToGridIndex = {
        (0, 0): 0, (0, 1): 1, (0, 2): 2,
        (1, 0): 3, (1, 1): 4, (1, 2): 5,
        (2, 0): 6, (2, 1): 7, (2, 2): 8
    }
    for i in range(9):
        for j in range(9):
            entry = board[i][j]
            if entry != ".":
                indexToRow[i].append(entry)
                indexToColumn[j].append(entry)
                indexToGrid[keyToGridIndex[(i // 3, j // 3)]].append(entry)

    for key, value in indexToRow.items():
        if len(value) != len(set(value)):
            return False

    for key, value in indexToColumn.items():
        if len(value) != len(set(value)):
            return False

    for key, value in indexToGrid.items():
        if len(value) != len(set(value)):
            return False

    return True

'''
    Link: https://leetcode.com/problems/valid-sudoku
    Purpose: Determine if 9 x 9 sudoku board is valid. Conditions:
           : 1. Each row must contain the digits 1-9 without repetition.
           : 2. Each column must contain the digits 1-9 without repetition.
           : 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    parameter: List[List[str]] board - a sudoku board
    return: bool - True if valid; otherwise, false
    Pre-Condition: board.length == 9
                 : board[i].length == 9
                 : board[i][j] is a digit 1-9 or '.'.
    Post-Condition: none
'''
# hash - runtime: O(3n^2), space: O(1)
def isValidSudoku_M2(board: List[List[str]]) -> bool:
    GridTopLeftEntries = {
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6)
    }

    # check rows
    for i in range(9):
        seen = set()
        for j in range(9):
            entry = board[i][j]
            if entry in seen:
                return False
            if entry != ".":
                seen.add(entry)

    # check columns
    for i in range(9):
        seen = set()
        for j in range(9):
            entry = board[j][i]
            if entry in seen:
                return False
            if entry != ".":
                seen.add(entry)

    # check grids
    for start_i, start_j in GridTopLeftEntries:
        seen = set()
        for i in range(3):
            for j in range(3):
                entry = board[i + start_i][j + start_j]
                if entry in seen:
                    return False
                if entry != ".":
                    seen.add(entry)

    return True

if __name__ == '__main__':
    board1 = [
     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board3 = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    board4 = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "1", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "1", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "1", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    print("\n === Solution 1 === \n")
    print(isValidSudoku_M1(board1)) # True
    print(isValidSudoku_M1(board2)) # False
    print(isValidSudoku_M1(board3)) # True
    print(isValidSudoku_M1(board4)) # False

    print("\n === Solution 2 === \n")
    print(isValidSudoku_M2(board1)) # True
    print(isValidSudoku_M2(board2)) # False
    print(isValidSudoku_M2(board3)) # True
    print(isValidSudoku_M2(board4)) # False

