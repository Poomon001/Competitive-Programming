from typing import List

'''
    Link: https://leetcode.com/problems/sequential-digits/
    Purpose: Find all integers that have sequential digits
           : sequential digits means each digit in the number is one more than the previous digit by 1
    parameter: int low - lower bound
             : int high - upper bound
    return: Optional[int] ans - a list of integer that contains sequential digits
    Pre-Condition: 10 <= low <= high <= 10^9
    Post-Condition: none
'''
# brute force - runtime: O(n), memory: O(1)
def sequentialDigits_M2(low: int, high: int) -> List[int]:
    # O(1) b/c there is a very fixed number of possible answers
    ans = []

    # loop though all numbers in the range between low and high
    for num in range(low, high + 1):
        num = str(num)
        prev = int(num[0])

        # loop though each digit in a number
        # O(9) = O(1)
        for i in range(1, len(num)):
            digit = int(num[i])
            # check if digits in an increasing order by 1
            if prev + 1 == digit:
                prev = digit
            else:
                break
        else:
            ans.append(int(num))

    return ans

'''
    Link: https://leetcode.com/problems/sequential-digits/
    Purpose: Find all integers that have sequential digits
           : sequential digits means each digit in the number is one more than the previous digit by 1
    parameter: int low - lower bound
             : int high - upper bound
    return: Optional[int] ans - a list of integer that contains sequential digits
    Pre-Condition: 10 <= low <= high <= 10^9
    Post-Condition: none
'''
# digit implementation - run-time: O(1), memory: O(1)
def sequentialDigits_M1(low: int, high: int) -> List[int]:
    # O(1) b/c there is a very fixed number of possible answers
    ans = []
    possibleAns = []

    # max range of 9 digits
    maxRange = "123456789"

    # get all possible integers has sequential digits
    # O(1) b/c there are only fixed int (9 digits) in maxRange
    for digit in range(2, 10):
        for j in range(0, len(maxRange) - digit + 1):
            to = digit + j
            possibleAns.append(maxRange[j:to])

    # filter the answer that is in between low and high
    # O(1) b/c there is a very fixed number of possible answers
    for num in possibleAns:
        num = int(num)
        if low <= num <= high:
            ans.append(num)

    return ans

if __name__ == '__main__':
    print("\n+=== faster solution ===+\n")
    print(sequentialDigits_M1(10, 88))  # [12, 23, 34, 45, 56, 67, 78]
    print(sequentialDigits_M1(100, 300))  # [123, 234]
    print(sequentialDigits_M1(1000, 13000))  # [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    print(sequentialDigits_M1(10, 99999999))  # [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789]

    print("\n+=== slower solution ===+\n")
    print(sequentialDigits_M2(10, 88)) # [12, 23, 34, 45, 56, 67, 78]
    print(sequentialDigits_M2(100, 300)) # [123, 234]
    print(sequentialDigits_M2(1000, 13000)) # [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    print("it will take about a minute")
    print(sequentialDigits_M2(10, 99999999)) # this will take about 60 sec, [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
