from typing import List

'''
    Link: https://leetcode.com/problems/count-partitions-with-even-sum-difference
    Purpose: Find the number of partitions where the difference between the sum of the left and right subarrays is even.
           : Left = [0, i] and right = [i+1, n-1]
    parameter: List[int] tasks - a list of tasks
             : int space - a day need to wait before process the same task 
    return: int day - the minimum number of days needed to complete all tasks
    Pre-Condition: 1 <= tasks.length <= 10^5
                 : 1 <= tasks[i] <= 10^9
                 : 1 <= space <= tasks.length
    Post-Condition: none
'''
# prefix sum: runtime: O(n), memnory: O(1)
def countPartitions(nums: List[int]) -> int:
    left = 0
    right = sum(nums)
    even_count = 0

    for i in range(len(nums) - 1):
        left += nums[i]
        right -= nums[i]

        if (left - right) % 2 == 0:
            even_count += 1

    return even_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(countPartitions([10,10,3,7,6])) # 4
    print(countPartitions([1, 2, 2])) # 0
    print(countPartitions([2,4,6,8])) # 3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
