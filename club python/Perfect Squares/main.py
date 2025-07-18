from math import inf, sqrt

'''
    Link: https://leetcode.com/problems/perfect-squares
    Purpose: Given an integer n, find the least number of perfect square numbers that sum to n
    Parameter: int n - an integer
    return: int - the least number of perfect square numbers that sum to n
    Pre-Condition: 1 <= n <= 104
    Post-Condition: None
'''
# backtracking - runtime(k ^ n), memory: O(k ^ n)
def numSquares_M1(n: int) -> int:
    sqrtr = int(sqrt(n))
    candidates = [num * num for num in range(1, sqrtr + 1)]
    minTotal = inf
    '''
                                        []
                    [1]                                         []
        [1, 1]                  [1,4]                       [4]     []
[1, 1, 1] [1, 1, 4]     [1, 4, 1]  [1, 4, 4]
    '''

    def backtrack(combination, n, remaining):
        nonlocal minTotal
        # base case
        if remaining == 0:
            minTotal = min(minTotal, len(combination))
            return
        elif remaining < 0:
            return

        for i in range(n, len(candidates)):
            combination.append(candidates[i])
            backtrack(combination, i, remaining - candidates[i])
            combination.pop()

    backtrack([], 0, n)
    return minTotal

'''
    Link: https://leetcode.com/problems/perfect-squares
    Purpose: Given an integer n, find the least number of perfect square numbers that sum to n
    Parameter: int n - an integer
    return: int - the least number of perfect square numbers that sum to n
    Pre-Condition: 1 <= n <= 104
    Post-Condition: None
'''
# dp - runtime(n * sqrt(n)), memory: O(n)
def numSquares_M2(n: int) -> int:
    # minSqrtCount[target] = min(minSqrtCount[n], 1 + minSqrtCount[target - square]);
    # target - square is the remaining after subtracting square =>
    # optimal solution of target - square is minSqrtCount[target - square]
    # dp[1] = min(inf, dp[0] + 1) = 1
    # dp[2] = min(inf, dp[1] + 1) = 2
    # dp[3] = min(inf, dp[2] + 1) = 3
    # dp[4] = min(inf, dp[4 - 1] + 1) = 4; min(inf, dp[4 - 4] + 1) = 1
    # dp[12] = min(inf, dp[12 - 1] + 1) = 4; min(4, dp[12 - 4] + 1) = 3; min(3, dp[12 - 9] + 1)
    # dp[14] = min(inf, dp[14 - 1] + 1), min(3, dp[14 - 4] + 1), min(3, dp[14 - 9] + 1)

    dp = [inf] * (n + 1)
    dp[0] = 0

    for target in range(1, n + 1):
        for num in range(1, target + 1):
            # try all possible squares (num * num) up to target: 1, 4, 9, 16, ...
            square = num * num
            if target - square < 0:
                break
            dp[target] = min(dp[target], dp[target - square] + 1)  # +1 mean (we add curr_square to target - curr_square)

    return dp[n]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(numSquares_M1(1)) # 1
    print(numSquares_M1(2)) # 2
    print(numSquares_M1(4)) # 1
    print(numSquares_M1(12)) # 3
    print(numSquares_M1(14)) # 3
    print(numSquares_M1(170)) # 2
    print(numSquares_M1(234)) # 2 -> take 30 sed

    print("\n === Solution 2 === \n")
    print(numSquares_M2(1))  # 1
    print(numSquares_M2(2))  # 2
    print(numSquares_M2(4))  # 1
    print(numSquares_M2(12))  # 3
    print(numSquares_M2(14))  # 3
    print(numSquares_M2(170))  # 2
    print(numSquares_M2(234))  # 2

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
