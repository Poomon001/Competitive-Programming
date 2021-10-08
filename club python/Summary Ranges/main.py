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
        # continuous: append to the same block
        if prev+1 == nums[i]:
            numList[index].append(nums[i])
        # not continuous: append to the next block
        else:
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
    # returned answer doesnt count as a memory usage
    s = []

    # handle empty case:
    if len(nums) == 0:
        return s

    # element in each range
    length = 0

    # save the first number of the range
    head = nums[0]

    # save previous number
    prev = nums[0]

    # group element into multiple ranges
    for i in range(1, len(nums)):
        # continuous: append to the same block
        if prev+1 == nums[i]:
            length += 1

        # not continuous: append to the next block
        else:
            ans = f"{head}->{nums[i-1]}" if length != 0 else f"{head}"
            s.append(ans)
            head = nums[i]
            length = 0

        prev = nums[i]

    # append the last range (loop will not cover the last range)
    ans = f"{head}->{nums[i]}" if length != 0 else f"{head}"
    s.append(ans)

    return s


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

