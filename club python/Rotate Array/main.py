from typing import List

'''
    Link: https://leetcode.com/problems/rotate-array/
    Purpose: Find an array after rotating it to the right by k steps
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: List[int] nums - a list of integer
          : int k - a number of rotations
    Pre-Condition: 1 <= nums.length <= 10^5
                 : -2^31 <= nums[i] <= 2^31 - 1
                 : 0 <= k <= 10^5
    Post-Condition: none
'''
# Find final head and slicing solution: runtime: O(n), memory: O(1)
def rotate_M1(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # pointer to the head of a rotated list
    j = 0

    # get head index of the new rotated list (after Kth rotations)
    # eg: 1,2,3,4,5 and k=9 then new head is 2
    for _ in range(k):
        j = j - 1

        # point to the back
        if j == -1:
            j = len(nums)-1

    # move all elements [from the start index to the index before the new head] to be after the new head
    nums[:] = nums[j:] + nums[:j]

'''
    Link: https://leetcode.com/problems/rotate-array/
    Purpose: Find an array after rotating it to the right by k steps
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: List[int] nums - a list of integer
          : int k - a number of rotations
    Pre-Condition: 1 <= nums.length <= 10^5
                 : -2^31 <= nums[i] <= 2^31 - 1
                 : 0 <= k <= 10^5
    Post-Condition: none
'''
# looping and appending solution: runtime: O(nk), memory: O(1)
def rotate_M2(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)

    # loop K times, O(k)
    for _ in range(k):
        # rotate by add all elements except the last element to the back of the list orderly
        for i in range(length - 1):
            nums.append(nums[i])

        # get a rotated list
        nums[:] = nums[length - 1:]

'''
    Link: https://leetcode.com/problems/rotate-array/
    Purpose: Find an array after rotating it to the right by k steps
    parameter: Optional[TreeNode] root - a root of a binary tree
    return: List[int] nums - a list of integer
          : int k - a number of rotations
    Pre-Condition: 1 <= nums.length <= 10^5
                 : -2^31 <= nums[i] <= 2^31 - 1
                 : 0 <= k <= 10^5
    Post-Condition: none
'''
# two pointer solution: runtime: O(nk), memory: O(1)
def rotate_M3(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(k):
        # keep track of the last element
        j = len(nums) - 1

        # rotate by using the last index as a storage of a previous number
        for i in range(len(nums)):
            swap(i, j, nums)

def swap(i: int, j: int, nums: List[int]) -> None:
    nums[i], nums[j] = nums[j], nums[i]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution M1 ===+\n")
    nums1 = [1,2,3,4,5]
    rotate_M1(nums1, 9)
    print(nums1)

    nums2 = [1, 2, 3, 4, 5, 6, 7]
    rotate_M1(nums2, 3)
    print(nums2)

    nums3 = [1, 2]
    rotate_M1(nums3, 5)
    print(nums3)

    nums4 = [1, 2, 3, 4, 5, 6, 7]
    rotate_M1(nums4, 92)
    print(nums4)

    print("\n+=== solution M2 ===+\n")
    nums5 = [1, 2, 3, 4, 5]
    rotate_M2(nums5, 9)
    print(nums5)

    nums6 = [1, 2, 3, 4, 5, 6, 7]
    rotate_M2(nums6, 3)
    print(nums6)

    nums7 = [1, 2]
    rotate_M2(nums7, 5)
    print(nums7)

    nums8 = [1, 2, 3, 4, 5, 6, 7]
    rotate_M2(nums8, 92)
    print(nums8)

    print("\n+=== solution M3 ===+\n")
    nums9 = [1, 2, 3, 4, 5]
    rotate_M3(nums9, 9)
    print(nums9)

    nums10 = [1, 2, 3, 4, 5, 6, 7]
    rotate_M3(nums10, 3)
    print(nums10)

    nums11 = [1, 2]
    rotate_M3(nums11, 5)
    print(nums11)

    nums12 = [1, 2, 3, 4, 5, 6, 7]
    rotate_M3(nums12, 92)
    print(nums12)

