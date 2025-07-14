from collections import Counter
from typing import List

'''
    Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
    Purpose: Find an array of all the start indices of p's permutations in s
    parameter: str s - first string
             : str P - second string
    return: List[int] ans -  an array of all the start indices
    Pre-Condition: 1 <= s.length, p.length <= 3 * 10^4
                 : s and p consist of lowercase English letters.
    Post-Condition: none
'''
# two-pointer and counting matching char solution - runtime: O(sp), memory: O(1) excluding the returned answer
def findAnagrams_M1(s: str, p: str) -> List[int]:
    # {"char", occurance}
    dic = Counter(p)
    # store answers
    ans = []
    left = 0
    right = 0

    while right < len(s):
        char = s[right]

        # detect a matching char in anagram
        if char in dic and dic[char] > 0:
            dic[char] -= 1
            right += 1
        else:
            # reset dic and move to a next char
            dic = Counter(p)
            left += 1
            right = left

        if right - left == len(p):
            ans.append(left)
            # reset dic and move to a next char
            dic = Counter(p)
            left += 1
            right = left

    return ans

'''
    Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
    Purpose: Find an array of all the start indices of p's permutations in s
    parameter: str s - first string
             : str P - second string
    return: List[int] ans -  an array of all the start indices
    Pre-Condition: 1 <= s.length, p.length <= 3 * 10^4
                 : s and p consist of lowercase English letters.
    Post-Condition: none
'''
# slicing window and compare two dictionaries solution - runtime: O(s), memory: O(1) excluding the returned answer
def findAnagrams_M2(s: str, p: str) -> List[int]:
    size = len(p)
    pToCount = Counter(p)
    subToCount = {}
    ans = []
    l = 0
    r = 0

    while r < len(s):
        subToCount[s[r]] = subToCount.get(s[r], 0) + 1

        if r - l >= size:
            subToCount[s[l]] = subToCount.get(s[l], 0) - 1
            if subToCount[s[l]] <= 0:
                del subToCount[s[l]]
            l += 1

        if pToCount == subToCount:
            ans.append(l)

        r += 1

    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution 1 ===+\n")
    print(findAnagrams_M1("cbaebabacd", "abc")) # [0, 6]
    print(findAnagrams_M1("nml", "abc")) # []
    print(findAnagrams_M1("abab", "ab")) # [0, 1, 2]
    print(findAnagrams_M1("abab", "a")) # [0, 2]
    print(findAnagrams_M1("aaaaaaaaaa","aaaaaaaaaaaaa")) # []

    print("\n+=== solusion 2 ===+\n")
    print(findAnagrams_M2("cbaebabacd", "abc"))  # [0, 6]
    print(findAnagrams_M2("nml", "abc"))  # []
    print(findAnagrams_M2("abab", "ab"))  # [0, 1, 2]
    print(findAnagrams_M2("abab", "a"))  # [0, 2]
    print(findAnagrams_M2("aaaaaaaaaa", "aaaaaaaaaaaaa"))  # []

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
