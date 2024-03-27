from typing import List

'''
    Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Purpose: Given list[int] which some integer appears once or twice. Find an array of all the integers that appears twice.
    parameter: int nums - a list of integer
    return: int - an array of all the integers that appears twice
    Pre-Condition: n == nums.length
                 : 1 <= n <= 105        
                 : 1 <= nums[i] <= n
                 : Each element in nums appears once or twice.
    Post-Condition: none
'''
# brute force - run time: O(n^2), memory: O(1)
def findAllDuplicates_M1(nums: List[int]) -> List[int]:
    # sort
    nums.sort()

    prev = 0
    j = 0

    # j increases by 1 when we find a duplicate and length decreases by 1 when we find non-duplicate
    # because list.remove() == j++. From for(i = 0; i < len; i++)
    # Thus, j < len(nums) mean the loop reach the end repeat
    while j < len(nums):
        # remove each unique element once
        if nums[j] == prev:
            j += 1
            continue
        else:
            prev = nums[j]
            nums.remove(nums[j])

    return nums


'''
    Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Purpose: Given list[int] which some integer appears once or twice. Find an array of all the integers that appears twice.
    parameter: int nums - a list of integer
    return: int - an array of all the integers that appears twice
    Pre-Condition: n == nums.length
                 : 1 <= n <= 105        
                 : 1 <= nums[i] <= n
                 : Each element in nums appears once or twice.
    Post-Condition: none
'''
# sort - run time: O(nlog(n)), memory: O(1)
def findAllDuplicates_M2(nums: List[int]) -> List[int]:
    # sort
    nums.sort()
    originalLength = len(nums)

    # Find all duplicate and append to the back of the list
    for i in range(originalLength-1):
        if nums[i] == nums[i+1]:
            nums.append(nums[i])

    # return only appendedd duplicate at the back of the list
    return nums[originalLength:]

'''
    Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Purpose: Given list[int] which some integer appears once or twice. Find an array of all the integers that appears twice.
    parameter: int nums - a list of integer
    return: int - an array of all the integers that appears twice
    Pre-Condition: n == nums.length
                 : 1 <= n <= 105        
                 : 1 <= nums[i] <= n
                 : Each element in nums appears once or twice.
    Post-Condition: none
'''
# in-place flag - run time: O(n), memory: O(1) -> answer doesnt count
def findAllDuplicates_M3(nums: List[int]) -> List[int]:
    ans = set()

    for num in nums:
        num = abs(num)
        index = num - 1

        if nums[index] > 0:
            nums[index] *= -1
        else:
            ans.add(num)

    return list(ans)

if __name__ == '__main__':
    print("\n === Method 1 === \n")
    print(findAllDuplicates_M1([10,2,5,10,9,1,1,4,3,7])) # [1, 10]
    print(findAllDuplicates_M1([4,3,2,7,8,2,3,1])) # [2 3]
    print(findAllDuplicates_M1([1,1,2])) # [1]
    print(findAllDuplicates_M1([1, 1]))  # [1]
    print(findAllDuplicates_M1([1])) # []

    print("\n === Method 2 === \n")
    print(findAllDuplicates_M2([10, 2, 5, 10, 9, 1, 1, 4, 3, 7]))  # [1, 10]
    print(findAllDuplicates_M2([4, 3, 2, 7, 8, 2, 3, 1]))  # [2 3]
    print(findAllDuplicates_M2([1, 1, 2]))  # [1]
    print(findAllDuplicates_M2([1, 1]))  # [1]
    print(findAllDuplicates_M2([1]))  # []

    print("\n === Method 3 === \n")
    print(findAllDuplicates_M3([10, 2, 5, 10, 9, 1, 1, 4, 3, 7]))  # [1, 10]
    print(findAllDuplicates_M3([4, 3, 2, 7, 8, 2, 3, 1]))  # [2 3]
    print(findAllDuplicates_M3([1, 1, 2]))  # [1]
    print(findAllDuplicates_M3([1, 1]))  # [1]
    print(findAllDuplicates_M3([1]))  # []


