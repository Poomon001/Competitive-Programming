'''
    Link: https://leetcode.com/problems/power-of-three/
    Purpose: Find if there exists an integer x such that n == 3^x
    parameter: int - an integer
    return: bool: return true if it is a power of three. Otherwise, return false.
    Pre-Condition: 231 <= n <= 231 - 1
    Post-Condition: none
'''
def isPowerOfThree(n: int) -> bool:
    pow = 1
    while (pow <= n):
        if (pow == n):
            return True
        pow *= 3

    return False

if __name__ == '__main__':
    print(isPowerOfThree(27)) # True
    print(isPowerOfThree(0)) # False
    print(isPowerOfThree(9)) # True
    print(isPowerOfThree(45)) # False
    print(isPowerOfThree(1)) # True
    print(isPowerOfThree(3)) # True

