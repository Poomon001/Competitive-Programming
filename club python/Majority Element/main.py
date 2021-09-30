from typing import List

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
    dic = {}
    ans = 0
    key = 0
    # count each num
    for num in nums:
        if num in dic.keys():
            dic[num] += 1
        else:
            dic[num] = 1

    # find the key with the highest counter
    for k in dic.keys():
        if dic.get(k) > ans:
            key = k
            ans = dic.get(k)

    return key

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
# sort: runtime O(n) and mem O(1)
def majorityElement_M2(nums: List[int]) -> int:
    nums.sort()
    globalMax = 0
    counter = 1
    ans = 0
    i = 0

    for i in range(len(nums) - 1):
        # compare the curr with the next ele
        if nums[i] == nums[i + 1]:
            # count one if they are in the same
            counter += 1
        elif counter > globalMax:
            # get max and reset counter to 0 if they are not the same
            ans = nums[i]
            globalMax = max(counter, globalMax)
            counter = 1

    # we need to check the case i+1 where i is the final index
    if counter > globalMax:
        ans = nums[i]

    return ans


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
