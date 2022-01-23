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
# runtime: O(n), memory: O(1)
def sequentialDigits(low: int, high: int) -> List[int]:
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sequentialDigits(10, 88)) # [12, 23, 34, 45, 56, 67, 78]
    print(sequentialDigits(100, 300)) # [123, 234]
    print(sequentialDigits(1000, 13000)) # [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    print(sequentialDigits(10, 99999999)) # this will take about 60 sec, [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
