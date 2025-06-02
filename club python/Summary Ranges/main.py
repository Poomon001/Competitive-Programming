from typing import List

'''
    Link: https://leetcode.com/problems/summary-ranges/
    Purpose:  find the smallest sorted list of ranges that cover all the numbers in the array exactly. 
    parameter: List[int] nums - a list of numbers
    return: List[int] s - the smallest sorted list of ranges that cover all the numbers
    Pre-Condition: 0 <= nums.length <= 20
                 : -231 <= nums[i] <= 231 - 1
                 : All the values of nums are unique.
                 : nums is sorted in ascending order.
    Post-Condition: none
'''
# runtime: O(n) memory: O(n)
def summaryRanges_M1(nums: List[int]) -> List[str]:
    numList = [[] for i in range(len(nums))]
    s = []

    # keep track of number of ranges
    index = 0

    # handle empty case:
    if len(nums) == 0:
        return []

    # append the first element to the list
    prev = nums[0]
    numList[index].append(prev)

    # group element into multiple ranges
    for i in range(1, len(nums)):
        if prev+1 == nums[i]:
            # continuous: append to the same block
            numList[index].append(nums[i])
        else:
            # not continuous: append to the next block
            index += 1
            numList[index].append(nums[i])
        prev = nums[i]

    # format answer
    for ele in numList:
        # format 1: only 1 element
        if len(ele) == 1:
            s.append(f"{ele[0]}")
        # format 2: more than 1 element
        elif len(ele) > 1:
            s.append(f"{ele[0]}->{ele[len(ele)-1]}")

    return s

'''
    Link: https://leetcode.com/problems/summary-ranges/
    Purpose:  find the smallest sorted list of ranges that cover all the numbers in the array exactly. 
    parameter: List[int] nums - a list of numbers
    return: List[int] s - the smallest sorted list of ranges that cover all the numbers
    Pre-Condition: 0 <= nums.length <= 20
                 : -231 <= nums[i] <= 231 - 1
                 : All the values of nums are unique.
                 : nums is sorted in ascending order.
    Post-Condition: none
'''
# runtime: O(n) memory: O(1)
def summaryRanges_M2(nums: List[int]) -> List[str]:
    ans = []
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [f"{nums[0]}"]

    start = nums[0]
    for i in range(1, len(nums)):
        curr = nums[i]
        prev = nums[i - 1]
        if curr - prev != 1:
            if start == prev:
                # no range
                ans.append(f"{start}")
            else:
                # there is a range
                ans.append(f"{start}->{prev}")
            start = nums[i]

    if start == nums[-1]:
        ans.append(f"{start}")
    else:
        ans.append(f"{start}->{nums[-1]}")

    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(" \n method 1 ==\n")
    print(summaryRanges_M1([0,1,2,4,5,7])) # ['0->2', '4->5', '7']
    print(summaryRanges_M1([0,2,3,4,6,8,9])) # ['0', '2->4', '6', '8->9']
    print(summaryRanges_M1([])) # []
    print(summaryRanges_M1([0])) # ['0']
    print(summaryRanges_M1([-1])) # ['-1']

    print(" \n method 2 ==\n")
    print(summaryRanges_M2([0, 1, 2, 4, 5, 7])) # ['0->2', '4->5', '7']
    print(summaryRanges_M2([0, 2, 3, 4, 6, 8, 9])) # ['0', '2->4', '6', '8->9']
    print(summaryRanges_M2([])) # []
    print(summaryRanges_M2([0])) # ['0']
    print(summaryRanges_M2([-1])) # ['-1']

