from typing import List

'''     
    Link: https://leetcode.com/problems/merge-sorted-array/
    Purpose: Merge 2 sorted lists in-place.
    Parameter: List[int] nums1 - the first sorted list with 0 spaces at the end
             : int m - length of the first list without 0 spaces
             : List[int] nums2 - the second sorted list with 0 spaces at the end
             : int n - length of the second list
    Returns: List[int] nums1 - a merged list
    Pre-Condition: nums1.length == m + n
                 : nums2.length == n
                 : 0 <= m, n <= 200
                 : 1 <= m + n <= 200
                 : -109 <= nums1[i], nums2[j] <= 109
    Post-Condition: none
'''
# HACK Sort Solution: runtime: O(n), memory: O(1)
def merge_M1(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    while n != 0:
        nums1.pop()
        n -= 1

    nums1.extend(nums2)
    nums1.sort()
    return nums1

'''     
    Link: https://leetcode.com/problems/merge-sorted-array/
    Purpose: Merge 2 sorted lists in-place.
    Parameter: List[int] nums1 - the first sorted list with 0 spaces at the end
             : int m - length of the first list without 0 spaces
             : List[int] nums2 - the second sorted list with 0 spaces at the end
             : int n - length of the second list
    Returns: List[int] nums1 - a merged list
    Pre-Condition: nums1.length == m + n
                 : nums2.length == n
                 : 0 <= m, n <= 200
                 : 1 <= m + n <= 200
                 : -109 <= nums1[i], nums2[j] <= 109
    Post-Condition: none
'''
# merge then sort: runtime: O(n), memory: O(1)
def merge_M2(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    i = n + m -1
    j = n -1
    while j >= 0:
        nums1[i] = nums2[j]
        i -= 1
        j -= 1
    nums1.sort()
    return nums1

'''     
    Link: https://leetcode.com/problems/merge-sorted-array/
    Purpose: Merge 2 sorted lists in-place.
    Parameter: List[int] nums1 - the first sorted list with 0 spaces at the end
             : int m - length of the first list without 0 spaces
             : List[int] nums2 - the second sorted list with 0 spaces at the end
             : int n - length of the second list
    Returns: List[int] nums1 - a merged list
    Pre-Condition: nums1.length == m + n
                 : nums2.length == n
                 : 0 <= m, n <= 200
                 : 1 <= m + n <= 200
                 : -109 <= nums1[i], nums2[j] <= 109
    Post-Condition: none
'''
# Filling backwards with 3 pointers: runtime: O(n), memory: O(1)
def merge_M3(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    # keep tract at the end of numbders before a list of 0s
    i = m - 1

    # keep tract at the end of the nums2
    j = n - 1

    # keep track of avaliable 0 space
    k = n + m - 1

    while(j >= 0):
        if i >= 0 and nums1[i] > nums2[j]:
            # swap 0 space with nums[i] in front of it
            nums1[k] = nums1[i]
            nums1[i] = 0
            k -= 1
            i -= 1
        else:
            # replace 0 space with nums2[j]
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    return nums1


if __name__ == '__main__':
    print("\n === hack merge and sort ===")
    print(merge_M1([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(merge_M1([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
    print(merge_M1([0], 0, [1], 1))
    print(merge_M1([2, 0], 1, [1], 1))

    print("\n === rigid merge and sort ===")
    print(merge_M2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(merge_M2([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
    print(merge_M2([0], 0, [1], 1))
    print(merge_M2([2, 0], 1, [1], 1))

    print("\n === filling backwards with 3 pointers ===")
    print(merge_M3([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(merge_M3([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
    print(merge_M3([0], 0, [1], 1))
    print(merge_M3([2,0], 1, [1], 1))

