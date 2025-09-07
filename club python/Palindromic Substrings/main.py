'''
    Link: https://leetcode.com/problems/palindromic-substrings
    Purpose: Find the number of palindromic substrings in String s,
           : A string is a palindrome when it reads the same backward as forward.
           : A substring is a contiguous sequence of characters within the string.
    parameter: str s - a string
    return: int count: a total number of palindromic substrings within s
    Pre-Condition: 1 <= s.length <= 1000
                 : s consists of lowercase English letters.
    Post-Condition: none
'''

# two pointer: runtime: O(n^2), memory: O(1)
def countSubstrings(s: str) -> int:
    # 1. start from the middle, exception for first and last characters
    # 2. expand left and right pointers by 1 from the center
    # 3. check if s[left] == s[right] -> valid_palindromic
    count = 0

    for i in range(len(s)):
        # for odd substring "a", "aaa", "aba"
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        # for even substring "aa", "aaaa", "abba"
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(countSubstrings("abc")) # 3
    print(countSubstrings("a")) # 1
    print(countSubstrings("aa")) # 3
    print(countSubstrings("aaa")) # 6
    print(countSubstrings("ab")) # 2
    print(countSubstrings("aabbccc")) # 12
    print(countSubstrings("aabbcc")) # 9
    print(countSubstrings("abba")) # 6
    print(countSubstrings("abbba")) # 9

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
