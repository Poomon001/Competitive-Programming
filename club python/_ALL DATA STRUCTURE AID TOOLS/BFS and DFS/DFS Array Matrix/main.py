from typing import List
from collections import deque

def dfs_matrix_iterative(board: List[List[str]]):
    # add right, left, top, bottom orderly to the stack
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def dfs(i, j, length):
        stack = deque()
        visited = set()
        stack.append((i, j, length))
        max_length = 0

        while stack:
            i, j, length = stack.pop()
            # - there is no blocker,
            # - not yet visited (No multiple append C-C and C-S e.g [["A", "B", "C", "E"], ["S", "F", "C", "S"])
            if (i, j) in visited or board[i][j] == "":
                continue

            visited.add((i, j))
            print(board[i][j], end="-")
            max_length = max(length + 1, max_length)

            for direction in directions:
                new_i = direction[1] + i
                new_j = direction[0] + j
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and (new_i, new_j) not in visited:
                    stack.append((new_i, new_j, length + 1))
        print(max_length)
    dfs(0, 0, 0)


if __name__ == "__main__":
    print("\n=== dfs iterative ===\n")
    dfs_matrix_iterative(
        [["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]]
    ) # A-S-A-D-F-B-C-C-E-E-S-E-12
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    ) # A-S-A-D-F-B-C-C-E-E-S-11
    print("")
    dfs_matrix_iterative(
        [["A", "", "L", "k"],
        ["", "F", "C", "S"],
        ["A", "D", "E", "E"]]
    ) # A-1
    print("")
    dfs_matrix_iterative(
        [["A", "B", "", "k"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    ) # A-B-F-D-A-5
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    ) # A-S-A-K-F-B-C-E-E-S-7

    print("\n=== dfs recursive ===\n")
    dfs_matrix_iterative(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-S-A-D-F-B-C-C-E-E-S-E-12
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-S-A-D-F-B-C-C-E-E-S-11
    print("")
    dfs_matrix_iterative(
        [["A", "", "L", "k"],
         ["", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-1
    print("")
    dfs_matrix_iterative(
        [["A", "B", "", "k"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    )  # A-B-F-D-A-5
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    )  # A-S-A-K-F-B-C-E-E-S-7