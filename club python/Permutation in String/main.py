from collections import Counter

'''
    Link: https://leetcode.com/problems/permutation-in-string/
    Purpose: Determine if string 1 is a Permutation of string 2 
    parameter: str s1 - the first string
             : str s2 - the second string
    return: bool - return true if s2 contains a permutation of s1, or false otherwise.
    Pre-Condition: 1 <= s1.length, s2.length <= 104
                 : s1 and s2 consist of lowercase English letters.
    Post-Condition: none
'''
# slicing window algo - rumtime: O(n), memory: O(m) where m is len(s1)
def checkInclusion(s1: str, s2: str) -> bool:
    s1Count = Counter(s1)
    subCount = Counter()
    size = len(s1)

    i = 0
    j = 0

    while j < len(s2):
        subCount[s2[j]] = subCount.get(s2[j], 0) + 1

        if subCount == s1Count:
            return True

        if j - i == size - 1:
            subCount[s2[i]] = subCount.get(s2[i], 0) - 1
            if subCount[s2[i]] == 0:
                del subCount[s2[i]]
            i += 1

        j += 1
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(checkInclusion("ab", "eidbaooo")) # True
    print(checkInclusion("ab", "eidbxaooo")) # False
    print(checkInclusion("horse", "ros")) # False
    print(checkInclusion("horse", "roseh")) # True
    print(checkInclusion("a", "a")) # True
    print(checkInclusion("a", "e")) # False
