'''
    Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
    Purpose: Given two integers left and right, find the total numbers in the numbers [left, right]
           : having a prime number of 1's bits in their binary representation.
    parameter: int left - the first number in the range
            :  int right - the last number in the range
    return: int ans - the total numbers, having a prime number of 1's bits in their binary representation.
    Pre-Condition: 1 <= left <= right <= 10^6
                 : 0 <= right - left <= 10^4
    Post-Condition: none
'''
# bitshift - runtime: O(n * k), space: O(k) where n = number of all bit and k = max(prime number)
def countPrimeSetBits(left: int, right: int) -> int:
    ans = 0
    for num in range(left, right + 1):
        count_ones = 0
        while num > 0:
            mask = num & 1
            if mask == 1:
                count_ones += 1
            num = num >> 1
        if _is_prime(count_ones):
            ans += 1
    return ans

def _is_prime(num: int):
    if num < 2:
        return False

    sqr_root = int(num ** 0.5)
    nums = [n for n in range(2, 1 + sqr_root)]
    # small_nums = [2, 3, 5, 7, 11, 13, 17, 19] # can handle upto 19 bits of 1's (large enough)
    for divider in nums:
        if num % divider == 0:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    6  -> 110 (2 set bits, 2 is prime)
    7  -> 111 (3 set bits, 3 is prime)
    8  -> 1000 (1 set bit, 1 is not prime)
    9  -> 1001 (2 set bits, 2 is prime)
    10 -> 1010 (2 set bits, 2 is prime)
    4 numbers have a prime number of set bits.
    '''
    print(countPrimeSetBits(6, 10)) # 4

    '''
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)
    5 numbers have a prime number of set bits.
    '''
    print(countPrimeSetBits(10, 15)) # 5

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
