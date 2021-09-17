from typing import List

'''
     Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
     Purpose: Return the intersection list of the 2 given lists
     Parameter: List nums1 - an integer list
              : List nums2 - an integer list
    Returns: List return - the intersection list
    Pre-Condition: 1 <= nums1.length, nums2.length <= 1000
                 : 0 <= nums1[i], nums2[i] <= 1000
    Post-Condition: none
'''

# brute force
# runtime O(nlon(m)), memory: O(n); where n is min(len(num1), len(num2)) and m is max(len(num1), len(num2))
def intersectionofTwoArrays2_M1(nums1: List, nums2: List) -> List:
    result = []

    # determine the shortest lists
    if len(nums1) < len(nums2):
        for n in nums1:
            # search n elem in a searching list
            if n in nums2:
                # add the element to a returning list
                result.append(n)
                # remove the element from the searched list: we need to get exact intersect number
                nums2.remove(n)
    else:
        for n in nums2:
            # search n elem in a searching list
            if n in nums1:
                # add the element to a returning list
                result.append(n)
                # remove the element from the searching list: we need to get exact intersect number
                nums1.remove(n)

    return result

'''
     Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
     Purpose: Return the intersection list of the 2 given lists
     Parameter: List nums1 - an integer list
              : List nums2 - an integer list
    Returns: List return - the intersection list
    Pre-Condition: 1 <= nums1.length, nums2.length <= 1000
                 : 0 <= nums1[i], nums2[i] <= 1000
    Post-Condition: none
'''

# sort
# runtime O(n), memory: O(n); where n is min(len(num1), len(num2))
def intersectionofTwoArrays2_M2(nums1: List, nums2: List) -> List:
    result = []
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            # move nums2 element up 1 position
            j += 1
        elif nums1[i] < nums2[j]:
            # move nums1 element up 1 position
            i += 1
        else:
            # append the intersect to the return list
            result.append(nums1[i])
            # move elements in both list up 1 position
            i += 1
            j += 1

    return result


if __name__ == '__main__':
    t0 = intersectionofTwoArrays2_M1([1, 2, 3], [1, 2, 3, 4, 5])
    print(t0)

    t1 = intersectionofTwoArrays2_M1([4, 9, 5], [9, 4, 9, 8, 4])
    print(t1)

    t2 = intersectionofTwoArrays2_M1([1, 2, 2, 1], [2, 2])
    print(t2)

    t3 = intersectionofTwoArrays2_M1([1, 2, 1], [2, 2])
    print(t3)

    t4 = intersectionofTwoArrays2_M1([1], [2])
    print(t4)

    t5 = intersectionofTwoArrays2_M1([1, 2], [2, 2])
    print(t5)

    t6 = intersectionofTwoArrays2_M1([], [])
    print(t6)

    print(" \n=== end M1 ===\n")

    t0 = intersectionofTwoArrays2_M2([1, 2, 3], [1, 2, 3, 4, 5])
    print(t0)

    t1 = intersectionofTwoArrays2_M2([4, 9, 5], [9, 4, 9, 8, 4])
    print(t1)

    t2 = intersectionofTwoArrays2_M2([1, 2, 2, 1], [2, 2])
    print(t2)

    t3 = intersectionofTwoArrays2_M2([1, 2, 1], [2, 2])
    print(t3)

    t4 = intersectionofTwoArrays2_M2([1], [2])
    print(t4)

    t5 = intersectionofTwoArrays2_M2([1, 2], [2, 2])
    print(t5)

    t6 = intersectionofTwoArrays2_M2([], [])
    print(t6)

    print(" \n=== end M2 ===\n")
