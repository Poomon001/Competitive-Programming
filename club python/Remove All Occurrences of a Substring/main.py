'''
    Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
    Purpose: Find the leftmost occurrence of the substring part and remove it from s.
    parameter: string s - a string
             : string part - a shorter string
    return: string s - a string that doesn't contain "part"
    Pre-Condition: 1 <= s.length <= 1000
                 : 1 <= part.length <= 1000
                 : s and part consists of lowercase English letters
                 : s is longer than part
    Post-Condition: none
'''
def removeOccurrences(s: str, part: str) -> str:
    while len(s) >= len(part):

        s = s.replace(part, "", 1)

        if part not in s:
            break

    return s

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(removeOccurrences(s = "daabcbaabcbc", part = "abc")) # dab
    print(removeOccurrences(s="aabababa", part="aba"))  # ba
    print(removeOccurrences(s = "axxxxyyyyb", part = "xy")) # ab
    print(removeOccurrences(s = "xxxxxxx", part = "x")) #
    print(removeOccurrences(s="axxxxyyyyb", part="z")) # axxxxyyyyb


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
