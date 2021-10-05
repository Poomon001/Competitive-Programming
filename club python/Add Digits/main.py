'''
    Link: https://leetcode.com/problems/add-digits/
    Purpose:  find the sum of all its digits until the result has only one digit
    parameter: int n - a number
    return: int sum - sum of all its digits until the result has only one digit
    Pre-Condition: 0 <= num <= 2^31 - 1
    Post-Condition: none
'''
# runtime: O(n) where n is the number of digit, memory: O(1)
def addDigits(num: int) -> int:
    # loop until one digit left: O(1)
    while (True):
        sum = 0
        # find sum of all digits: O(n)
        for digit in str(num):
            sum += int(digit)

        # if the sum of digits results in a single digit number, we are done
        if (len(str(sum)) == 1):
            return sum

        # update num
        num = sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(addDigits(38)) # 11 -> 2
    print(addDigits(0))  # 0
    print(addDigits(123456789)) # 45 -> 9
    print(addDigits(9))  # 9
