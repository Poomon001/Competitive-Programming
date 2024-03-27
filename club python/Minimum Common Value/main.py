from typing import List

'''
    Link: https://leetcode.com/problems/minimum-common-value
    Purpose: Given two integer arrays nums1 and nums2, sorted in non-decreasing order.
           : Find the minimum common integer to both arrays, return -1 if there is no common integer.
           :  An integer is common if nums1 and nums2 have at least one occurrence of that integer.
    parameter: List[int] num1 - a list of integer
             : List[int] num2 - a list of integer
    return: int - a minimum common integer, -1 if there is no common integer.
    Pre-Condition: 1 <= nums1.length, nums2.length <= 10^5
                 : 1 <= nums1[i], nums2[j] <= 10^9
                 : Both nums1 and nums2 are sorted in non-decreasing order.
    Post-Condition: None
'''
# set intersection - run time: O(n), memory: O(1)
def getCommon_m1(nums1: List[int], nums2: List[int]) -> int:
    common = set(nums1) & set(nums2)
    return -1 if len(common) == 0 else min(common)

'''
    Link: https://leetcode.com/problems/minimum-common-value
    Purpose: Given two integer arrays nums1 and nums2, sorted in non-decreasing order.
           : Find the minimum common integer to both arrays, return -1 if there is no common integer.
           :  An integer is common if nums1 and nums2 have at least one occurrence of that integer.
    parameter: List[int] num1 - a list of integer
             : List[int] num2 - a list of integer
    return: int - a minimum common integer, -1 if there is no common integer.
    Pre-Condition: 1 <= nums1.length, nums2.length <= 10^5
                 : 1 <= nums1[i], nums2[j] <= 10^9
                 : Both nums1 and nums2 are sorted in non-decreasing order.
    Post-Condition: None
'''
# two pointers - run time: O(n), memory: O(1)
def getCommon_m2(nums1: List[int], nums2: List[int]) -> int:
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            return nums1[i]

    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === solution 1 ===\n")
    print(getCommon_m1([1, 2, 3, 10], [2, 4, 10, 11]))  # 2
    print(getCommon_m1([2, 4, 10, 11], [1, 3, 10]))  # 10
    print(getCommon_m1([1, 2, 3, 6], [2, 3, 4, 5]))  # 2
    print(getCommon_m1([1, 2, 3], [2, 4]))  # 2
    print(getCommon_m1([5], [5]))  # 5
    print(getCommon_m1([1], [7]))  # -1
    print(getCommon_m1([1, 2, 3], [7, 8, 9]))  # -1

    print("\n === solution 2 ===\n")
    print(getCommon_m2([1,2,3,10], [2,4,10,11])) # 2
    print(getCommon_m2([2, 4, 10, 11], [1, 3, 10])) # 10
    print(getCommon_m2([1,2,3,6], [2,3,4,5])) # 2
    print(getCommon_m2([1,2,3], [2, 4])) # 2
    print(getCommon_m2([5], [5])) # 5
    print(getCommon_m2([1], [7])) # -1
    print(getCommon_m2([1,2,3], [7,8,9])) # -1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
