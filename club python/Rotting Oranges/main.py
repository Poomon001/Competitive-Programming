from typing import List
from collections import deque
'''
    Link: https://leetcode.com/problems/rotting-oranges/
    Purpose: Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. 
           : Find the min minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
           : 0 representing an empty cell
           : 1 representing a fresh orange
           : 2 representing a rotten orange
    parameter: List[List[int]] grid - a grid where each cell has one of 0, 1, or 2
    return: int min - the min minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    Pre-Condition: m == grid.length
                 : n == grid[i].length
                 : 1 <= m, n <= 10
                 : grid[i][j] is 0, 1, or 2.
    Post-Condition: none
'''
# BFS: runtime: O(n^2), memory: O(n^2)
def orangesRotting_M1(grid):
    good = set()
    bad = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                good.add((i, j))
            if grid[i][j] == 2:
                bad.add((i, j, 0))

    if not good:
        return 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs():
        queue = deque()
        visited = set()
        queue.extend(bad)
        while queue:
            i, j, level = queue.popleft()

            if (i, j) in visited:
                continue

            visited.add((i, j))

            if grid[i][j] == 1:
                good.remove((i, j))

            if len(good) == 0:
                return level

            for new_i, new_j in directions:
                new_i += i
                new_j += j
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and (new_i, new_j) not in visited and \
                        grid[new_i][new_j] != 0:
                    queue.append((new_i, new_j, level + 1))
        return -1

    return bfs()

'''
    Link: https://leetcode.com/problems/rotting-oranges/
    Purpose: Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. 
           : Find the min minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
           : 0 representing an empty cell
           : 1 representing a fresh orange
           : 2 representing a rotten orange
    parameter: List[List[int]] grid - a grid where each cell has one of 0, 1, or 2
    return: int min - the min minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    Pre-Condition: m == grid.length
                 : n == grid[i].length
                 : 1 <= m, n <= 10
                 : grid[i][j] is 0, 1, or 2.
    Post-Condition: none
'''
# BFS: runtime: O(n^2), memory: O(n^2)
def orangesRotting_M2(grid: List[List[int]]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rottens = set()
    goods = set()

    def bfs():
        queue = deque(rottens)
        visited = set()
        level = 0
        while (len(queue) != 0 and len(goods) > 0):
            temp = deque()
            while (len(queue) != 0):
                i, j = queue.popleft()

                if (i, j) in visited:
                    continue

                visited.add((i, j))
                if (i, j) in goods:
                    goods.remove((i, j))

                for direction in directions:
                    new_i = i + direction[1]
                    new_j = j + direction[0]
                    if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and (new_i, new_j) not in visited and \
                            grid[new_i][new_j] == 1:
                        temp.append((new_i, new_j))
            queue = temp
            if len(goods) > 0:
                level += 1
        return -1 if len(goods) > 0 else level

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rottens.add((i, j))
            if grid[i][j] == 1:
                goods.add((i, j))

    return bfs()


if __name__ == '__main__':
    print("\n == Solution 1 ==\n")
    print(orangesRotting_M1([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(orangesRotting_M1([[2,1,1],[0,1,1],[1,0,1]])) # -1
    print(orangesRotting_M1([[2, 1, 0, 1]])) # -1
    print(orangesRotting_M1([[0,2]])) # 0
    print(orangesRotting_M1([[2,1,0,2]])) # 1
    print(orangesRotting_M1([[2,1,1],[0,1,1],[1,0,1]]))  # -1
    print(orangesRotting_M1([[0]]))  # 0
    print(orangesRotting_M1([[1]]))  # -1
    print(orangesRotting_M1([[2,2],[1,1],[0,0],[2,0]]))  # 1

    print("\n == Solution 2 ==\n")
    print(orangesRotting_M2([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
    print(orangesRotting_M2([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
    print(orangesRotting_M2([[2, 1, 0, 1]]))  # -1
    print(orangesRotting_M2([[0, 2]]))  # 0
    print(orangesRotting_M2([[2, 1, 0, 2]]))  # 1
    print(orangesRotting_M2([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
    print(orangesRotting_M2([[0]]))  # 0
    print(orangesRotting_M2([[1]]))  # -1
    print(orangesRotting_M2([[2, 2], [1, 1], [0, 0], [2, 0]]))  # 1