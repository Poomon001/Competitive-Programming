from typing import List

'''
    Link: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
    Purpose: Determine the minimum cost to move all coins to the same position
           : Cost rate:
                : position[i] + 2 or position[i] - 2 with cost = 0.
                : position[i] + 1 or position[i] - 1 with cost = 1.
    parameter: List[int] - a list of positions containing a coin
    return: int - minimum cost to move all coin in one position
    Pre-Condition: The number of nodes in the tree is in the range [0, 5000].
                 : 1 <= position.length <= 100
                 : 1 <= position[i] <= 10^9
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def minCostToMoveChips(position: List[int]) -> int:
    # cost
    evenCost = 0
    oddCost = 0

    # if moving by 2 position is free then
    # 1. moving from odd to odd position is free
    # 2. moving from even to even postion is free
    # 3. moving from odd/even to even/odd position is not free
    for p in position:
        if p % 2 == 0:
            # find cost from moving even coin to odd position
            evenCost += 1
        else:
            # find cost from moving odd coin to even position
            oddCost += 1

    return min(evenCost, oddCost)


if __name__ == '__main__':
    print(minCostToMoveChips([1,2,3])) # 1
    print(minCostToMoveChips([2,2,2,3,3])) # 2
    print(minCostToMoveChips([1,1000000000])) # 1
    print(minCostToMoveChips([1, 3, 5, 7, 9, 11, 21, 23, 51])) # 0
    print(minCostToMoveChips([2, 4, 6, 8, 10 ,12, 22, 24, 50])) # 0
    print(minCostToMoveChips([1])) # 0

