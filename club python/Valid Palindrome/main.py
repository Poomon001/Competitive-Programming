'''
    Link: https://leetcode.com/problems/valid-palindrome/
    Purpose: Determine if s a valid palindrome. Consider only Alphanumeric characters include letters and numbers.
           : Ignore, if otherwise.
           : a palindrome is a string that reads the same forward and backward.
    parameter: string s - a string
    return: bool - return true if it is a palindrome, or false otherwise.
    Pre-Condition: 1 <= s.length <= 2 * 105
                 : s consists only of printable ASCII characters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def isPalindrome(s: str) -> bool:
    s = s.lower()
    phase = ""

    # filter
    for c in s:
        if c.islower() or c.isnumeric():
            phase = phase + c

    # check if a palindrome
    front = 0
    back = len(phase) - 1
    while front < back and len(phase) != 0:
        if phase[front] == phase[back]:
            front += 1
            back -= 1
        else:
            return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama")) # True
    print(isPalindrome("*& __")) # True
    print(isPalindrome("1010")) # False
    print(isPalindrome("11")) # True
    print(isPalindrome("0P")) # False
    print(isPalindrome("race a car")) # False
    print(isPalindrome(" ")) # True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
