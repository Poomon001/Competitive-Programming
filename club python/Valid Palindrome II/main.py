
'''
    Link: https://leetcode.com/problems/valid-palindrome-ii/
    Purpose: Determine if the s can be palindrome after deleting at most one character from it.
    parameter: str s - a string
    return: bool - return true if the s can be palindrome after deleting at most one character from it. Otherwise false
    Pre-Condition: 1 <= s.length <= 105
                 : s consists of lowercase English letters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def validPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    removeOne = False

    # scan from left and right
    while left < right:
        if s[left] != s[right]:
            if removeOne:
                return False
            else:
                removeOne = True
                # skip left
                if isPalindrome(s[left + 1:right + 1]):
                    left += 1
                    continue
                # skip right
                elif isPalindrome(s[left:right]):
                    right -= 1
                    continue
                else:
                    return False

        left += 1
        right -= 1
    return True


'''
Purpose: Determine if the s can be palindrome.
    parameter: str s - a string
    return: bool - return true if the s is palindrome. Otherwise false
    Pre-Condition: 1 <= s.length <= 105
                 : s consists of lowercase English letters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def isPalindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == "__main__":
    print(validPalindrome("aba")) # True
    print(validPalindrome("abca")) # True
    print(validPalindrome("abc")) # False
    print(validPalindrome("abc")) # False
    print(validPalindrome("deeee")) # True
    print(validPalindrome("lcupuuffuupucul")) # True
