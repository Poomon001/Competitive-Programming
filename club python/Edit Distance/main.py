'''
    Link: CSC 226 Lab# 8
    Purpose: Finding the minimum number of edits (insertion, deletion and replacement) required to
             change one string (str1) into the other (str2)
    parameter: str str1 - a string
             : str str2 - a string
    return: int - the minimum edit distance
    Pre-Condition: len(str1) = len(str2)
                 : len(str1) < 1000
                 : len(str2) < 1000
                 : contain only lowercase characters
    Post-Condition: none
'''
# rumtime: O(n^2), memory: O(n^2)
def minimumEditDistance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # init matrix
    matrix = [[0 for j in range(len1 + 1)] for i in range(len2 + 1)]

    # init first row
    for i in range(len1 + 1):
        matrix[0][i] = i

    # init first column
    for i in range(len2 + 1):
        matrix[i][0] = i

    # fill the rest of the matrix
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

    return matrix[len1][len2]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
      # i
    # 0 1
    e 1 1
    '''
    print(minimumEditDistance("i", "e")) # 1

    '''
      # i n
    # 0 1 2
    e 1 1 2
    x 2 2 2
    '''
    print(minimumEditDistance("in", "ex")) # 2

    '''
          # b a c k
        # 0 1 2 3 4
        b 1 0 1 2 3
        a 2 1 0 1 2
        k 3 1 1 1 1
        e 4 1 2 2 2
    '''
    print(minimumEditDistance("back", "bake")) # 2

    '''
       # i n t e n t i o n
     # 0 1 2 3 4 5 6 7 8 9
     e 1 1 2 3 4 5 6 6 7 8
     x 2 2 2 3 4 5 6 7 7 7
     e 3 3 3 3 4 5 5 6 7 8
     c 4 3 4 3 4 5 6 6 7 8
     u 5 4 4 4 4 5 6 7 7 7
     t 6 5 5 5 5 5 5 6 7 8
     i 7 6 6 6 6 6 6 5 6 7
     o 8 7 7 7 7 7 7 6 5 6
     n 9 8 8 8 8 8 8 7 6 5
    '''
    print(minimumEditDistance("intention", "execution")) # 5

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
