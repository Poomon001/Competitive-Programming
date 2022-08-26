'''
    Link: https://leetcode.com/problems/power-of-three/
    Purpose: Find if there exists an integer x such that n == 3^x
    parameter: int - an integer
    return: bool: return true if it is a power of three. Otherwise, return false.
    Pre-Condition: 231 <= n <= 231 - 1
    Post-Condition: none
'''
# runtime: O(log(n)), memory: O(1)
def isPowerOfThree_M1(n: int) -> bool:
    pow = 1
    # increse by power of 3 until over n
    while (pow <= n):
        if (pow == n):
            return True
        pow *= 3

    return False

'''
    Link: https://leetcode.com/problems/power-of-three/
    Purpose: Find if there exists an integer x such that n == 3^x
    parameter: int - an integer
    return: bool: return true if it is a power of three. Otherwise, return false.
    Pre-Condition: 231 <= n <= 231 - 1
    Post-Condition: none
'''
# runtime: O(log(n)), memory: O(1)
def isPowerOfThree_M2(n: int) -> bool:
    # decrease by power of 3 until reach 3^0 = 1. Otherwise return false
    while n > 1:
        if n%3 == 0:
            n = n/3
        else:
            return False

    return n == 1

if __name__ == '__main__':
    print("\n+=== Solution1 ===+\n")
    print(isPowerOfThree_M1(27)) # True
    print(isPowerOfThree_M1(0)) # False
    print(isPowerOfThree_M1(9)) # True
    print(isPowerOfThree_M1(45)) # False
    print(isPowerOfThree_M1(1)) # True
    print(isPowerOfThree_M1(3)) # True

    print("\n+=== Solution2 ===+\n")
    print(isPowerOfThree_M2(27)) # True
    print(isPowerOfThree_M2(0)) # False
    print(isPowerOfThree_M2(9)) # True
    print(isPowerOfThree_M2(45)) # False
    print(isPowerOfThree_M2(1)) # True
    print(isPowerOfThree_M2(3)) # True
