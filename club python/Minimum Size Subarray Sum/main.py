from math import inf
from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    right = 0
    minDiff = inf
    totalSum = 0

    while right < len(nums):
        totalSum += nums[right]

        while totalSum >= target:
            minDiff = min(minDiff, right - left + 1)  # update new minDiff where totalSum >= target first
            totalSum -= nums[left]
            left += 1
        right += 1

    return minDiff if minDiff != inf else 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minSubArrayLen(7, [2,3,1,2,4,3])) # 2
    print(minSubArrayLen(5, [2, 3, 1, 2, 4, 3])) # 2
    print(minSubArrayLen(1, [1, 4, 4])) # 1
    print(minSubArrayLen(4, [1, 4, 4])) # 1
    print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
