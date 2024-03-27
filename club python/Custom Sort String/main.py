from collections import Counter
'''
    Link: https://leetcode.com/problems/custom-sort-string
    Purpose: Given two string order and s. Order string, representing the order of characters, contains unique characters.
           : Re-order s such that it sorted by the order of character appearance in Order string
           : e.g order = "cba", all 'c' char will be at the front, all 'b' chars will be at the middle, all 'a' char will be at the end
           : s = "abcacb" => "ccbbaa"
    parameter: string order - a string containing unique character
             : string s - a string
    return: str ans - the sorted strings by the order of characters appearance in Order string
    Pre-Condition: 1 <= order.length <= 26
                 : 1 <= s.length <= 200
                 : order and s consist of lowercase English letters.
                 : All the characters of order are unique.
    Post-Condition: None
'''
# brute force - run time: O(n), memory: O(1)
def customSortString(order: str, s: str) -> str:
    charToFreq = Counter(s)
    ans = ""
    # add letters that are specified in order orderly
    for c in order:
        ans += c * charToFreq[c]
        charToFreq[c] = 0

    # add letters that are not specified in order but are in s
    for c, freq in charToFreq.items():
        ans += c * freq

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(customSortString("cba", "abcdbcae")) # ccbbaade
    print(customSortString("bac", "abcbcaed")) # bbaacced
    print(customSortString("abc", "deabcbca")) # aabbccde
    print(customSortString("bcafg", "abcd")) # bcad
    print(customSortString("", "zxcasd"))  # zxcasd
    print(customSortString("abc", "abcbca"))  # aabbcc

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
