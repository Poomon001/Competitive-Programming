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
    # using this fact: answer[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])
    # prefix = [1,  1,  2, 6]
    # suffix = [24, 12, 4, 1]
    # answer = [24, 12, 8, 6]
    length = len(nums)
    prefix = [0] * length
    suffix = [0] * length
    l_product = 1
    r_product = 1

    for i in range(length):
        j = -i - 1  # e.g i = 0, j = -1 ... i = 1, j = -2
        prefix[i] = l_product
        suffix[j] = r_product

        l_product *= nums[i]
        r_product *= nums[j]

    answer = []
    for pre, suf in zip(prefix, suffix):
        answer.append(pre * suf)

    return answer

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

