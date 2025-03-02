from math import inf
from typing import List

'''
    Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
    Purpose: Given two nums arrays with [uid, value] as elements, merge two array by summing mutual uid value
    parameter: List[List[int]] nums1 - a list of integer with length n
             : List[List[int]] nums2 - a list of integer with length n
    return: List[List[int]] ans - the merged array
    Pre-Condition: 1 <= nums1.length, nums2.length <= 200
                 : nums1[i].length == nums2[j].length == 2
                 : 1 <= idi, vali <= 1000
                 : Both arrays contain unique ids.
                 : Both arrays are in strictly ascending order by id.
    Post-Condition: none
'''
# two pointer: runtime - O(max(n, m)), space: O(m + n)
def mergeArrays_M1(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    ans = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        idx1, num1 = nums1[i]
        idx2, num2 = nums2[j]
        if idx1 < idx2:
            ans.append([idx1, num1])
            i += 1
        elif idx2 < idx1:
            ans.append([idx2, num2])
            j += 1
        else:
            ans.append([idx1, num2 + num1])
            i += 1
            j += 1

    while i < len(nums1):
        idx1, num1 = nums1[i]
        ans.append([idx1, num1])
        i += 1

    while j < len(nums2):
        idx2, num2 = nums2[j]
        ans.append([idx2, num2])
        j += 1

    return ans

'''
    Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
    Purpose: Given two nums arrays with [uid, value] as elements, merge two array by summing mutual uid value
    parameter: List[List[int]] nums1 - a list of integer with length n
             : List[List[int]] nums2 - a list of integer with length n
    return: List[List[int]] ans - the merged array
    Pre-Condition: 1 <= nums1.length, nums2.length <= 200
                 : nums1[i].length == nums2[j].length == 2
                 : 1 <= idi, vali <= 1000
                 : Both arrays contain unique ids.
                 : Both arrays are in strictly ascending order by id.
    Post-Condition: none
'''
# two pointer with compressed loop: runtime - O(max(n, m)), space: O(m + n)
def mergeArrays_M2(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    ans = []
    i = j = 0
    while i < len(nums1) or j < len(nums2):
        idx1, num1 = (inf, 0) if i >= len(nums1) else nums1[i]
        idx2, num2 = (inf, 0) if j >= len(nums2) else nums2[j]
        if idx1 < idx2:
            ans.append([idx1, num1])
            i += 1
        elif idx2 < idx1:
            ans.append([idx2, num2])
            j += 1
        else:
            ans.append([idx1, num2 + num1])
            i += 1
            j += 1

    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n=== solution 1 ===\n")
    print(mergeArrays_M1(
        [[1,2],[2,3],[4,5]],
        [[1,4],[3,2],[4,1]]
    )) # [[1, 6], [2, 3], [3, 2], [4, 6]]
    print(mergeArrays_M1(
        [[2,4],[3,6],[5,5]],
        [[1,3],[4,3]]
    )) # [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
    print(mergeArrays_M1(
        [[1, 3], [4, 3]],
        [[2, 4], [3, 6], [5, 5]]
    )) # [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]

    print("\n=== solution 2 ===\n")
    print(mergeArrays_M2(
        [[1, 2], [2, 3], [4, 5]],
        [[1, 4], [3, 2], [4, 1]]
    ))  # [[1, 6], [2, 3], [3, 2], [4, 6]]
    print(mergeArrays_M2(
        [[2, 4], [3, 6], [5, 5]],
        [[1, 3], [4, 3]]
    )) # [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
    print(mergeArrays_M2(
        [[1, 3], [4, 3]],
        [[2, 4], [3, 6], [5, 5]]
    )) # [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
