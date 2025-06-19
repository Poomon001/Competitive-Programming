'''
    Link: https://leetcode.com/problems/happy-number/
    Purpose: Determine if it is a happy number:
           : Starting with any positive integer, replace the number by the sum of the squares of its digits.
           : Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
           : Those numbers for which this process ends in 1 are happy.
    Parameters: num n - a number to check if happy
    Returns: boolean - true if happy. Otherwise false
    Pre-Condition: 1 <= n <= 2^31 - 1
    Post-Condition : None
'''
# Hashset with int-to-string - runtime: O(log(n)), space: O(log(n))
def isHappy_M1(n: int) -> bool:
    num_to_squr = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
    seen = set()
    while True:
        total = 0

        for i in range(len(str(n))):
            digit = str(n)[i]
            total += num_to_squr[digit]

        if total == 1:
            return True
        if total in seen:
            return False

        seen.add(total)
        n = total
    return False

'''
    Link: https://leetcode.com/problems/happy-number/
    Purpose: Determine if it is a happy number:
           : Starting with any positive integer, replace the number by the sum of the squares of its digits.
           : Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
           : Those numbers for which this process ends in 1 are happy.
    Parameters: num n - a number to check if happy
    Returns: boolean - true if happy. Otherwise false
    Pre-Condition: 1 <= n <= 2^31 - 1
    Post-Condition : None
'''
# Hashset with mod last digit - runtime: O(log(n)), space: O(log(n))
def isHappy_M2(n: int) -> bool:
    num_to_squr = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    seen = set()
    while True:
        total = 0

        while n != 0:
            digit = n % 10
            n = n // 10
            total += num_to_squr[digit]

        if total == 1:
            return True
        if total in seen:
            return False

        seen.add(total)
        n = total
    return False

'''
    Link: https://leetcode.com/problems/happy-number/
    Purpose: Determine if it is a happy number:
           : Starting with any positive integer, replace the number by the sum of the squares of its digits.
           : Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
           : Those numbers for which this process ends in 1 are happy.
    Parameters: num n - a number to check if happy
    Returns: boolean - true if happy. Otherwise false
    Pre-Condition: 1 <= n <= 2^31 - 1
    Post-Condition : None
'''
# slow and fast cycle detection - runtime: O(log(n)), space: O(1)
def isHappy_M3(n: int) -> bool:
    def nextSum(n):
        num_to_squr = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        total = 0
        while n != 0:
            digit = n % 10
            n = n // 10
            total += num_to_squr[digit]
        return total

    slow = n
    fast = nextSum(n)
    while fast != 1 and slow != fast:
        slow = nextSum(slow)
        fast = nextSum(nextSum(fast))
    return fast == 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(isHappy_M1(19)) # True
    print(isHappy_M1(1)) # True
    print(isHappy_M1(2)) # False
    print(isHappy_M1(7)) # True
    print(isHappy_M1(100)) # True
    print(isHappy_M1(11111111)) # False

    print("\n === Solution 2 === \n")
    print(isHappy_M2(19))  # True
    print(isHappy_M2(1))  # True
    print(isHappy_M2(2))  # False
    print(isHappy_M2(7))  # True
    print(isHappy_M2(100))  # True
    print(isHappy_M2(11111111))  # False


    print("\n === Solution 3 === \n")
    print(isHappy_M3(19)) # True
    print(isHappy_M3(1)) # True
    print(isHappy_M3(2)) # False
    print(isHappy_M3(7)) # True
    print(isHappy_M3(100)) # True
    print(isHappy_M3(11111111)) # False

