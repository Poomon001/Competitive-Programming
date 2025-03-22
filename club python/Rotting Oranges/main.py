from typing import List

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
# List: runtime: O(n^3), memory: O(n)
def orangesrotten_List(grid: List[List[int]]) -> int:
    # map: [x-axis, y-axis]
    rotten = [] # outer-most visited node
    good = [] # not visited node

    # store the answer
    min = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # locate good orange location
            if grid[y][x] == 1:
                good.append([x,y])

            # locate rotten orange
            if grid[y][x] == 2:
                rotten.append([x,y])

    # Do BFS on 4 directions until: 1. no good orange left, or 2. no path to visit good oranges
    # one BFS hop
    while good:
        # Was good and become bad
        infected = []  # helper to update outer-most visited nodes

        # visit all neighbours of each outer-most visited nodes
        for r in rotten:
            x = r[0]
            y = r[1]

            # visit left neighbour
            if x+1 < len(grid[y]) and [x+1, y] in good:
                grid[y][x+1] = 2
                # remove node from unvisited list and put it to outer-most visited list
                good.remove([x+1, y])
                infected.append([x+1, y])

            # visit right neighbour
            if x - 1 > -1 and [x - 1, y] in good:
                grid[y][x - 1] = 2
                # remove node from unvisited list and put it to outer-most visited list
                good.remove([x - 1, y])
                infected.append([x - 1, y])

            # visit up neighbour
            if y + 1 < len(grid) and [x, y + 1] in good:
                grid[y+1][x] = 2
                # remove node from unvisited list and put it to outer-most visited list
                good.remove([x, y + 1])
                infected.append([x, y + 1])

            # visit down neighbour
            if y - 1 > -1 and [x, y - 1] in good:
                grid[y - 1][x] = 2
                # remove node from unvisited list and put it to outer-most visited list
                good.remove([x, y - 1])
                infected.append([x, y - 1])

        # There is still a good orange but there is no path for BFS (infection) to visit. Thus, impossible.
        if len(infected) == 0:
            return -1

        min += 1

        # clear rotten list b/c now the elements are visited nodes (not outer-most visited)
        rotten.clear()

        # update outer-most visited node to the outer-most visited list
        rotten.extend(infected)

    return min

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
def orangesrotten_Set(grid: List[List[int]]) -> int:
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
    print(orangesrotten_List([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(orangesrotten_List([[2,1,1],[0,1,1],[1,0,1]])) # -1
    print(orangesrotten_List([[2, 1, 0, 1]])) # -1
    print(orangesrotten_List([[0,2]])) # 0
    print(orangesrotten_List([[2,1,0,2]])) # 1
    print(orangesrotten_List([[2,1,1],[0,1,1],[1,0,1]]))  # -1
    print(orangesrotten_List([[0]]))  # 0
    print(orangesrotten_List([[1]]))  # -1
    print(orangesrotten_List([[2,2],[1,1],[0,0],[2,0]]))  # 1