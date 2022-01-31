from typing import List

'''
    Link: https://leetcode.com/problems/richest-customer-wealth/
    Purpose: Find wealth (money) of the richest customer
    parameter: List[List[int]] accounts - accounts[i][j] is the amount of money the ith customer has in the jth bank
    return: int maxSum - the wealth (money) of the richest customer
    Pre-Condition: m == accounts.length
                 : n == accounts[i].length
                 : 1 <= m, n <= 50
                 : 1 <= accounts[i][j] <= 100
    Post-Condition: none
'''
def maximumWealth(accounts: List[List[int]]) -> int:
    maxSum = 0
    for account in accounts:
        currSum = 0
        for money in account:
            currSum += money
        maxSum = max(maxSum, currSum)
    return maxSum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maximumWealth([[1,2,3],[3,2,1]])) # 6
    print(maximumWealth([[1,5],[7,3],[3,5]])) # 10
    print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]])) # 17
    print(maximumWealth([[2, 1, 1]])) # 4
    print(maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5],[1,5],[7,3],[3,5]])) # 17


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
