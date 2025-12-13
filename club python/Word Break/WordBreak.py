from functools import cache
from typing import List

'''
    Link: https://leetcode.com/problems/word-break/
    Purpose: Find if s string can be segmented into a space-separated sequence of one or more dictionary words.
    parameter: str s - a string
             : List[str] wordDict - a list of strings
    return: bool - True if s can be segmented. otherwise, False
    Pre-Condition: 1 <= s.length <= 300
                 : 1 <= wordDict.length <= 1000
                 : 1 <= wordDict[i].length <= 20
                 : s and wordDict[i] consist of only lowercase English letters.
                 : All the strings of wordDict are unique.
    Post-Condition: none
'''
# bruteforce[without @cache] - runtime: O(2^n), space: O(1)
def wordBreak_m1(s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)
    @cache
    def recursive(i: int) -> bool:
        # base
        if i == len(s):
            return True

        for j in range(i, len(s)):
            if s[i:j + 1] in wordDict:
                if recursive(j + 1):
                    return True
        return False

    return recursive(0)

'''
    Link: https://leetcode.com/problems/word-break/
    Purpose: Find if s string can be segmented into a space-separated sequence of one or more dictionary words.
    parameter: str s - a string
             : List[str] wordDict - a list of strings
    return: bool - True if s can be segmented. otherwise, False
    Pre-Condition: 1 <= s.length <= 300
                 : 1 <= wordDict.length <= 1000
                 : 1 <= wordDict[i].length <= 20
                 : s and wordDict[i] consist of only lowercase English letters.
                 : All the strings of wordDict are unique.
    Post-Condition: none
'''
# top-up dp - runtime: O(n^2), memory: O(n)
def wordBreak_m2(s: str, wordDict: List[str]) -> bool:
    dp = {} # {start_index, is_match_from_start_index_to_end_string}
    wordDict = set(wordDict)
    def recursive(i: int) -> bool:
        # base
        if i == len(s):
            return True
        if i in dp:
            return dp[i]

        for j in range(i, len(s)):
            if s[i:j+1] in wordDict:
                if recursive(j + 1):
                    dp[i] = True
                    return True
        dp[i] = False
        return False

    return recursive(0)

'''
    Link: https://leetcode.com/problems/word-break/
    Purpose: Find if s string can be segmented into a space-separated sequence of one or more dictionary words.
    parameter: str s - a string
             : List[str] wordDict - a list of strings
    return: bool - True if s can be segmented. otherwise, False
    Pre-Condition: 1 <= s.length <= 300
                 : 1 <= wordDict.length <= 1000
                 : 1 <= wordDict[i].length <= 20
                 : s and wordDict[i] consist of only lowercase English letters.
                 : All the strings of wordDict are unique.
    Post-Condition: none
'''
# bottom-down - runtime: O(n^2), memory: O(n)
def wordBreak_m3(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    wordDict = set(wordDict)
    for i in range(len(s)):
        if dp[i] == True:
            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    dp[j + 1] = True
    return dp[-1]

if __name__ == "__main__":
    print("\n === Solution 1 === \n")
    print(wordBreak_m1("leetcode", ["leet","code"]))
    print(wordBreak_m1("applepenapple", ["apple","pen"]))
    print(wordBreak_m1("catsandog", ["cats","dog","sand","and","cat"]))
    print(wordBreak_m1("aaaaa", ["aaaa","aaa"]))
    print(wordBreak_m1("aaaaaaa", ["aaaaa", "aaa", "aa"]))
    print(wordBreak_m1("aaaaaaa", ["aaaaa", "aaa", "a"]))

    print("\n === Solution 2 === \n")
    print(wordBreak_m2("leetcode", ["leet", "code"]))
    print(wordBreak_m2("applepenapple", ["apple", "pen"]))
    print(wordBreak_m2("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(wordBreak_m2("aaaaa", ["aaaa", "aaa"]))
    print(wordBreak_m2("aaaaaaa", ["aaaaa", "aaa", "aa"]))
    print(wordBreak_m2("aaaaaaa", ["aaaaa", "aaa", "a"]))

    print("\n === Solution 3 === \n")
    print(wordBreak_m3("leetcode", ["leet", "code"]))
    print(wordBreak_m3("applepenapple", ["apple", "pen"]))
    print(wordBreak_m3("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(wordBreak_m3("aaaaa", ["aaaa", "aaa"]))
    print(wordBreak_m3("aaaaaaa", ["aaaaa", "aaa", "aa"]))
    print(wordBreak_m3("aaaaaaa", ["aaaaa", "aaa", "a"]))