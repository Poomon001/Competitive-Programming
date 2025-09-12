'''
    Link: https://leetcode.com/problems/longest-palindromic-substring/
    Purpose: Find the longest palindromic substring in s.
          : A palindrome when it reads the same backward as forward.
          : A substring is a contiguous sequence of characters within the string.
    parameter: str s - a string
    return: str longest_palindrome - longest palindromic substring in s
    Pre-Condition: 1 <= s.length <= 1000
                 : s consist of only digits and English letters.
    Post-Condition: none
'''
# greedy and two pointers- runtime: O(n^2), memory: O(1)
def longestPalindrome(s: str) -> str:
    longest_palindrome = ""

    for i in range(len(s)):
        left = right = i
        while right < len(s) and left >= 0 and s[left] == s[right]:
            if len(longest_palindrome) < right - left + 1:
                longest_palindrome = s[left:right + 1]
            right += 1
            left -= 1

        left = i
        right = i + 1
        while right < len(s) and left >= 0 and s[left] == s[right]:
            if len(longest_palindrome) < right - left + 1:
                longest_palindrome = s[left:right + 1]
            right += 1
            left -= 1

    return longest_palindrome

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(longestPalindrome("bbbab"))  # bbb
    print(longestPalindrome("abc"))  # a
    print(longestPalindrome("a"))  # a
    print(longestPalindrome("aa"))  # aa
    print(longestPalindrome("aaa"))  # aaa
    print(longestPalindrome("ab"))  # a
    print(longestPalindrome("aabbccc"))  # ccc
    print(longestPalindrome("aabbcc"))  # aa
    print(longestPalindrome("abba"))  # abba
    print(longestPalindrome("abbba"))  # abbba

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
