from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = 1
    k = 2

    # less than 3 so no way to get duplicate
    if len(nums) < 3:
        return len(nums)

    # detect all thied duplicates and assign None value to it
    while (k < len(nums)):
        if nums[i] == nums[j] == nums[k]:
            # need to assign None to the left most duplicate
            # so that we can dectect the coming duplicate on the right most
            nums[i] = None

        i += 1
        j += 1
        k += 1

    # remove all None (third duplicate) by moving them to the back and slice them
    nums[:] = [i for i in nums if i is not None]

    return len(nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [1,1,1,2,2,3]
    nums2 = [1, 1, 1, 2, 2]
    nums3 = [0,0,1,1,1,1,2,3,3]
    print(removeDuplicates(nums1)) # 5
    print(nums1) # [1, 1, 2, 2, 3]

    print(removeDuplicates(nums2))  # 4
    print(nums2)  # [1, 1, 2, 2]

    print(removeDuplicates(nums3))  # 7
    print(nums3)  # [0,0,1,1,2,3,3]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
