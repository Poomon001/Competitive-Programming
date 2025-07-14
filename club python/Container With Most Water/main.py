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
# two pointer + greedy: O(n), memory: O(1)
def maxArea_M2(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    maxStorage = 0

    while left != right:
        storage = (right - left) * min(height[left], height[right])
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

        maxStorage = max(maxStorage, storage)

    return maxStorage


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
