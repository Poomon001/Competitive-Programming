from typing import List

'''
    Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
    Purpose: Find the single element that appears only once 
           : from an array of integers where every element appears exactly twice, except for the one element 
    parameter: List[int] nums - a list of integers where every element appears exactly twice, except for the one element 
    return: int - an element that appear once
    Pre-Condition: 1 <= nums.length <= 10^5
                 : 0 <= nums[i] <= 10^5
    Post-Condition: none
'''
# runtime: O(log(n)), memory: O(1)
def singleNonDuplicate(nums: List[int]) -> int:
    front = 0
    back = len(nums) - 1

    while (front < back):
        mid = (front + back) // 2

        # check if mid the answer
        if (mid - 1 > 0 and nums[mid] != nums[mid - 1]) and (mid + 1 < len(nums) and nums[mid] != nums[mid + 1]):
            return nums[mid]

        # check for an answer when 3 element left
        if back - front == 2:
            if nums[mid] == nums[front]:
                return nums[back]
            else:
                return nums[front]

        # check if mid has a duplicate on its left.
        # this case makes [0, m] contains answer if there are odd elements from [0, m] eg, [1, 1, ... x, ... midDup, mid]
        if mid - 1 > 0 and nums[mid] == nums[mid - 1]:
            # if there are even elements from [0, m], we can ignore [0 to midDup, mid].
            if (mid + 1) % 2 == 0:
                front = mid + 1

            # if there are odd elements from [0, m], we can ignore [midDup, mid to end]
            if (mid + 1) % 2 == 1:
                back = mid - 2

            continue

        # check if mid has a duplicate on its right.
        # this case makes [0, m] contains answer if there are even elements from [0, m] eg, [1, 1, ... x, ... mid], midDup
        if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
            # if there are even elements from [0, m], we can ignore [midDup, mid to end].
            if (mid + 1) % 2 == 0:
                back = mid - 1

            # if there are odd elements from [0, m], we can ignore [0 to midDup, mid]
            if (mid + 1) % 2 == 1:
                front = mid + 2

            continue

    return nums[front]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(singleNonDuplicate([1])) # 1
    print(singleNonDuplicate([0, 1, 1, 2, 2, 5, 5])) # 0
    print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])) # 2
    print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])) # 10
    print(singleNonDuplicate([1, 1, 2, 2, 3])) # 3
    print(singleNonDuplicate([1, 2, 2, 3, 3])) # 1
    print(singleNonDuplicate([1, 1, 2, 3, 3])) # 2

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
