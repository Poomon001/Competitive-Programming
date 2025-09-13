from typing import List

'''
    Link: https://leetcode.com/problems/move-zeroes/
    Purpose: Move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    parameter: List[int] - alist of integer
    return: List[int] - a list of integer where all 0's are at the end
    Pre-Condition: 1 <= nums.length <= 104
                 : -2^31 <= nums[i] <= 2^31 - 1
    Post-Condition: none
'''
# in-place swap: runtime: O(n), memory: O(1)
def moveZeroes_M1(nums: List[int]) -> List:
    # 1. create 2 pointer: i and j
    # 2. i will keep track of 0's
    # 3. j will keep track of non-0's
    # 4. i and j needs to be swapped if j is non-zeros

    i = 0  # keep track of the left-most 0

    for j in range(len(nums)):
        while i < len(nums) and nums[i] != 0:
            i += 1

        if nums[j] != 0 and i < j:
            nums[j], nums[i] = nums[i], nums[j] # swap
    return nums
'''
    Link: https://leetcode.com/problems/move-zeroes/
    Purpose: Move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    parameter: List[int] - alist of integer
    return: List[int] - a list of integer where all 0's are at the end
    Pre-Condition: 1 <= nums.length <= 104
                 : -2^31 <= nums[i] <= 2^31 - 1
    Post-Condition: none
'''
# in-place overwrite: runtime: O(n), memory: O(1)
def moveZeroes_M2(nums: List[int]) -> List:
    # keep track of non-zero int
    j = 0

    for i in range(len(nums)):
        # if int is non-zero, overwrite it at the front
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # put 0's from the j index to the end of array
    for i in range(j, len(nums)):
        nums[i] = 0

    return nums

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n ==== Solution M1 ==== \n")
    print(moveZeroes_M1([1, 1, 3, 12, 2])) # [1, 1, 3, 12, 2]
    print(moveZeroes_M1([1])) # [1]
    print(moveZeroes_M1([0])) # [0]
    print(moveZeroes_M1([0, 1, 0, 3, 12])) # [1, 3, 12, 0, 0]
    print(moveZeroes_M1([0, 0, 0, 0, 1, 0, 3, 12])) # [1, 3, 12, 0, 0, 0, 0, 0]
    print(moveZeroes_M1([1, 0, 0, 0, 0, 3, 0, 0, 0, 12, 0])) # [1, 3, 12, 0, 0, 0, 0, 0, 0, 0, 0]

    print("\n ==== Solution M2 ==== \n")
    print(moveZeroes_M2([1, 1, 3, 12, 2]))  # [1, 1, 3, 12, 2]
    print(moveZeroes_M2([1]))  # [1]
    print(moveZeroes_M2([0]))  # [0]
    print(moveZeroes_M2([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
    print(moveZeroes_M2([0, 0, 0, 0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0, 0, 0, 0]
    print(moveZeroes_M2([1, 0, 0, 0, 0, 3, 0, 0, 0, 12, 0]))  # [1, 3, 12, 0, 0, 0, 0, 0, 0, 0, 0]

