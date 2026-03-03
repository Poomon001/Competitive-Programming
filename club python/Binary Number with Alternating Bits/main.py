'''
    Link: https://leetcode.com/problems/binary-number-with-alternating-bits
    Purpose: Find if the number has alternating bits
    parameter: int n - a positive number
    return: bool - True if the number has alternating bits. Otherwise, False
    Pre-Condition: 1 <= n <= 2^31 - 1
    Post-Condition: none
'''
# bit manipulation: runtime - O(n), space: O(1)
def hasAlternatingBits(n: int) -> bool:
    mask = 1  # 0000 0001
    temp = mask & n
    n = n >> 1
    while n > 0:
        last = mask & n
        if last == temp:
            return False
        temp = last
        n = n >> 1
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(hasAlternatingBits(1)) # True
    print(hasAlternatingBits(5)) # True
    print(hasAlternatingBits(7)) # False
    print(hasAlternatingBits(11)) # False
    print(hasAlternatingBits(1000)) # False
