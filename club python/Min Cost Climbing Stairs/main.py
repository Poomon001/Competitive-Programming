from typing import List

'''
    Link: https://leetcode.com/problems/min-cost-climbing-stairs/
    Purpose: Find the minimum cost to reach the top of the floor. 
           : Each step on a staircase will cost money. You can either climb one or two steps once paying the cost.
    parameter: int[] cost - an array of integers where cost[i] is the cost of i th step on a staircase.
    return: int currMaxMoney - the minimum cost to reach the top of the floor.
    Pre-Condition: 2 <= cost.length <= 1000
                 : 0 <= cost[i] <= 999
    Post-Condition: none
'''
# recursion: runtime - O(2^n), memory - O(height)
def minCostClimbingStairs_M1(cost: List[int]) -> int:
    def recursive(n):
        x = 0
        y = 0
        # base case
        if n < 1:
            return 0

        if n - 1 >= 0:
            x = cost[n - 1]

        if n - 2 >= 0:
            y = cost[n - 2]
        return min(recursive(n - 1) + x, recursive(n - 2) + y) # add current cost and recursive call

    return recursive(len(cost))

'''
    Link: https://leetcode.com/problems/min-cost-climbing-stairs/
    Purpose: Find the minimum cost to reach the top of the floor. 
           : Each step on a staircase will cost money. You can either climb one or two steps once paying the cost.
    parameter: int[] cost - an array of integers where cost[i] is the cost of i th step on a staircase.
    return: int currMaxMoney - the minimum cost to reach the top of the floor.
    Pre-Condition: 2 <= cost.length <= 1000
                 : 0 <= cost[i] <= 999
    Post-Condition: none
'''
# dynamic programming: runtime - O(n), memory - O(n)
def minCostClimbingStairs_M2(cost: List[int]) -> int:
    # base case: first 2 stairs are free
    # {index, min cost}
    memory = {0: 0, 1: 0}

    def dp(n):
        # use exist memory and memorize new memory
        if n in memory:
            return memory[n]
        else:
            if n - 1 in memory and n - 2 in memory:
                memory[n] = min(memory[n - 1] + cost[n - 1], memory[n - 2] + cost[n - 2]) # add current cost and recursive call
                return memory[n]
        return min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2]) # add current cost and recursive call

    return dp(len(cost))

'''
    Link: https://leetcode.com/problems/min-cost-climbing-stairs/
    Purpose: Find the minimum cost to reach the top of the floor. 
           : Each step on a staircase will cost money. You can either climb one or two steps once paying the cost.
    parameter: int[] cost - an array of integers where cost[i] is the cost of i th step on a staircase.
    return: int currMaxMoney - the minimum cost to reach the top of the floor.
    Pre-Condition: 2 <= cost.length <= 1000
                 : 0 <= cost[i] <= 999
    Post-Condition: none
'''
# dynamic programming: runtime - O(n), memory - O(n)
def minCostClimbingStairs_M3(cost: List[int]) -> int:
    last = len(cost) - 1

    if last == 1:
        return min(cost[0], cost[1])

    if last == 0:
        return cost[0]

    # keep track of the minimum cost from the beginning to each currect step
    stepToMinCost = {0: cost[0], 1: cost[1]}

    for i in range(2, len(cost)):
        stepToMinCost[i] = min(stepToMinCost[i - 1], stepToMinCost[i - 2]) + cost[i]

    return min(stepToMinCost[last - 1], stepToMinCost[last])

'''
    Link: https://leetcode.com/problems/min-cost-climbing-stairs/
    Purpose: Find the minimum cost to reach the top of the floor. 
           : Each step on a staircase will cost money. You can either climb one or two steps once paying the cost.
    parameter: int[] cost - an array of integers where cost[i] is the cost of i th step on a staircase.
    return: int currMaxMoney - the minimum cost to reach the top of the floor.
    Pre-Condition: 2 <= cost.length <= 1000
                 : 0 <= cost[i] <= 999
    Post-Condition: none
'''
# dynamic programming: runtime - O(n), memory - O(1)
def minCostClimbingStairs_M4(cost: List[int]) -> int:
    cost.append(0)
    prevMinCost = 0
    currMinCost = 0

    for c in cost:
        temp = currMinCost
        currMinCost = c + min(prevMinCost, currMinCost)
        prevMinCost = temp

    return currMinCost


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution1 ===+\n")
    print(minCostClimbingStairs_M1([10, 15, 20]))  # 15
    print(minCostClimbingStairs_M1([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
    print(minCostClimbingStairs_M1([1, 100, 1, 1, 2, 1, 1, 1, 100, 1]))  # 6
    print(minCostClimbingStairs_M1([10]))  # 0
    print(minCostClimbingStairs_M1([10, 15]))  # 10
    # will take a few second
    print(minCostClimbingStairs_M1([841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,953,38,195,679,65,707,196,705,569,275,259,872,630,965,978,109,56])) # 7072

    print("\n+=== solution2 ===+\n")
    print(minCostClimbingStairs_M2([10,15,20])) # 15
    print(minCostClimbingStairs_M2([1,100,1,1,1,100,1,1,100,1])) # 6
    print(minCostClimbingStairs_M2([1,100,1,1,2,1,1,1,100,1])) # 6
    print(minCostClimbingStairs_M2([10])) # 0
    print(minCostClimbingStairs_M2([10, 15])) # 10
    print(minCostClimbingStairs_M2([841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,953,38,195,679,65,707,196,705,569,275,259,872,630,965,978,109,56])) # 7072

    print("\n+=== solution3 ===+\n")
    print(minCostClimbingStairs_M3([10,15,20])) # 15
    print(minCostClimbingStairs_M3([1,100,1,1,1,100,1,1,100,1])) # 6
    print(minCostClimbingStairs_M3([1,100,1,1,2,1,1,1,100,1])) # 6
    print(minCostClimbingStairs_M3([10])) # 0
    print(minCostClimbingStairs_M3([10, 15])) # 10
    print(minCostClimbingStairs_M3([841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,953,38,195,679,65,707,196,705,569,275,259,872,630,965,978,109,56])) # 7072

    print("\n+=== solution4 ===+\n")
    print(minCostClimbingStairs_M4([10,15,20])) # 15
    print(minCostClimbingStairs_M4([1,100,1,1,1,100,1,1,100,1])) # 6
    print(minCostClimbingStairs_M4([1,100,1,1,2,1,1,1,100,1])) # 6
    print(minCostClimbingStairs_M4([10])) # 0
    print(minCostClimbingStairs_M4([10, 15])) # 10
    print(minCostClimbingStairs_M4([841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,953,38,195,679,65,707,196,705,569,275,259,872,630,965,978,109,56])) # 7072
