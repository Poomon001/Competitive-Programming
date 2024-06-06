'''
    Purpose: Find total number of bits from an integer
    parameter: int n - an integer
    return: int ans - a number of total bits
    Pre-Condition: 0 <= n <= 10^5
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def countTotaBits(n):
    if n == 0:
        return 1

    ans = 0
    while(n != 0):
        ans += 1
        n = n >> 1
    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(countTotaBits(0)) # 1
    print(countTotaBits(1))  # 1
    print(countTotaBits(2))  # 2
    print(countTotaBits(4))  # 3
    print(countTotaBits(9))  # 4
    print(countTotaBits(32))  # 6
    print(countTotaBits(12345)) # 14

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
