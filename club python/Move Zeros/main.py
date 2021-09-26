from typing import List

'''
    Link: https://leetcode.com/problems/move-zeroes/
    Purpose: Move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    parameter: List[int] - alist of integer
    return: List[int] - a list of integer where all 0's are at the end
    Pre-Condition: 1 <= nums.length <= 104
                 : -231 <= nums[i] <= 231 - 1
    Post-Condition: none
'''
# memory: O(n) and runtime: O(n)
def moveZeroes_M1(nums: List[int]) -> List:
        newNums = []
        numZero = 0

        # append only non-zero
        for num in nums:
            if num == 0:
                numZero += 1
            else:
                newNums.append(num)

        #append zero at the end
        for i in range(numZero):
            newNums.append(0)

        return newNums[:]

'''
    Link: https://leetcode.com/problems/move-zeroes/
    Purpose: Move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    parameter: List[int] - alist of integer
    return: List[int] - a list of integer where all 0's are at the end
    Pre-Condition: 1 <= nums.length <= 104
                 : -231 <= nums[i] <= 231 - 1
    Post-Condition: none
'''
# memory: O(1) and runtime: O(n)
def moveZeroes(nums: List[int]) -> List:
    # keep track of non-zero int
    j = 0
    length = len(nums)

    for i in range(length):
        # if int is non-zero queue from the front
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # after j non-zero int to the end of array, put 0's
    for i in range(j, length):
        nums[i] = 0

    return nums

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(moveZeroes([0,1,0,3,12])) # [1, 3, 12, 0, 0]


