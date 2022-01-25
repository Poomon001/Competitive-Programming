from typing import List

'''
    Link: https://leetcode.com/problems/valid-mountain-array/
    Purpose: Determine if an array is a valid mountain array:
           : arr.length >= 3
           : arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
           : arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    parameter: List[int] - an array of integer
    return: bool - true iff an array is a valid mountain array. Otherwise, false
    Pre-Condition: 1 <= arr.length <= 104
                 : 0 <= arr[i] <= 104
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def validMountainArray(arr: List[int]) -> bool:
    i = 0

    # find if an array lenth is more than 3
    if len(arr) < 3:
        return False

    # check if there is a number before the peek
    if arr[0] > arr[1]:
        return False

    # check incresing order until peek
    while i + 1 < len(arr):
        if arr[i] >= arr[i + 1]:
            # reach the peak where arr[i] = peak
            break
        i += 1

    # check if there is a number after the peek
    if i + 1 == len(arr):
        return False

    # check decresasing order after peek
    while i + 1 < len(arr):
        if arr[i] <= arr[i + 1]:
            return False
        i += 1

    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(validMountainArray([0, 3])) # False
    print(validMountainArray([0])) # False
    print(validMountainArray([0,3,2,1])) # true
    print(validMountainArray([1,2,3,4,5,6,7,8,9])) # False
    print(validMountainArray([9,8,7,6,5,4,3,2,1,0])) # False
    print(validMountainArray([2,0,2])) # False
    print(validMountainArray([0, 2, 0]))  # true
    print(validMountainArray([3,5,5])) # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
