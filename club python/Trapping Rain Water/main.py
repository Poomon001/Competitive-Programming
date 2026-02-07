from typing import List

'''
    Link: https://leetcode.com/problems/trapping-rain-water/
    Purpose: Find how much water it can trap after raining.
           : Given n non-negative integers representing an elevation map where the width of each bar is 1.
    parameter: List[int] height - non-negative integers representing an elevation map where the width of each bar is 1
    return: int capacity - a trapping water after raining
    Pre-Condition: n == height.length
                 : 1 <= n <= 2 * 10^4
                 : 0 <= height[i] <= 10^5
    Post-Condition: none
'''
# Array - runtime: O(n), memory: O(n)
def trap(height: List[int]) -> int:
    # get the capacity at height[i] = min(highest_left_wall[i], highest_right_wall[i]) - height[i]

    highest_left_walls = [0] * len(height)
    highest_right_walls = [0] * len(height)
    capacity = 0

    highest_wall = 0
    for i in range(1, len(height)):
        highest_wall = max(highest_wall, height[i - 1])
        highest_left_walls[i] = highest_wall

    highest_wall = 0
    for i in range(len(height) - 2, -1, -1):
        highest_wall = max(highest_wall, height[i + 1])
        highest_right_walls[i] = highest_wall

    for i in range(len(height)):
        curr_capacity = min(highest_left_walls[i], highest_right_walls[i]) - height[i]
        capacity += curr_capacity if curr_capacity > 0 else 0

    return capacity


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(trap([4,2,0,3,2,5])) # 9
    print(trap([4])) # 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
