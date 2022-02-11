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
    # {char : occurance}
    dic1 = Counter(s1)
    dic2 = Counter()

    # keep tract of chars in s1
    left = 0
    right = 0

    # make sure that s2 is equal or longer than s1
    if len(s1) > len(s2):
        return False

    # move right pointer and init dic2
    while right < len(s1) - 1:
        dic2.update({s2[right]: 1})
        right += 1

    # perform slicing window
    while right < len(s2):
        # add the next right element
        dic2.update({s2[right]: 1})

        # compare if they are permutation
        if dic1 == dic2:
            return True

        # remove left most element from a dic
        leftChar = s2[left]
        if dic2[leftChar] > 1:
            dic2.update({leftChar: -1})
        else:
            del dic2[leftChar]

        left += 1
        right += 1

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(checkInclusion("ab", "eidbaooo")) # True
    print(checkInclusion("ab", "eidbxaooo")) # False
    print(checkInclusion("horse", "ros")) # False
    print(checkInclusion("horse", "roseh")) # True
    print(checkInclusion("a", "a")) # True
    print(checkInclusion("a", "e")) # False
