from typing import List
from collections import deque

def dfs_matrix_iterative(board: List[List[str]]):
    # add top, bottom, right, left orderly to the stack
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def dfs(i, j, index):
        stack = deque()
        visited = set()
        stack.append((i, j, index))
        max_length = 0

        while stack:
            i, j, index = stack.pop()
            # - there is no blocker,
            # - not yet visited (No multiple append C-C and C-S e.g [["A", "B", "C", "E"], ["S", "F", "C", "S"])
            if (i, j) in visited or board[i][j] == "":
                continue

            visited.add((i, j))
            print(board[i][j], end="-")
            max_length = max(index + 1, max_length)

            for y, x in directions:
                c = i + y
                r = j + x
                if 0 <= c < len(board) and 0 <= r < len(board[0]) and (c, r) not in visited:
                    stack.append((c, r, index + 1))
        print(max_length)
    dfs(0, 0, 0)


if __name__ == "__main__":
    print("\n=== dfs iterative ===\n")
    dfs_matrix_iterative(
        [["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]]
    ) # A-B-C-E-S-C-F-S-A-D-E-E-
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    ) # A-B-C-C-F-S-A-D-E-E-S-
    print("")
    dfs_matrix_iterative(
        [["A", "", "L", "k"],
        ["", "F", "C", "S"],
        ["A", "D", "E", "E"]]
    ) # A-
    print("")
    dfs_matrix_iterative(
        [["A", "B", "", "k"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    ) # A-B-F-D-A-
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    ) # A-B-C-F-S-A-K-E-E-S-9

    print("\n=== dfs recursive ===\n")
    dfs_matrix_iterative(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-B-C-E-S-C-F-S-A-D-E-E-
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-B-C-C-F-S-A-D-E-E-S-
    print("")
    dfs_matrix_iterative(
        [["A", "", "L", "k"],
         ["", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-
    print("")
    dfs_matrix_iterative(
        [["A", "B", "", "k"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    )  # A-B-F-D-A-
    print("")
    dfs_matrix_iterative(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    )  # A-B-C-F-S-A-K-E-E-S-9