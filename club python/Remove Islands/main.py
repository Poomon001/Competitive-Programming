'''
    Link: https://www.youtube.com/watch?v=4tYoVx0QoN0
    Purpose: Remove isolated islands that do not connect with the boarder land
    parameter: List[List[int]] matrix - 2D matrix of integers: 0 and 1
    return: List[List[int]] matrix -  a new 2D matrix of integers: 0 and 1 after removing isolated islands
    Pre-Condition: 0 <= matrix[i][j] <= 1
                 : 0 <= i, j <= 1000
    Post-Condition: none
'''
# dfs - runtime: O(n*m), space: O(n*m)
def removeIslands(matrix):
    visited = set()

    def dfs(i, j):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if (i, j) not in visited:
            visited.add((i,j))

            for direction in directions:
                new_i = i + direction[1]
                new_j = j + direction[0]
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and (new_i, new_j) not in visited and matrix[new_i][new_j] == 1:
                    dfs(new_i, new_j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1) and (i, j) not in visited:
                dfs(i, j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i, j) not in visited:
                matrix[i][j] = 0

    return matrix

if __name__ == "__main__":
    matrix1 = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
    matrix2 = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
    ]

    matrix3 = [
        [1, 0],
        [0, 1],
        [0, 0],
        [0, 1],
        [0, 0],
        [1, 1],
    ]

    matrix4 = [[]]

    matrix5 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    '''
    [[1, 0, 0, 0, 0, 0], 
     [0, 0, 0, 1, 1, 1], 
     [0, 0, 0, 0, 1, 0], 
     [1, 1, 0, 0, 1, 0], 
     [1, 0, 0, 0, 0, 0], 
     [1, 0, 0, 0, 0, 1]]
    '''
    print(removeIslands(matrix1))

    '''
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    '''
    print(removeIslands(matrix2))

    '''
    [1, 0],
    [0, 1],
    [0, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    '''
    print(removeIslands(matrix3))

    '''
    []
    '''
    print(removeIslands(matrix4))

    '''
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    '''
    print(removeIslands(matrix5))