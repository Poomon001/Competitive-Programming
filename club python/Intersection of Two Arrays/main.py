from typing import List

'''
    Link: https://leetcode.com/problems/intersection-of-two-arrays
    Purpose: Find intersection of 2 lists
    parameter: List[int] nums1 - a list of integer
             : List[int] nums2 - a list of integer 
    return: List[int] - a list of intersection between nums1 and nums2 
    Pre-Condition: 1 <= nums1.length, nums2.length <= 1000
                 : 0 <= nums1[i], nums2[i] <= 1000
    Post-Condition: none
'''
# runtime: O(n) where n is min(nums11, nums2), memory: O(1)
def intersection_M1(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return nums1 & nums2

'''
    Link: https://leetcode.com/problems/intersection-of-two-arrays
    Purpose: Find intersection of 2 lists
    parameter: List[int] nums1 - a list of integer
             : List[int] nums2 - a list of integer 
    return: List[int] - a list of intersection between nums1 and nums2 
    Pre-Condition: 1 <= nums1.length, nums2.length <= 1000
                 : 0 <= nums1[i], nums2[i] <= 1000
    Post-Condition: none
'''
# runtime: O(nlog(n)) where n is min(nums11, nums2), memory: O(1) -> answer doesn't count
def intersection_M2(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    intersection = set()
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersection.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return intersection

'''
    Link: https://leetcode.com/problems/intersection-of-two-arrays
    Purpose: Find intersection of 2 lists
    parameter: List[int] nums1 - a list of integer
             : List[int] nums2 - a list of integer 
    return: List[int] - a list of intersection between nums1 and nums2 
    Pre-Condition: 1 <= nums1.length, nums2.length <= 1000
                 : 0 <= nums1[i], nums2[i] <= 1000
    Post-Condition: none
'''
# runtime: O(n) where n is min(nums11, nums2), memory: O(1) -> answer doesn't count
def intersection_M3(nums1: List[int], nums2: List[int]) -> List[int]:
    intersection = set()
    nums1 = set(nums1)
    for i in nums2:
        # this "in" time complexity is O(1)
        if i in nums1:
            intersection.add(i)

    return intersection






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+==== M1 ====+\n")
    print(intersection_M1([1, 2, 2, 1], [2, 2]))  # 2
    print(intersection_M1([4, 9, 5], [9, 4, 9, 8, 4]))  # 9, 4
    print(intersection_M1([4, 9, 5], [9, 4, 5]))  # 9, 4, 5
    print(intersection_M1([2, 3, 6, 7], [1, 3, 4, 5]))  # 3

    print("\n+==== M2 ====+\n")
    print(intersection_M2([1, 2, 2, 1], [2, 2]))  # 2
    print(intersection_M2([4, 9, 5], [9, 4, 9, 8, 4]))  # 9, 4
    print(intersection_M2([4, 9, 5], [9, 4, 5]))  # 9, 4, 5
    print(intersection_M2([2, 3, 6, 7], [1, 3, 4, 5]))  # 3

    print("\n+==== M3 ====+\n")
    print(intersection_M3([1,2,2,1], [2,2])) # 2
    print(intersection_M3([4,9,5], [9,4,9,8,4])) # 9, 4
    print(intersection_M3([4, 9, 5], [9, 4, 5])) # 9, 4, 5
    print(intersection_M3([2, 3, 6, 7], [1 , 3, 4, 5])) # 3

