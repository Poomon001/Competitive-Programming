from typing import List

'''
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
    Purpose: Find remove all duplicates IN-PLACE so that that all duplicate appear at most twice and return the length of a list. 
    parameter: List[int] nums - a list of integer with length n
    return: int - the length of a new list that all duplicate appear at most twice
    Pre-Condition: 1 <= nums.length <= 3 * 10^4
                 : -10^4 <= nums[i] <= 10^4
                 : nums is sorted in non-decreasing order.
    Post-Condition: the input list must contains all duplicates at most twice
'''
# runtime: O(n), memory: O(1)
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = 1
    k = 2
    length = len(nums)

    # less than 3 so no way to get duplicate
    if length < 3:
        return len(nums)

    # detect all thied duplicates and assign None value to it
    while (k < length):
        if nums[i] == nums[j] == nums[k]:
            # need to assign None to the left most duplicate
            # so that we can detect the coming duplicate on the right most
            nums[i] = None

        i += 1
        j += 1
        k += 1

    # remove all None in-place (third duplicate)
    ''' method 1: assign new list to nums (inplace overriden) '''
    nums[:] = [i for i in nums if i is not None]

    ''' method 2: append i to num and slice new part (inplace appending) '''
    # for i in range(length):
    #     if nums[i] is not None:
    #         nums.append(nums[i])
    # nums[:] = nums[length:]

    ''' method 3: i run while j stop at None and swap (inplace swap) '''
    # keep track of None
    # j = 0
    # for i in range(len(nums)):
    #     if nums[i] is not None:
    #         nums[i], nums[j] = nums[j], nums[i]
    #         j += 1
    #
    # nums[:] = nums[:j]

    return len(nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [1,1,1,2,2,3]
    nums2 = [1, 1, 1, 2, 2]
    nums3 = [0,0,1,1,1,1,2,3,3]
    nums4 = [0]

    print(removeDuplicates(nums1)) # 5
    print(nums1) # [1, 1, 2, 2, 3]

    print(removeDuplicates(nums2))  # 4
    print(nums2)  # [1, 1, 2, 2]

    print(removeDuplicates(nums3))  # 7
    print(nums3)  # [0,0,1,1,2,3,3]

    print(removeDuplicates(nums4))  # 1
    print(nums4)  # [0]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
