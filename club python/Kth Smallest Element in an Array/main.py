from typing import List
from heapq import heappush, heappop


'''
    Link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
    Purpose: Find the kth smallest element in the array
    parameter: List[int] nums - a list of integers
             : int k - an integer
    return: bool - int - a Kth smallest number
    Pre-Condition: 1 <= k <= nums.length <= 10^5
                 : -10^4 <= nums[i] <= 10^4
    Post-Condition: must process in O(n) time complexity
'''
# min heap - runtime: O(nlog(k)), memory: O(n)
def findKthSmallest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        if len(heap) < k:
            heappush(heap, -num)
        else:
            curr = -heappop(heap)
            heappush(heap, -min(num, curr))
    return -heappop(heap)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findKthSmallest([3, 2, 1, 5, 6, 4], 3))  # 3
    print(findKthSmallest([3, 2, 1, 5, 6, 4], 1))  # 1
    print(findKthSmallest([3, 2, 1, 5, 6, 4], 5))  # 5
    print(findKthSmallest([3, 4], 2))  # 4
    print(findKthSmallest([3, 4, -1, -3], 2))  # -1
    print(findKthSmallest([3, 4, -1, -3], 4))  # 4
    print(findKthSmallest([3, -4, 0, 3, 4], 2))  # 0
    print(findKthSmallest([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 5))  # 2
    print(findKthSmallest([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 1))  # 0
    print(findKthSmallest([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 2))  # 1
    print(findKthSmallest([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 9))  # 5
    print(findKthSmallest([2, 3, 5, 6, 4, 7, 8, 9, 1, 0, 1, 2, 2], 10))  # 6
