import math
from typing import List

'''
    Link: https://leetcode.com/problems/product-of-array-except-self
    Purpose: Given nums array, find the product of all the elements of nums except nums[i].
    parameter: List[int] nums - a list of numbers
    return: List[int] answer - num array where answer[i] is equal to the product of all the elements of nums except nums[i].
    Pre-Condition: 2 <= nums.length <= 105
                 : -30 <= nums[i] <= 30
                 : The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer
    Post-Condition: none
'''
# Division - runtime: O(n), memory: O(1)
def productExceptSelf_M1(nums: List[int]) -> List[int]:
    multi = math.prod(nums)
    answer = []

    for i in range(len(nums)):
        if nums[i] != 0:
            answer.append(multi // nums[i])
        else:
            zero = math.prod(nums[:i]) * math.prod(nums[i + 1:])
            answer.append(zero)

    return answer

'''
    Link: https://leetcode.com/problems/product-of-array-except-self
    Purpose: Given nums array, find the product of all the elements of nums except nums[i].
    parameter: List[int] nums - a list of numbers
    return: List[int] answer - num array where answer[i] is equal to the product of all the elements of nums except nums[i].
    Pre-Condition: 2 <= nums.length <= 105
                 : -30 <= nums[i] <= 30
                 : The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer
    Post-Condition: none
'''
# prefix * suffix - runtime: O(n), memory: O(n)
def productExceptSelf_M2(nums: List[int]) -> List[int]:
    # prefix[i] = product from [0 to i - 1]
    # suffix[i] = product from [i - 1 to 0]
    # Thus, prefix[i] * suffix[i] = product of all, excluding the integer at i-th
    # [1, 2, 3, 4] = [1,           1*1,   1*1*2,   1*1*2*3]
    # [1, 2, 3, 4] = [2*3*4*1,   3*4*1,     4*1,         1]

    prefix = [1] * len(nums)
    suffix = [1] * len(nums)
    for n in range(len(nums) - 1):
        i = n + 1
        j = len(nums) - n - 2
        prefix[i] = prefix[i - 1] * nums[n]
        suffix[j] = suffix[j + 1] * nums[len(nums) - n - 1]

    return [x * y for x, y in zip(prefix, suffix)]

if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(productExceptSelf_M1([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
    print(productExceptSelf_M1([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(productExceptSelf_M1([2, 3, 1, 4]))  # [12, 8, 24, 6]
    print(productExceptSelf_M1([0, -12, 0]))  # [0, 0, 0]
    print(productExceptSelf_M1([-10, -12, 10, -1]))  # [120, 100, -120, 1200]

    print("\n === Solution 2 === \n")
    print(productExceptSelf_M2([-1,1,0,-3,3])) # [0, 0, 9, 0, 0]
    print(productExceptSelf_M2([1, 2, 3, 4])) # [24, 12, 8, 6]
    print(productExceptSelf_M2([2, 3, 1, 4])) # [12, 8, 24, 6]
    print(productExceptSelf_M2([0, -12, 0])) # [0, 0, 0]
    print(productExceptSelf_M2([-10, -12, 10, -1])) # [120, 100, -120, 1200]

