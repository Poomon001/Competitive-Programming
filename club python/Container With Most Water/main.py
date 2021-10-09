from typing import List

'''
    Link: https://leetcode.com/problems/container-with-most-water/
    Purpose: Find the highest area from a list of lines(height)
    parameter: List[int] - height: a list of number that represents lines' height
    return: int maxArea - a max Area
    Pre-Condition: n == height.length
                 : 2 <= n <= 105
                : 0 <= height[i] <= 104
    Post-Condition: none
'''
# brute force runtime: O(n^2), memory: O(1)
def maxArea_M1(height: List[int]) -> int:
    maxArea = 0
    for i in range(len(height)):
        # reset distance to 0 before each iteration
        distance = 0
        # calculate max area from [currHeight, lastHeight]
        for j in range(i + 1, len(height)):
            # each iteration increase distance by 1
            distance += 1
            currHeight = min(height[i], height[j])
            maxArea = max(maxArea, currHeight * distance)
    return maxArea


'''
    Link: https://leetcode.com/problems/container-with-most-water/
    Purpose: Find the highest area from a list of lines(height)
    parameter: List[int] - height: a list of number that represents lines' height
    return: int maxArea - a max Area
    Pre-Condition: n == height.length
                 : 2 <= n <= 105
                : 0 <= height[i] <= 104
    Post-Condition: none
'''
# two pointer + algo: O(n), memory: O(1)
# 1. we determine maxArea from 1. highest distance, 2. a shorter height of 2 bars.
# 2. Distance will decrease by 1 at max but height can increase by more than 1 (eg. [1, 10, 6] first d=2, h=1, second d=1, h=6)
#    If no higher height is found, the first iteration with the highest distance is the answer.
# We should start with the highest distance (0 and length-1). Then decrease distance by 1 in hope to find a higher height
# To search higher height, we move pointer of a shorter height of two bar.
def maxArea_M2(height: List[int]) -> int:
    front = 0
    back = len(height) - 1
    distance = len(height) - 1
    maxArea = 0
    while (front < back):
        currHeight = min(height[front], height[back])
        maxArea = max(maxArea, currHeight * distance)
        if height[front] < height[back]:
            front += 1
        else:
            back -= 1
        # decreae distance by 1 every iteration
        distance -= 1
    return maxArea


if __name__ == '__main__':
    print(" \n brute force solution")
    print(maxArea_M1([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(maxArea_M1([1, 1]))  # 1
    print(maxArea_M1([4, 3, 2, 1, 4]))  # 16
    print(maxArea_M1([1, 2, 1]))  # 2
    print(maxArea_M1([1, 2, 4, 3]))  # 4

    print(" \n two pointer+aldo solution")
    print(maxArea_M2([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(maxArea_M2([1, 1]))  # 1
    print(maxArea_M2([4, 3, 2, 1, 4]))  # 16
    print(maxArea_M2([1, 2, 1]))  # 2
    print(maxArea_M2([1, 2, 4, 3]))  # 4
