from typing import List

'''
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Purpose: Find the max profit by choosing a single day to buy one stock and 
           : choosing a different day in the future to sell that stock.
    parameter: List[int] prices - a list of integer where each number represents a price, and its index represent a day.
    return: int maxProfit - the max profit
    Pre-Condition: 1 <= nums.length <= 10^5
                 : -2^31 <= nums[i] <= 2^31 - 1
                 : 0 <= k <= 10^5
    Post-Condition: none
'''
# brute force: runtime: O(n^2), memory: O(1)
def maxProfit_M1(prices: List[int]) -> int:
    maxProfit = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            profit = sell - buy
            maxProfit = max(maxProfit, profit)

    return maxProfit

'''
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Purpose: Find the max profit by choosing a single day to buy one stock and 
           : choosing a different day in the future to sell that stock.
    parameter: List[int] prices - a list of integer where each number represents a price, and its index represent a day.
    return: int maxProfit - the max profit
    Pre-Condition: 1 <= nums.length <= 10^5
                 : -2^31 <= nums[i] <= 2^31 - 1
                 : 0 <= k <= 10^5
    Post-Condition: none
'''
# Greedy: buy low, sell high: O(n), memory:O(1)
def maxProfit_M2(prices: List[int]) -> int:
    profit = 0
    bought = prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        if profit < price - bought:
            profit = price - bought
        else:
            bought = min(bought, price)

    return profit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution 1 ===+\n")
    print(maxProfit_M1([7, 1, 5, 3, 6, 4]))  # 5
    print(maxProfit_M1([7, 1, 5, 3, 0, 6, 4]))  # 6
    print(maxProfit_M1([7]))  # 0
    print(maxProfit_M1([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))  # 9
    print(maxProfit_M1([1, 2, 4]))  # 3
    print(maxProfit_M1([7, 6, 4, 3, 1]))  # 0

    print("\n+=== solution 2 ===+\n")
    print(maxProfit_M2([7,1,5,3,6,4])) # 5
    print(maxProfit_M2([7,1,5,3,0,6,4])) # 6
    print(maxProfit_M2([7])) # 0
    print(maxProfit_M2([1,2,4,2,5,7,2,4,9,0,9])) # 9
    print(maxProfit_M2([1,2,4])) # 3
    print(maxProfit_M2([7,6,4,3,1]))  # 0
