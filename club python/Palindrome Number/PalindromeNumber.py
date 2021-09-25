'''
    Link: https://leetcode.com/problems/palindrome-number/
    Purpose: Find if an interger is palindrome integer
    parameter: integer - any number
    return: boolean - true if the integer is palindrome. Otherwise false
    Pre-Condition: input not empty
                 : -231 <= int <= 231 - 1
    Post-Condition: none
'''

def isPanlindromeNumber(num: int) -> bool:
    reverseNum = str(num)[::-1]
    if(str(num) == reverseNum):
        return True
    return False

print(isPanlindromeNumber(121)) # Talse
print(isPanlindromeNumber(-121)) # False
print(isPanlindromeNumber(10)) # False
print(isPanlindromeNumber(-101)) # False
