
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
    s1 = ""
    s2 = ""
    while left < right:
        if s[left] != s[right]:
            s1 = s[left:right]  # a new substring excluding the char at the right pointer
            s2 = s[left + 1:right + 1]  # a new substring excluding the char at the left pointer
            break
        left += 1
        right -= 1

    # Check if either of the substrings is a palindrome
    return s1 == s1[::-1] or s2 == s2[::-1]

if __name__ == "__main__":
    print(validPalindrome("aba")) # True
    print(validPalindrome("abca")) # True
    print(validPalindrome("abc")) # False
    print(validPalindrome("abc")) # False
    print(validPalindrome("deeee")) # True
    print(validPalindrome("lcupuuffuupucul")) # True
