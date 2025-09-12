'''
    Link: https://leetcode.com/problems/longest-palindromic-subsequence/
    Purpose: Find the longest palindromic subsequence's length in s.
          : A palindrome when it reads the same backward as forward.
          : A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
          : without changing the order of the remaining elements.
    parameter: str s - a string
    return: int - the longest palindromic subsequence's length in s.
    Pre-Condition: 1 <= s.length <= 1000
                 : s consist of only digits and English letters.
    Post-Condition: none
'''
# dp - runtime: O(n^2), memory: O(n^2)
def longestPalindromeSubseq(s: str) -> int:
    s_reverse = s[::-1]
    # "abca" -> "acba"
    # "cbbac" -> "cabbc"
    #   c b b a c
    # c 1 1 1 1 1
    # a 1 1 1 2 2
    # b 1 2 2 2 2
    # b 1 2 3 3 3
    # c 1 2 3 3 4
    grid = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(s_reverse) + 1):
            if s[i - 1] == s_reverse[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i][j - 1], grid[i - 1][j])

    return grid[-1][-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(longestPalindromeSubseq("bbbab"))  # 4
    print(longestPalindromeSubseq("abc"))  # 1
    print(longestPalindromeSubseq("a"))  # 1
    print(longestPalindromeSubseq("aa"))  # 2
    print(longestPalindromeSubseq("aaa"))  # 3
    print(longestPalindromeSubseq("ab"))  # 1
    print(longestPalindromeSubseq("aabbccc"))  # 3
    print(longestPalindromeSubseq("aabbcc"))  # 2
    print(longestPalindromeSubseq("abba"))  # 4
    print(longestPalindromeSubseq("abbba"))  # 5
