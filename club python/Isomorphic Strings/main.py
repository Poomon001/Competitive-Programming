'''
    Link: https://leetcode.com/problems/isomorphic-strings/
    Purpose: Given two strings s and t, determine if they are isomorphic.
           : Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    Parameter: str s: the first string
             : str t: the second string
    Returns: bool: true if isomorphic. Otherwise, false
    Pre-Condition: 1 <= s.length <= 5 * 104
                 : t.length == s.length
                 : s and t consist of any valid ascii character.
    Post-Condition: none
'''
# 1:1 check solution - Runtime: O(n^2), Memory: O(n)
def isIsomorphic(s: str, t: str) -> bool:
    if len(set(s)) != len(set(t)):
        return False

    # {s char, t cahr}
    sTot = {}

    # {t char, s char}
    tTos = {}

    for i, j in zip(s, t):
        # test 1:1 mapping
        if i in sTot and sTot[i] != j:
            return False

        # test 1:1 mapping
        if j in tTos and tTos[j] != i:
            return False

        sTot[i] = j
        tTos[j] = i

    return True

if __name__ == '__main__':
    print(" \n === method 1 === \n")
    print(isIsomorphic(s = "egg", t = "add")) # True
    print(isIsomorphic(s = "foo", t = "bar")) # False
    print(isIsomorphic(s = "paper", t = "title")) # True
    print(isIsomorphic(s="badc", t="baba")) #False
    print(isIsomorphic(s="233", t="011"))  # True
    print(isIsomorphic(s="100", t="987"))  # False
