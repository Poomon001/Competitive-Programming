from typing import List

'''
    Link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x
    Purpose: Find Special number = x where
           : x is the exact total number of elements in nums that are great or equal to x
    parameter: List[int] nums - a list of integers
    return: int - special number x if exist. Otherwise, return -1
    Pre-Condition: 1 <= nums.length <= 100
                 : 0 <= nums[i] <= 1000
    Post-Condition: none
'''
# sort - runtime: O(nlog(n)), memory: O(n)
def specialArray_M1(nums: List[int]) -> int:
    # Special number = x where
    # x is the exact total number of elements in nums that are great or equal to x
    nums.sort()
    prev = 0
    for i in range(len(nums)):
        # the only posbility is the remaining
        remaining = len(nums) - i
        if nums[i] >= remaining and prev < remaining:
            return remaining
        prev = nums[i]
    return -1

'''
    Link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x
    Purpose: Find Special number = x where
           : x is the exact total number of elements in nums that are great or equal to x
    parameter: List[int] nums - a list of integers
    return: int - special number x if exist. Otherwise, return -1
    Pre-Condition: 1 <= nums.length <= 100
                 : 0 <= nums[i] <= 1000
    Post-Condition: none
'''
# sort & binary search - runtime: O(nlog(n)), memory: O(n)
def specialArray_M2(nums: List[int]) -> int:
    # Special number = x where
    # x is the exact total number of elements in nums that are great or equal to x
    nums.sort()

    left = 0
    right = len(nums)

    # use the fact that the ans is the index of nums [0, len(nums)]
    # Thus, binary search
    while left <= right:
        middle = left + (right - left) // 2

        # count if the num that is greater than middle appear middle time
        count = 0
        for num in nums:
            if num >= middle:
                count += 1

        if count == middle:
            return count

        if count > middle:
            left = middle + 1
        if count < middle:
            right = middle - 1

    return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(specialArray_M1([0, 6, 6, 3, 7])) # -1
    print(specialArray_M1([3,6,7,7,0])) # -1
    print(specialArray_M1([1])) # 1
    print(specialArray_M1([2])) # 1
    print(specialArray_M1([3,5])) # 2
    print(specialArray_M1([0,0])) # -1
    print(specialArray_M1([0,4,3,0,4])) # 3

    print("\n === solution 2 === \n")
    print(specialArray_M2([0, 6, 6, 3, 7])) # -1
    print(specialArray_M2([3, 6, 7, 7, 0])) # -1
    print(specialArray_M2([1])) # 1
    print(specialArray_M2([2])) # 1
    print(specialArray_M2([3, 5])) # 2
    print(specialArray_M2([0, 0])) # -1
    print(specialArray_M2([0, 4, 3, 0, 4])) # 3

