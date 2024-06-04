'''
    Link: https://leetcode.com/problems/fibonacci-number/
    Purpose: Determine fibonacci of n
    parameter: int n - an integer
             : int = a fibonacci of n
    return: List[List[int]] - all subsets in nums
    Pre-Condition: 0 <= n <= 30
    Post-Condition: none
'''

# recursive - runtime: O(2^n), memory: O(log(n))
def fib_M1(n: int) -> int:
    def fibSum(n: int) -> int:
        # base case
        if n == 0:
            return 0

        if n == 1:
            return 1

        return fibSum(n - 1) + fibSum(n - 2)

    return fibSum(n)

# Dynamic programming while loop - runtime: O(n), memory: O(1)
def fib_M2(n: int) -> int:
    fibSum1 = 0
    fibSum2 = 1
    ans = 0

    while n != 0:
        n -= 1
        ans = fibSum1 + fibSum2
        fibSum2 = fibSum1
        fibSum1 = ans

    return ans

# Dynamic programming with table - runtime: O(n), memory: O(n)
def fib_M3(n: int) -> int:
    # {n:result}
    table = {0: 0, 1: 1}

    def fibSum(n: int) -> int:
        # found data in a table, just use it
        if n in table:
            return table[n]

        # new data can be find by the table using previous data
        if n - 1 == len(table) - 1 and n not in table:
            table[n] = table[n - 1] + table[n - 2]
            return table[n]

        return fibSum(n - 1) + fibSum(n - 2)

    return fibSum(n)

# Dynamic programming with table - runtime: O(n), memory: O(n)
def fib_M4(n: int) -> int:
    dic = {0: 0, 1: 1}

    def fibSum(n):
        if n == 0 or n == 1:
            return dic[n]

        if n - 1 in dic and n - 2 in dic:
            return dic[n - 1] + dic[n - 2]
        else:
            ans = fibSum(n - 1) + fibSum(n - 2)
            dic[n] = ans
            return ans

    return fibSum(n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("+=== Solution 1 ===+")
    print(fib_M1(1))
    print(fib_M1(2))
    print(fib_M1(3))
    print(fib_M1(4))
    print(fib_M1(5))
    print(fib_M1(6))

    print("+=== Solution 2 ===+")
    print(fib_M2(1))
    print(fib_M2(2))
    print(fib_M2(3))
    print(fib_M2(4))
    print(fib_M2(5))
    print(fib_M2(6))

    print("+=== Solution 3 ===+")
    print(fib_M3(1))
    print(fib_M3(2))
    print(fib_M3(3))
    print(fib_M3(4))
    print(fib_M3(5))
    print(fib_M3(6))

    print("+=== Solution 4 ===+")
    print(fib_M4(1))
    print(fib_M4(2))
    print(fib_M4(3))
    print(fib_M4(4))
    print(fib_M4(5))
    print(fib_M4(6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
