from typing import List
def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    li = []

    # sort top diagonal
    for y in range(len(mat[0])):
        temp = []
        x = 0
        while x < len(mat) and y < len(mat[0]):
            temp.append(mat[x][y])
            x += 1
            y += 1
        temp.sort()
        li.append(temp)

    # sort left diagonal
    for x in range(1, len(mat)):
        temp = []
        y = 0
        while x < len(mat) and y < len(mat[0]):
            temp.append(mat[x][y])
            x += 1
            y += 1
        temp.sort()
        li.append(temp)

    front = 0
    # convert top diagonal to list
    for j in range(len(mat[0])):
        temp = li[front]
        front += 1
        i = 0
        while i < len(mat) and j < len(mat[0]):
            mat[i][j] = temp[i]
            i += 1
            j += 1

    # convert left diagonal to list
    for x in range(1, len(mat)):
        temp = li[front]
        front += 1
        y = 0
        while x < len(mat) and y < len(mat[0]):
            mat[x][y] = temp[y]
            x += 1
            y += 1
    return mat


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
