from typing import List

'''
    Purpose: Find all integers in which cannot find in anywhere else in all other lists in a increasing order.
    parameter: List[List[int]] nums - a list of integer lists 
    return: List[int] numsList - a list of integer that  cannot find in any other lists. 
    Pre-Condition: 1 <= len(nums) <= 100
                 : 1 <= len(nums[i]) <= 1000
                 : nums[i] are integer
'''
# brute force: runtime: O(n^4), memory: O(n)
def uniqueIntegerArray_method1(numsList: List[List[int]]) -> List[int]:
    answer = set()
    for i in range(len(numsList)):
        for j in range(len(numsList[i])):
            currNum = numsList[i][j]
            for k in range(len(numsList)):
                if k == i:
                    continue
                if currNum in numsList[k]:
                    break
            else:
                answer.add(currNum)

    return sorted(list(answer))

# set operations: runtime: O(n^3), memory: O(n)
def uniqueIntegerArray_method2(numsList: List[List[int]]) -> List[int]:
    answer = set()
    for i in range(len(numsList)):
        temp = set(numsList[i])
        for j in range(len(numsList)):
            if i != j:
                other = set(numsList[j])
                temp = temp - other
        answer = answer | temp
    return sorted(list(answer))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numsList0 = [[1, 2, 3, 3, 2,], [3, 4, 5, 6, 7], [7, 5, 6]] # [1,2,4]
    numsList1 = [[1,2,3,4,5,6],[1,1,1,1,1],[0,0],[4,5,6,7,7,7],[1],[5,6,7]] # 0,2,3
    numsList2 = [[1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1], [0, 0], [4, 5, 6, 7, 7, 7], [1], [5]]  # 0,2,3,7
    numsList3 = [[1, 1, 1, 1, 1], [0, 0], [4, 5, 6, 7, 7, 7], [1], [5, 6, 7],[1, 2, 3, 4, 5, 6]]  # 0,2,3
    numsList4 = [[1, 1, 1, 1, 1], [0, 0], [4], [1], [2], [3, 5, 6]] # 0,2,3,4,5,6
    numsList5 = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]  # 0,1,2,3,4,5,6,7,8,9,10
    numsList6 = [[10], [9], [8], [7], [6], [5], [4], [3], [2], [1], [0]]  # 0,1,2,3,4,5,6,7,8,9,10
    numsList7 = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10], [10]]  #
    numsList8 = [[10], [6,7,8], [1,2,11,9], [7,8,9], [7,8,9], [10,2,3,4,6], [10,2,3,4], [10,8,9], [5], [2,3,4,10], [10,9,1]]  # [5,11]

    print("\n+=== Solution 1 ===+\n")

    print(uniqueIntegerArray_method1(numsList0))
    print(uniqueIntegerArray_method1(numsList1))
    print(uniqueIntegerArray_method1(numsList2))
    print(uniqueIntegerArray_method1(numsList3))
    print(uniqueIntegerArray_method1(numsList4))
    print(uniqueIntegerArray_method1(numsList5))
    print(uniqueIntegerArray_method1(numsList6))
    print(uniqueIntegerArray_method1(numsList7))
    print(uniqueIntegerArray_method1(numsList8))

    print("\n+=== Solution 2 ===+\n")

    print(uniqueIntegerArray_method2(numsList0))
    print(uniqueIntegerArray_method2(numsList1))
    print(uniqueIntegerArray_method2(numsList2))
    print(uniqueIntegerArray_method2(numsList3))
    print(uniqueIntegerArray_method2(numsList4))
    print(uniqueIntegerArray_method2(numsList5))
    print(uniqueIntegerArray_method2(numsList6))
    print(uniqueIntegerArray_method1(numsList7))
    print(uniqueIntegerArray_method1(numsList8))
