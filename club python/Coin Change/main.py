# This is a sample Python script.
from functools import cache
from math import inf
from typing import List

'''
    Link: https://leetcode.com/problems/coin-change/
    Purpose: Find the fewest number of coins that you need to make up that amount.
    parameter: List[int] - coins
             : int - amount
    return: ans - the fewest number of coins
    Pre-Condition: 1 <= coins.length <= 12
                 : 1 <= coins[i] <= 231 - 1
                 : 0 <= amount <= 104
    Post-Condition: none
'''
# bruteforce - runtime: O(2^n), memory: O(k) where k = amount
def coinChange_m1(coins: List[int], amount: int) -> int:
    #                                               11
    #                   10                          9                          6
    #          9        8        5    |   8        7        4    |    5        4         1
    #        8 7 4    7 6 3    4 3 1    6 7 3    6 5 2    3 2 -1    4 3 0    3 2 -1   0 -1 -4

    ans = inf
    def dfs(no_of_coin, amount):
        nonlocal ans
        if amount == 0:
            ans = min(no_of_coin, ans)
            return
        if amount < 0:
            return

        for i in range(len(coins)):
            dfs(no_of_coin + 1, amount - coins[i])

    dfs(0, amount)
    return ans if ans != inf else -1

'''
    Link: https://leetcode.com/problems/coin-change/
    Purpose: Find the fewest number of coins that you need to make up that amount.
    parameter: List[int] - coins
             : int - amount
    return: ans - the fewest number of coins
    Pre-Condition: 1 <= coins.length <= 12
                 : 1 <= coins[i] <= 231 - 1
                 : 0 <= amount <= 104
    Post-Condition: none
'''
# cache - runtime: O(n^2), memory: O(k) where k = amount
def coinChange_m2(coins: List[int], amount: int) -> int:
    #                                               11
    #                   10                          9                          6
    #          9        8        5    |   8        7        4    |    5        4         1
    #        8 7 4    7 6 3    4 3 1    6 7 3    6 5 2    3 2 -1    4 3 0    3 2 -1   0 -1 -4
    @cache
    def dfs(remainder):
        if remainder == 0:
            return 0
        if remainder < 0:
            return inf

        no_of_coins = inf
        for i in range(len(coins)):
            no_of_coins = min(no_of_coins, 1 + dfs(remainder - coins[i]))
        return no_of_coins

    ans = dfs(amount)
    return ans if ans != inf else -1

'''
    Link: https://leetcode.com/problems/coin-change/
    Purpose: Find the fewest number of coins that you need to make up that amount.
    parameter: List[int] - coins
             : int - amount
    return: ans - the fewest number of coins
    Pre-Condition: 1 <= coins.length <= 12
                 : 1 <= coins[i] <= 231 - 1
                 : 0 <= amount <= 104
    Post-Condition: none
'''
# manual cache - runtime: O(n^2), memory: O(k) where k = amount
def coinChange_m3(coins: List[int], amount: int) -> int:
    #                                              11
    #                   10                         9                           6
    #          9        8        5    |   8        7        4    |    5        4         1
    #        8 7 4    7 6 3    4 3 1    6 7 3    6 5 2    3 2 -1    4 3 0    3 2 -1   0 -1 -4

    memo = {}

    def dfs(remainder):
        if remainder in memo:
            return memo[remainder]

        if remainder == 0:
            return 0
        if remainder < 0:
            return inf

        no_of_coins = inf
        for i in range(len(coins)):
            no_of_coins = min(no_of_coins, 1 + dfs(remainder - coins[i]))
        memo[remainder] = no_of_coins

        return no_of_coins

    ans = dfs(amount)
    return ans if ans != inf else -1

'''
    Link: https://leetcode.com/problems/coin-change/
    Purpose: Find the fewest number of coins that you need to make up that amount.
    parameter: List[int] - coins
             : int - amount
    return: ans - the fewest number of coins
    Pre-Condition: 1 <= coins.length <= 12
                 : 1 <= coins[i] <= 231 - 1
                 : 0 <= amount <= 104
    Post-Condition: none
'''
# top-down - runtime: O(n^2), memory: O(k) where k = amount
def coinChange_m4(coins: List[int], amount: int) -> int:
    # Formula = the no_of_coin = min(current no_of_coin, Optimal(remainder_no_of_coin) + 1)
    # e.g coin = [1, 2], amount =3
    coins.sort()
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            remainder = i - coin
            if remainder < 0:
                break
            dp[i] = min(dp[i], dp[remainder] + 1)

    return dp[amount] if dp[amount] != inf else -1
        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === bruteforce === \n")
    print(coinChange_m1([1, 2, 5], 11))  # 3
    print(coinChange_m1([2], 3))  # -1
    print(coinChange_m1([1], 0))  # 0
    ''' Too long '''
    # print(coinChange_m1([3, 6, 12, 13], 100))  # 8
    # print(coinChange_m1([474, 83, 404, 3], 264))  # 8

    print("\n === bottom-up dp === \n")
    print(coinChange_m2([1, 2, 5], 11))  # 3
    print(coinChange_m2([2], 3))  # -1
    print(coinChange_m2([1], 0))  # 0
    print(coinChange_m2([3, 6, 12, 13], 100))  # 8
    print(coinChange_m2([474, 83, 404, 3], 264))  # 8

    print("\n === bottom-up dp === \n")
    print(coinChange_m3([1, 2, 5], 11))  # 3
    print(coinChange_m3([2], 3))  # -1
    print(coinChange_m3([1], 0))  # 0
    print(coinChange_m3([3, 6, 12, 13], 100))  # 8
    print(coinChange_m3([474, 83, 404, 3], 264))  # 8

    print("\n === top-down dp === \n")
    print(coinChange_m4([1,2,5], 11)) # 3
    print(coinChange_m4([2], 3)) # -1
    print(coinChange_m4([1], 0)) # 0
    print(coinChange_m4([3, 6, 12, 13], 100)) # 8
    print(coinChange_m4([474,83,404,3], 264)) # 8

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
