from typing import List

'''
    Link: https://leetcode.com/problems/number-of-islands/
    Purpose: Find the number of islands where '1's (land) and '0's
    Parameter: List[List[str]] grid - a 2D matrix of 0 and 1s
    return: int counter - a number of island
    Pre-Condition: m == grid.length
                 : n == grid[i].length
                 : 1 <= m, n <= 300
                 : grid[i][j] is '0' or '1'.
    Post-Condition: None
'''
# dfs - runtime: O(n*m), memory: O(n*m)
def numIslands(grid: List[List[str]]) -> int:
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited = set()
    counter = 0

    def dfs(i, j):
        if (i, j) in visited:
            return

        visited.add((i, j))

        for direction in directions:
            new_j = j + direction[0]
            new_i = i + direction[1]
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and (new_i, new_j) not in visited and grid[new_i][
                new_j] == '1':
                dfs(new_i, new_j)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                counter += 1

    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    grid3 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"],
    ]

    grid4 = [
        ["1", "1", "1"],
    ]
    print(numIslands(grid1)) # 1
    print(numIslands(grid2)) # 3
    print(numIslands(grid3)) # 0
    print(numIslands(grid4)) # 1
