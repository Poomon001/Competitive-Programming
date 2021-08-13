# https://www.youtube.com/watch?v=ngCos392W4w

'''
    Level: 1
    Purpose: Write a recursive function that given an input n sums all non-negatice integers up to n
    parameter: int - n integers
    return: int - sum of all non negative up to n
    Pre-Condition: non-negaive integer
    Post-Condition: None
'''

def sumN(n:int)->int:
    if(n==0):
        return 0
    # sum of n = sums of k = sum of 1 to n-1 + n
    return sumN(n-1) + n

print(sumN(0)) # 0

'''
 1 
'''
print(sumN(1)) # 1

'''
 1 
 1 + 1
'''
print(sumN(2)) # 3

'''
 1 
 1 + 1
 1 + 1 + 1
'''
print(sumN(3)) # 6

'''
 1 
 1 + 1
 1 + 1 + 1
 1 + 1 + 1 + 1
'''
print(sumN(4)) #10

'''
 1 
 1 + 1
 1 + 1 + 1
 1 + 1 + 1 + 1
 1 + 1 + 1 + 1 + 1
'''
print(sumN(5)) # 15
print("=== Done question# 1 ===")

'''
    Level: 2
    Purpose: Write a function that takes two inputs n and m and outputs the number of unique paths from 
           : the top left corner to bottom right corner of a nxm grid.  
    parameter: int - n integers
             : int - m integers
    return: int - the number of unique paths from the top left corner to bottom right corner of a nxm grid
    Pre-Condition: Can only move down or right 1 unit at a time
                 : m and n are positive integer
    Post-Condition: None
'''

def findAllUniqueGridPath(n: int, m: int) -> int:
    # if we have 1xm or nx1 grid then the only unique is 1 path
    if(n==1 or m==1):
        return 1
    # from multiple testcases, we know that paths of nxm = paths of n-1xm + paths of nxm-1
    # this is becase we only need to go 1 more grid from the unique paths of n-1xm or nxm-1 to get the unique path of nxm
    return findAllUniqueGridPath(n-1, m) + findAllUniqueGridPath(n, m-1)
'''
0 --> 1
'''
print(findAllUniqueGridPath(1,1)) # 1 unique path

'''
0 --> 1
0     1
'''
print(findAllUniqueGridPath(2,1)) # 1 unique path

'''
0 0 --> 1 1
'''
print(findAllUniqueGridPath(1,2)) # 1  unique path

'''
0 0   --> 1 0   or   1 1
0 0       1 1        0 1
'''
print(findAllUniqueGridPath(2,2)) # 2 unique paths

'''
0 0 0   --> 1 0 0   or   1 1 0   or   1 1 1
0 0 0       1 1 1        0 1 1        0 0 1
'''
print(findAllUniqueGridPath(2,3)) # 3 unique paths

'''
0 0   --> 1 0   or   1 0   or   1 1
0 0       1 0        1 1        0 1 
0 0       1 1        0 1        0 1
'''
print(findAllUniqueGridPath(3,2)) # 3 unique paths

'''
0 0 0   --> 1 0 0   -->   1 0 0   --> 1 0 0   -->   1 1 0   -->  1 1 0  --->  1 1 1
0 0 0       1 0 0         1 1 0       1 1 1         0 1 0        0 1 1        0 0 1
0 0 0       1 1 1         0 1 1       0 0 1         0 1 1        0 0 1        0 0 1
'''
print(findAllUniqueGridPath(3,3)) # 6 unique paths

'''
0 0   -->  1 0   -->  1 0   -->   1 0   --> 1 1
0 0        1 0        1 0         1 1       0 1
0 0        1 0        0 1         0 1       0 1
0 0        1 1        0 1         0 1       0 1
'''
print(findAllUniqueGridPath(4,2)) # 4 unique paths
print("=== Done question# 2 ===")

'''
    Level: 3
    Purpose: Write a function that counts the number if ways you can partition n objects using up to m
    parameter: int - n integers (number of objects that partitions need to sum to)
             : int - m integers (number of maximum partition)
    return: int - number of partition
    Pre-Condition: n and m are positive integer
                 : n >= m
    Post-Condition: None
'''
def countPartition(n: int, m: int) -> int:
    # if we have n = n = 0, then only possible solution is 1
    if(n==0):
        return 1

    # alway have 0 because cannot make n from only 0 partition (sum of 0 is 0)
    if(m==0 or n < 1):
        return 0

    # We have n,m-1 partition in n,m partition
    # on top of n,m-1, we have maximum partion m parts to build n,m
    return countPartition(n - m, m) + countPartition(n, m-1)

'''
n = 0 partitions sum to
m = 0 limited biggest partition

0
'''
print(countPartition(0, 0)) # 1

'''
n = 1 partitions sum to
m = 1 limited biggest partition

1
'''
print(countPartition(1, 1)) # 1

'''
n = 2 partitions sum to
m = 1 limited biggest partition

1 + 1 
'''
print(countPartition(2, 1)) # 1

'''
n = 2 partitions sum to
m = 2 limited biggest partition

2 
1 + 1 
'''
print(countPartition(2, 2)) # 2

'''
n = 3 partitions sum to
m = 1 limited biggest partition

1 + 1 + 1
'''
print(countPartition(3, 1)) # 1

'''
n = 3 partitions sum to
m = 2 limited biggest partition

2 + 1
1 + 1 + 1
'''
print(countPartition(3, 2)) # 2

'''
n = 3 partitions sum to
m = 3 limited biggest partition

3
2 + 1
1 + 1 + 1
'''
print(countPartition(3, 3)) # 3

'''
n = 4 partitions sum to
m = 1 limited biggest partition

1 + 1 + 1 + 1
'''
print(countPartition(4, 1)) # 1

'''
n = 4 partitions sum to
m = 2 limited biggest partition

2 + 2
2 + 1 + 1 
1 + 1 + 1 + 1
'''
print(countPartition(4, 2)) # 3

'''
n = 5 partitions sum to
m = 5 limited biggest partition

1 + 1 + 1 + 1 + 1
4 + 1
3 + 2
3 + 1 + 1
2 + 1 + 1 + 1
2 + 2 + 1
5
'''
print(countPartition(5, 5)) # 7

'''
n = 6 partitions sum to
m = 4 limited biggest partition

4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
'''
print(countPartition(6, 4)) # 9
print("=== Done question# 3 ===")