from typing import List
import random

'''
    Link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
    Purpose: Find the kth largest element in the array
    parameter: List[int] nums - a list of integers
             : int k - an integer
    return: bool - true if ransomNote can be constructed by using the letters from magazine and false otherwise.
    Pre-Condition: 1 <= k <= nums.length <= 10^5
                 : -10^4 <= nums[i] <= 10^4
    Post-Condition: none
'''

# sort: runtime - O(nlog(n)), memory - O(1)
def findKthLargest_m1(nums: List[int], k:int) -> int:
    nums.sort()
    return nums[len(nums) - k]

'''
    Link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
    Purpose: Find the kth largest element in the array
    parameter: List[int] nums - a list of integers
             : int k - an integer
    return: bool - true if ransomNote can be constructed by using the letters from magazine and false otherwise.
    Pre-Condition: 1 <= k <= nums.length <= 10^5
                 : -10^4 <= nums[i] <= 10^4
    Post-Condition: must process in O(n) time complexity
'''
# reverse quick-select: runtime - O(n) -> master theorem, memory - O(log(n)) -> fire stack
def findKthLargest_m2(nums: List[int], k: int) -> int:
    k -= 1
    left = 0
    right = len(nums) - 1

    def quickSelect(nums: List[int], left: int, right: int, k: int):
        pIndex = partition(left, right, nums)
        if k == pIndex:
            return nums[pIndex]
        elif k < pIndex:
            return quickSelect(nums, left, pIndex - 1, k)
        elif k > pIndex:
            return quickSelect(nums, pIndex + 1, right, k)

    def partition(left: int, right: int, nums: List[int]) -> int:
        # randomize quick select
        r = random.randint(left, right)
        swap(nums, left, r)

        pivotIndex = left
        pivot = nums[left]
        left += 1

        while left <= right:
            while left < len(nums) and pivot <= nums[left]:
                left += 1

            while right > 0 and pivot > nums[right]:
                right -= 1

            if left <= right:
                swap(nums,left, right)
        swap(nums, pivotIndex, right)
        return right

    def swap(nums, left, right):
        temp = nums[right]
        nums[right] = nums[left]
        nums[left] = temp

    return quickSelect(nums, left, right, k)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution 1 ===+\n")
    print(findKthLargest_m1([3,2,1,5,6,4], 3)) # 4
    print(findKthLargest_m1([3, 2, 1, 5, 6, 4], 1)) # 6
    print(findKthLargest_m1([3, 2, 1, 5, 6, 4], 5)) # 2
    print(findKthLargest_m1([3, 4], 2)) # 3
    print(findKthLargest_m1([2,3,5,6,4,7,8,9,1,0,1,2,2], 5)) # 5
    print(findKthLargest_m1([2,3,5,6,4,7,8,9,1,0,1,2,2], 1)) # 9
    print(findKthLargest_m1([2,3,5,6,4,7,8,9,1,0,1,2,2], 2)) # 8
    print(findKthLargest_m1([2,3,5,6,4,7,8,9,1,0,1,2,2], 9)) # 2
    print(findKthLargest_m1([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 10)) # 2

    print("\n+=== solution 2 ===+\n")
    print(findKthLargest_m2([3, 2, 1, 5, 6, 4], 3))  # 4
    print(findKthLargest_m2([3, 2, 1, 5, 6, 4], 1))  # 6
    print(findKthLargest_m2([3, 2, 1, 5, 6, 4], 5))  # 2
    print(findKthLargest_m2([3, 4], 2))  # 3
    print(findKthLargest_m2([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 5))  # 5
    print(findKthLargest_m2([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 1))  # 9
    print(findKthLargest_m2([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 2))  # 8
    print(findKthLargest_m2([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 9))  # 2
    print(findKthLargest_m2([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 10))  # 2