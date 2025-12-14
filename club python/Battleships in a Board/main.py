from typing import List

'''
    Link: https://leetcode.com/problems/battleships-in-a-board/
    Purpose: Find the number of battleship, 'X', where each battleship can be:
           : 1. all horizontal battleships 
           : 2. all vertical battleships
    Parameter: List[List[str]] - a board with 'X' and '.'
    return: int count - a number of battleship
    Pre-Condition: m == board.length
                 : n == board[i].length
                 : 1 <= m, n <= 200
                 : board[i][j] is either '.' or 'X'.
    Post-Condition: None
'''
# array - runtime: O(n*m), memory: O(1)
def countBattleships_m1(board: List[List[str]]) -> int:
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X' and ((j + 1 == len(board[0]) or board[i][j + 1] == '.') and (
                    i + 1 == len(board) or board[i + 1][j] == '.')):
                count += 1

    return count

'''
    Link: https://leetcode.com/problems/battleships-in-a-board/
    Purpose: Find the number of battleship, 'X', where each battleship can be:
           : 1. all horizontal battleships 
           : 2. all vertical battleships
    Parameter: List[List[str]] - a board with 'X' and '.'
    return: int count - a number of battleship
    Pre-Condition: m == board.length
                 : n == board[i].length
                 : 1 <= m, n <= 200
                 : board[i][j] is either '.' or 'X'.
    Post-Condition: None
'''
# bfs - runtime: O(n*m), memory: O(n*m)
def countBattleships_m2(board: List[List[str]]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    count = 0

    def bfs(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for x, y in directions:
            new_i = i + y
            new_j = j + x
            if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and (new_i, new_j) not in visited and \
                    board[new_i][new_j] != '.':
                bfs(new_i, new_j)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if (i, j) not in visited and board[i][j] == 'X':
                count += 1
                bfs(i, j)
    return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(countBattleships_m1(
        [["."]]
    )) # 0

    print(countBattleships_m1(
        [["X", ".", ".", "X"],
         [".", ".", ".", "X"],
         [".", ".", ".", "X"]]
    )) # 2

    print(countBattleships_m1(
        [["X", ".", "X", "."],
         [".", "X", ".", "X"],
         ["X", ".", "X", "."]]
    )) # 6

    print(countBattleships_m1(
        [["X"]]
    )) # 1

    print("\n === solution 2 === \n")
    print(countBattleships_m2(
        [["."]]
    ))  # 0

    print(countBattleships_m2(
        [["X", ".", ".", "X"],
         [".", ".", ".", "X"],
         [".", ".", ".", "X"]]
    ))  # 2

    print(countBattleships_m2(
        [["X", ".", "X", "."],
         [".", "X", ".", "X"],
         ["X", ".", "X", "."]]
    ))  # 6

    print(countBattleships_m2(
        [["X"]]
    ))  # 1