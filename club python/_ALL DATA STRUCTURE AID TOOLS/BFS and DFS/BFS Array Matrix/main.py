from typing import List, Tuple
from collections import deque

# runtime - O(m * n), memory - O(n * m)
def bfs_matrix_iterative_multi_sources(board: List[List[str]]):
    # add right, left, top, bottom orderly to the queue
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    max_hop = 0

    def bfs(sources: Tuple[Tuple[int, int, int], ...]):
        nonlocal max_hop
        queue = deque()
        queue.extend(sources)
        visited = set()
        unvisited = set((i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] != "")
        while len(queue) > 0:
            temp = deque()
            while len(queue) > 0:
                i, j, hop = queue.popleft()

                if (i, j) in visited and board[i][j] != "":
                    continue

                visited.add((i, j))
                if (i, j) in unvisited:
                    unvisited.remove((i, j))

                print(board[i][j], end='-')
                max_hop = max(hop, max_hop)

                for direction in directions:
                    new_i = direction[1] + i
                    new_j = direction[0] + j
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and (new_i, new_j) not in visited and board[new_i][new_j] != "":
                        temp.append((new_i, new_j, hop + 1))
            queue = temp
            if len(unvisited) > 0:
                print("", end=f"|{max_hop}|-")

    s1 = (0, 0, 0) # top left most
    s2 = (len(board) - 1, len(board[0]) - 1, 0) # bottom right most
    bfs((s1, s2))
    print(max_hop)

# runtime - O(m * n), memory - O(n * m)
def bfs_matrix_iterative_explicit_level(board: List[List[str]]):
    # add right, left, top, bottom orderly to the queue
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    max_hop = 0

    def bfs(i, j, hop):
        nonlocal max_hop
        queue = deque()
        queue.append((i, j, hop))
        visited = set()
        unvisited = set((i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] != "")
        while len(queue) > 0:
            temp = deque()
            while len(queue) > 0:
                i, j, hop = queue.popleft()

                if (i, j) in visited and board[i][j] != "":
                    continue

                visited.add((i, j))
                if (i, j) in unvisited:
                    unvisited.remove((i, j))

                print(board[i][j], end='-')
                max_hop = max(hop, max_hop)

                for direction in directions:
                    new_i = direction[1] + i
                    new_j = direction[0] + j
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and (new_i, new_j) not in visited and board[new_i][new_j] != "":
                        temp.append((new_i, new_j, hop + 1))
            queue = temp
            if len(unvisited) > 0:
                print("", end=f"|{max_hop}|-")

    bfs(0, 0, 0)
    print(max_hop)

# runtime - O(m * n), memory - O(n * m)
def bfs_matrix_iterative_implicit_level(board: List[List[str]]):
    # add right, left, top, bottom orderly to the queue
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    max_hop = 0
    def bfs(i, j, hop):
        nonlocal max_hop
        queue = deque()
        queue.append((i, j, hop))
        visited = set()
        while len(queue) > 0:
            i, j, hop = queue.popleft()

            if (i, j) in visited and board[i][j] != "":
                continue

            visited.add((i, j))
            print(board[i][j], end='-')
            max_hop = max(hop, max_hop)

            for direction in directions:
                new_i = direction[1] + i
                new_j = direction[0] + j
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and (new_i, new_j) not in visited and board[new_i][new_j] != "":
                    queue.append((new_i, new_j, hop + 1))
    bfs(0, 0, 0)
    print(max_hop)

if __name__ == "__main__":
    print("\n=== bfs iterative 1 ===\n")

    bfs_matrix_iterative_implicit_level(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-B-S-C-F-A-E-C-D-E-E-S-5
    print("")
    bfs_matrix_iterative_implicit_level(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-B-S-C-F-A-C-D-S-E-E-5
    print("")
    bfs_matrix_iterative_implicit_level(
        [["A", "", "L", "k"],
         ["", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-0
    print("")
    bfs_matrix_iterative_implicit_level(
        [["A", "B", "", "k"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    )  # A-B-F-D-A-4
    print("")
    bfs_matrix_iterative_implicit_level(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    )  # A-B-S-C-F-A-K-E-E-S-6

    print("\n=== bfs iterative 2 ===\n")

    bfs_matrix_iterative_explicit_level(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-|0|-B-S-|1|-C-F-A-|2|-E-C-D-|3|-S-E-|4|-E-5
    print("")
    bfs_matrix_iterative_explicit_level(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-|0|-B-S-|1|-C-F-A-|2|-C-D-|3|-S-E-|4|-E-5
    print("")
    bfs_matrix_iterative_explicit_level(
        [["A", "", "L", "k"],
         ["", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-0
    print("")
    bfs_matrix_iterative_explicit_level(
        [["A", "B", "", "k"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    )  # A-|0|-B-|1|-F-|2|-D-|3|-A-4
    print("")
    bfs_matrix_iterative_explicit_level(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    )  # A-|0|-B-S-|1|-C-F-A-|2|-K-|3|-E-|4|-E-|5|-S-6

    print("\n=== bfs multi sources ===\n")

    bfs_matrix_iterative_multi_sources(
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-E-|0|-B-S-E-S|1|-C-F-A-D-C-E-2
    print("")
    bfs_matrix_iterative_multi_sources(
        [["A", "B", "C", ""],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-E-|0|-B-S-E-S-|1|-C-F-A-D-C-2
    print("")
    bfs_matrix_iterative_multi_sources(
        [["A", "", "L", "k"],
         ["", "F", "C", "S"],
         ["A", "D", "E", "E"]]
    )  # A-E-|0|-E-S-|1|-D-C-K-|2|-A-F-L-3
    print("")
    bfs_matrix_iterative_multi_sources(
        [["A", "B", "", "K"],
         ["", "F", "", "S"],
         ["A", "D", "", "E"]]
    )  # A-E-|0|-B-S-|1|-F-K-|2|-D-|3|-A-4
    print("")
    bfs_matrix_iterative_multi_sources(
        [["A", "B", "C", ""],
         ["S", "F", "", "S"],
         ["A", "K", "E", "E"]]
    )  # A-E-|0|-B-S-E-S-|1|-C-F-A-K-2