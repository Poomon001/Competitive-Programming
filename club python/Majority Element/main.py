import math
from typing import List
from collections import Counter
'''
    Link: https://leetcode.com/problems/majority-element/
    Purpose: Find the majority element
    parameter: List[int] nums - an integer
    return: int ans: the majority element
    Pre-Condition: n == nums.length
                 : 1 <= n <= 5 * 104
                 : -231 <= nums[i] <= 231 - 1
    Post-Condition: none
'''

# hash map: runtime O(n) and mem O(n)
def majorityElement_M1(nums: List[int]) -> int:
    # {number, counter}
    dic = Counter(nums)
    halfSize = math.ceil(len(nums) / 2)

    for key, value in dic.items():
        if value >= halfSize:
            return key

    return nums[0]

'''
    Link: https://leetcode.com/problems/majority-element/
    Purpose: Find the majority element
    parameter: List[int] nums - an integer
    return: int ans: the majority element
    Pre-Condition: n == nums.length
                 : 1 <= n <= 5 * 104
                 : -231 <= nums[i] <= 231 - 1
    Post-Condition: none
'''
# sort: runtime O(nlog(n)) and mem O(1)
def majorityElement_M2(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]

# moore's voting algo: runtime: O(n), memory: O(1)
def majorityElement_M3(nums:List[int]):
    count = 1
    candidate = nums[0]

    for i in range(1, len(nums)):
        # select a new candidate
        if count == 0:
            candidate = nums[i]

        if nums[i] == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == '__main__':
    print("\n === M1 ===\n")
    print(majorityElement_M1([2, 2, 1, 1, 1, 2, 2]))  # 2
    print(majorityElement_M1([3, 2, 3]))  # 3
    print(majorityElement_M1([1]))  # 3
    print(majorityElement_M1([6, 6, 6, 7, 7]))  # 6
    print("\n === M2 ===\n")
    print(majorityElement_M2([2,2,1,1,1,2,2])) # 2
    print(majorityElement_M2([3,2,3]))  # 3
    print(majorityElement_M2([1]))  # 3
    print(majorityElement_M2([6,6,6,7,7]))  # 6
    print("\n === M3 ===\n")
    print(majorityElement_M2([2, 2, 1, 1, 1, 2, 2]))  # 2
    print(majorityElement_M2([3, 2, 3]))  # 3
    print(majorityElement_M2([1]))  # 3
    print(majorityElement_M2([6, 6, 6, 7, 7]))  # 6
