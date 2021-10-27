from typing import List

'''
    Link: https://leetcode.com/problems/sort-colors/
    Purpose: Let 0, 1, and 2 represent 3 unique colors. In-place sorted and group the colors.
    parameter: List[int] nums - a list of number representing the 3 colors 
    return: List[int] nums - a sorted and grouped list of colors
    Pre-Condition: None
    Post-Condition: Must change only nums.
'''
# runtime: O(n), memory: O(1)
def sortColors(nums: List[int]) -> List[int]:
    front = 0

    # get all 0s to the front
    for runner in range(len(nums)):
        # if 0 is found, swap 0 with the front-most non-zero element
        if nums[runner] == 0:
            nums[runner] = nums[front]
            nums[front] = 0
            front += 1

    # get all 1s after all 0s
    for runner in range(front, len(nums)):
        # if 1 is found, swap 1 with the front-most non-one element (the position is located after all 0s)
        if nums[runner] == 1:
            nums[runner] = nums[front]
            nums[front] = 1
            front += 1

    return nums


if __name__ == '__main__':
    print(sortColors([2,0,0,0,2,1,2,1,1,0])) # [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]
    print(sortColors([2,0,2,1,1,0])) # [0, 0, 1, 1, 2, 2]
    print(sortColors([2,0,1])) # [0, 1, 2]
    print(sortColors([0])) # [0]
    print(sortColors([1])) # [1]

