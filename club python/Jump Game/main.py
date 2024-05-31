from typing import List

'''
    Link: https://leetcode.com/problems/jump-game/
    Purpose: Find if you can reach the last index of the array where each element in the array represents 
            your maximum jump length at that position.
    parameter: List[int] - nums: a list of number that represents your maximum jump length at that position.
    return: bool - Return true if you can reach the last index, or false otherwise.
    Pre-Condition: 1 <= nums.length <= 104
                 : 0 <= nums[i] <= 105
    Post-Condition: none
'''

# greedy: runtime O(n), memory O(1)
def jumpGame(nums: List[int]) -> bool:
    greedyFuel = 0
    for num in nums:
        if greedyFuel < 0:
            return False
        else:
            # greedy pick: current fuel or the new fuel
            greedyFuel = max(greedyFuel, num)

        greedyFuel -= 1

    return True



if __name__ == '__main__':
    print(jumpGame([2, 3, 1, 1, 4])) # true
    print(jumpGame([3, 2, 1, 0, 4])) # false
    print(jumpGame([1, 3, 1, 0, 0, 1])) # false
    print(jumpGame([1, 1, 2, 5, 2, 1, 0, 0, 1, 3])) # true
    print(jumpGame([2, 0, 0])) # true
    print(jumpGame([0])) # true
