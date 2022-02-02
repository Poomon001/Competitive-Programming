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
    pCounter = Counter(p)
    sCounter = Counter()
    ans = []
    left = 0
    right = 0

    if len(p) > len(s):
        return []

    # move right pointer and init dictionary
    while right < len(p)-1:
        sCounter.update({s[right]:1})
        right += 1


    while right < len(s):
        # add right-most char from dic
        sCounter.update({s[right]: 1})

        # compare 2 dic
        if sCounter == pCounter:
            ans.append(left)

        # remove left-most char from dic
        sCounter[s[left]] -= 1
        if sCounter[s[left]] == 0:
            char = s[left]
            del sCounter[char] # O(1)

        # slicing window by 1 char
        left += 1
        right +=1

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
