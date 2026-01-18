from math import inf
from typing import List

li1 = ["fol", "flower", "flow", "fly", "flown"] #f
li2 = ["flower", "flow", "fly", "flown"] #fl
li3 = ["flower", "flow", "fly", "cat" ,"flown"] #""

'''
    Link: https://leetcode.com/problems/longest-common-prefix/
    Purpose: find the longest common prefix string amongst an array of strings.
    parameter: array - contains words
    return: string - longest common prefix
    Pre-Condition: only lower-case English letters.
                 : number of words is between 1 and 200
                 : number of chars in a word is between 0 and 200
    Post-Condition: none
'''
# two for...loop: runtime - O(n), memory - O(1)
def commonLongestPrefix_m1(strs: List[str]) -> str:
    target = ""
    length = inf
    for s in strs:
        if length > len(s):
            target = s
            length = len(s)

    longest_common_prefix = ""
    for i in range(len(target)):
        for s in strs:
            if s[i] != target[i]:
                return longest_common_prefix

        longest_common_prefix += target[i]
    return longest_common_prefix

'''
    Link: https://leetcode.com/problems/longest-common-prefix/
    Purpose: find the longest common prefix string amongst an array of strings.
    parameter: array - contains words
    return: string - longest common prefix
    Pre-Condition: only lower-case English letters.
                 : number of words is between 1 and 200
                 : number of chars in a word is between 0 and 200
    Post-Condition: none
'''
# onw for...loop: runtime - O(n), memory - O(1)
def commonLongestPrefix_m2(strs: List[str]) -> str:
    longest_common_prefix = ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for s in strs:
            if len(s) <= i:
                return longest_common_prefix

            if s[i] != c:
                return longest_common_prefix

        longest_common_prefix += c
    return longest_common_prefix


print("\n === Solution 1 === \n")
print(commonLongestPrefix_m1(li1)) # "f"
print(commonLongestPrefix_m1(li2)) # "fl"
print(commonLongestPrefix_m1(li3)) # ""

print("\n === Solution 2 === \n")
print(commonLongestPrefix_m2(li1)) # "f"
print(commonLongestPrefix_m2(li2)) # "fl"
print(commonLongestPrefix_m2(li3)) # ""


