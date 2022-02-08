'''
    Link: https://leetcode.com/problems/add-digits/
    Purpose:  find the sum of all its digits until the result has only one digit
    parameter: int n - a number
    return: int sum - sum of all its digits until the result has only one digit
    Pre-Condition: 0 <= num <= 2^31 - 1
    Post-Condition: none
'''
# while...loop - runtime: O(n) where n is the number of digit, memory: O(1)
def addDigits_M1(num: int) -> int:
    # loop until num is a single digit
    while num > 9:
        sumDigit = 0
        for i in str(num):
            sumDigit += int(i)

        # update num
        num = sumDigit

    return num


'''
    Link: https://leetcode.com/problems/add-digits/
    Purpose:  find the sum of all its digits until the result has only one digit
    parameter: int n - a number
    return: int sum - sum of all its digits until the result has only one digit
    Pre-Condition: 0 <= num <= 2^31 - 1
    Post-Condition: none
'''
# while...loop - runtime: O(n) where n is the number of digit, memory: O(1)
def addDigits_M2(num: int) -> int:
    return __sumDigits(num)


def __sumDigits(num):
    if num < 10:
        return num

    # get the last digit and recursive call on the other digits
    return __sumDigits(num % 10 + __sumDigits(num // 10))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution M1 ===+\n")
    print(addDigits_M1(38)) # 11 -> 2
    print(addDigits_M1(0))  # 0
    print(addDigits_M1(123456789)) # 45 -> 9
    print(addDigits_M1(9))  # 9
    print(addDigits_M1(394))  # 7
    print(addDigits_M1(39485))  # 2

    print("\n+=== solution M2 ===+\n")
    print(addDigits_M2(38))  # 11 -> 2
    print(addDigits_M2(0))  # 0
    print(addDigits_M2(123456789))  # 45 -> 9
    print(addDigits_M2(9))  # 9
    print(addDigits_M2(394))  # 7
    print(addDigits_M2(39485))  # 2

