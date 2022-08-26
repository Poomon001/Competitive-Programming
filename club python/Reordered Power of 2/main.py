from collections import Counter

'''
    Link: https://leetcode.com/problems/reordered-power-of-2/
    Purpose: Find if we can reorder digits in n such that the result is a power of two.
    parameter: int n - an integer
    return: bool - True if the result is a power of two. Otherwise False
    Pre-Condition: 1 <= n <= 10^9
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def reorderedPowerOf2(n: int) -> bool:
    # {power, result of 2^power}
    powers = {}
    strN = str(n)

    # find results of all possible power of 2 that have a length equal to the length of digits in n
    result = 0
    i = 0
    while len(str(result)) <= len(strN):
        result = 2 ** i
        if len(str(result)) == len(strN):
            powers[i] = result
        i += 1

    # count frequency of digit in n
    nTable = Counter(strN)

    # compare a frequency of digits in every result to the frequency of digits in n
    for p in powers:
        powerTable = Counter(str(powers[p]))
        if powerTable == nTable:
            return True

    return False

if __name__ == '__main__':
    print(reorderedPowerOf2(2**0)) # True
    print(reorderedPowerOf2(2 ** 1)) # True
    print(reorderedPowerOf2(2 ** 2)) # True
    print(reorderedPowerOf2(2**10)) # True
    print(reorderedPowerOf2(2 ** 25)) # True
    print(reorderedPowerOf2(10)) # False
    print(reorderedPowerOf2(15551)) # False
    print(reorderedPowerOf2(123456789)) # False


