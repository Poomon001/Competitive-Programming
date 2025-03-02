from typing import List
from collections import deque

'''
    Link: https://leetcode.com/problems/word-search/submissions/1553550738
    Purpose: Determine if the board contains a consecutive sequence of characters to form a target word
    parameter: List[int] board - a matrix array of upper case chars
             : str word - an english word in upper case
    return: bool - True is the board contains a consecutive sequence of characters to form a target word, else False 
    Pre-Condition: m == board.length
                 : n = board[i].length
                 : 1 <= m, n <= 6
                 : 1 <= word.length <= 15
                 : board and word consists of only lowercase and uppercase English letters.
    Post-Condition: none
'''
# DFS recursive - O(m * n * 4^L), memory - O(m*n*L), visited has max(n*m) and stack contain at most L char
# where m*n is the board size, 4 is the power set of 4 direction backtracking, and L is the word length
def WordSearch_Recursive(board: List[List[str]], word: str):
    visited = set()
    def dfs(i, j, index):
        # check index bound , matching word, and is visited
        if not (0 <= i < len(board)) or not 0 <= j < len(board[0]) or\
                (i, j) in visited or board[i][j] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        visited.add((i, j))

        ans = dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or \
            dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1)

        visited.remove((i, j))

        return ans

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
    return False

# DFS iterative: runtime - O(m * n * 4^L), memory - O(m*n*L), visited has max(n*m) and stack contain at most L char
# where m*n is the board size, 4 is the power set of 4 direction backtracking, and L is the word length
def WordSearch_Iterative(board: List[List[str]], word: str):
    # add top, bottom, right, left orderly to the stack
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def dfs(i, j, index):
        stack = deque()
        visited = set()
        stack.append((i, j, index, visited))
        while stack:
            i, j, index, visited = stack.pop()

            visited.add((i, j))

            if index == len(word) - 1:
                return True

            for y, x in directions:
                c = i + y
                r = j + x
                # check for the next char
                if 0 <= c < len(board) and 0 <= r < len(board[0]) and (c, r) not in visited and board[c][r] == word[index + 1]:
                    stack.append((c, r, index + 1, visited.copy()))
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
    return False

# DFS iterative: runtime - O(m * n * 4^L), memory - O(m * n), visited has max(n*m)
# where m*n is the board size, 4 is the power set of 4 direction backtracking, and L is the word length
def WordSearch_Iterative_Optimize(board: List[List[str]], word: str):
    # add top, bottom, right, left orderly to the stack
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def dfs(i, j, index):
        stack = deque()
        visited = set()
        stack.append((i, j, index, False))
        while stack:
            i, j, index, is_backtrack = stack.pop()

            if is_backtrack:
                visited.remove((i, j)) # note: normal dfs will just backtrack without remoting
                continue

            visited.add((i, j))

            # Just preventing a re-visit during exploration,
            # later will be removed right away during backtrack to allow re-visit from a different path
            stack.append((i, j, index, True))

            if index == len(word) - 1:
                return True

            for y, x in directions:
                c = i + y
                r = j + x
                # check for the next char
                if 0 <= c < len(board) and 0 <= r < len(board[0]) and (c, r) not in visited and board[c][r] == word[index + 1]:
                    stack.append((c, r, index + 1, False))
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
    return False


if __name__ == '__main__':
    print("\n === Recursive === \n")
    print(WordSearch_Recursive(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "ABCCED"
    ))  # True

    print(WordSearch_Recursive(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "SEE"
    ))  # True

    print(WordSearch_Recursive(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "ABCB"
    ))  # False

    print(WordSearch_Recursive(
        [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]],
        "ABCESEEEFS"
    ))  # True

    print(WordSearch_Recursive(
        [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "X"]],
        "ABCESEEEFS"
    ))  # False

    print(WordSearch_Recursive(
        [["A", "B"],
         ["S", "F"]],
        "ABCB"
    ))  # False

    print(WordSearch_Recursive(
        [["A", "B", "C", "E"],
         ["S", "C", "E", "O"],
         ["S", "E", "E", "E"]],
        "ABCES"
    ))  # True

    print("\n === Iterative === \n")

    print(WordSearch_Iterative(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "ABCCED"
    ))  # True

    print(WordSearch_Iterative(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "SEE"
    ))  # True

    print(WordSearch_Iterative(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]],
        "ABCB"
    ))  # False

    print(WordSearch_Iterative(
        [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]],
        "ABCESEEEFS"
    ))  # True

    print(WordSearch_Iterative(
        [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "X"]],
        "ABCESEEEFS"
    ))  # False

    print(WordSearch_Iterative(
        [["A", "B"],
         ["S", "F"]],
        "ABCB"
    ))  # False

    print(WordSearch_Iterative(
        [["A", "B", "C", "E"],
         ["S", "C", "E", "O"],
         ["S", "E", "E", "E"]],
        "ABCES"
    ))  # True

    print("\n === Iterative Optimization === \n")
    # print(WordSearch_Iterative_Optimize(
    #     [["A", "B", "C", "E"],
    #      ["S", "F", "C", "S"],
    #      ["A", "D", "E", "E"]],
    #     "ABCCED"
    # ))  # True
    #
    # print(WordSearch_Iterative_Optimize(
    #     [["A", "B", "C", "E"],
    #      ["S", "F", "C", "S"],
    #      ["A", "D", "E", "E"]],
    #     "SEE"
    # ))  # True
    #
    # print(WordSearch_Iterative_Optimize(
    #     [["A", "B", "C", "E"],
    #      ["S", "F", "C", "S"],
    #      ["A", "D", "E", "E"]],
    #     "ABCB"
    # ))  # False

    print(WordSearch_Iterative_Optimize(
        [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]],
        "ABCESEEEFS"
    ))  # True

    print(WordSearch_Iterative_Optimize(
        [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "X"]],
        "ABCESEEEFS"
    ))  # False

    # print(WordSearch_Iterative_Optimize(
    #     [["A", "B"],
    #      ["S", "F"]],
    #     "ABCB"
    # ))  # False

    print(WordSearch_Iterative_Optimize(
        [["A", "B", "C", "E"],
         ["S", "C", "E", "O"],
         ["S", "E", "E", "E"]],
        "ABCES"
    ))  # True

