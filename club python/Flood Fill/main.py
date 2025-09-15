from typing import List

'''
    Link: https://leetcode.com/problems/flood-fill/
    Purpose: Fill the image starting from the pixel image[sr][sc] for each pixel that is directly adjacent pixels.
    parameter: List[List[int]] image - a 2D array
             : int sr - an integer
             : int sc - an integer
             : int color - an integer
    return: List[List[int]] image - the filled image
    Pre-Condition: m == image.length
                 : n == image[i].length
                 : 1 <= m, n <= 50
                 : 0 <= image[i][j], color < 216
                 : 0 <= sr < m
                 : 0 <= sc < n
    Post-Condition: none
'''
# greedy and two pointers- runtime: O(n^2), memory: O(1)
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    color_target = image[sr][sc]

    def dfs(i: int, j: int) -> None:
        if (i, j) in visited:
            return

        visited.add((i, j))
        image[i][j] = color

        for direction in directions:
            new_i = i + direction[1]
            new_j = j + direction[0]
            if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and (new_i, new_j) not in visited and \
                    image[new_i][new_j] == color_target:
                dfs(new_i, new_j)

    dfs(sr, sc)

    return image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    [[2, 2, 2],
     [2, 2, 0], 
     [2, 0, 1]]
    '''
    print(floodFill([
        [1,1,1],
        [1,1,0],
        [1,0,1]
    ], 1, 1, 2))

    '''
    [[1, 1, 1], 
    [1, 1, 0], 
    [1, 0, 2]]
    '''
    print(floodFill([
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ], 2, 2, 2))

    '''
    [[1, 1, 1], 
    [1, 1, 0], 
    [1, 0, 1]]
    '''
    print(floodFill([
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ], 1, 1, 1))

    '''
    [[1, 1, 1], 
    [1, 1, 0], 
    [1, 1, 1]]
    '''
    print(floodFill([
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ], 2, 1, 1))

    '''
    [[1, 1, 1], 
    [1, 1, 1]]
    '''
    print(floodFill([
        [0,0,0],
        [0,0,0]
    ], 1, 1, 1))

    '''
    [[0, 0, 0], 
    [0, 0, 0]]
    '''
    print(floodFill([
        [0, 0, 0],
        [0, 0, 0]
    ], 1, 1, 0))
