from typing import List

'''
    Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
    Purpose: Find the maximum number of operations you can perform on the array.
           : In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
    parameter: List[int] nums - an integer
             : int k - an integer 
    return: int counter: the maximum number of operations
    Pre-Condition: 1 <= nums.length <= 10^5
                 : 1 <= nums[i] <= 10^9
                 : 1 <= k <= 109
    Post-Condition: none
'''
# brute force - runtime: O(n^2), memory: O(1)
def maxOperations_M1(nums: List[int], k: int) -> int:
    counter = 0
    for i in range(len(nums)):
        # nums[i] is already used
        if nums[i] == -1:
            continue
        for j in range(i + 1, len(nums)):
            # nums[j] is already used
            if nums[j] == -1:
                continue

            if nums[i] + nums[j] == k:
                counter += 1
                nums[i] = -1
                nums[j] = -1
                break

    return counter

# sort - runtime: O(nlog(n)), memory: O(1)
def maxOperations_M2(nums: List[int], k: int) -> int:
    counter = 0
    nums.sort()

    left = 0
    right = len(nums) - 1

    while (left < right):
        if nums[left] + nums[right] < k:
            left += 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            counter += 1
            left += 1
            right -= 1

    return counter

# hashmap - runtime: O(n), memory: O(n)
def maxOperations_M3(nums: List[int], k: int) -> int:
    # if diff + num = k then
    # {diff, number of diff}
    pair = {}
    counter = 0

    for num in nums:
        diff = k - num

        # increment count if there is a diff in a map
        if num in pair and pair[num] > 0:
            counter += 1
            pair[num] -= 1
            continue

        # add a diff to a map
        if diff in pair:
            pair[diff] += 1
        else:
            pair[diff] = 1

    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+===== solution 1 =====+\n")
    print(maxOperations_M1([3, 1, 3, 4, 3], 6)) #1
    print(maxOperations_M1([1, 2, 3, 4], 5)) #2
    print(maxOperations_M1([3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2], 1)) #0
    print(maxOperations_M1([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3)) #4
    print(maxOperations_M1([1], 1)) #0

    print("\n+===== solution 2 =====+\n")
    print(maxOperations_M2([3, 1, 3, 4, 3], 6)) #1
    print(maxOperations_M2([1, 2, 3, 4], 5)) #2
    print(maxOperations_M2([3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2], 1)) #0
    print(maxOperations_M2([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3)) #4
    print(maxOperations_M2([1], 1)) #0

    print("\n+===== solution 3 =====+\n")
    print(maxOperations_M3([3,1,3,4,3], 6)) #1
    print(maxOperations_M3([1,2,3,4], 5)) #2
    print(maxOperations_M3([3,1,5,1,1,1,1,1,2,2,3,2,2], 1)) #0
    print(maxOperations_M3([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)) #4
    print(maxOperations_M3([1], 1)) #0


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
