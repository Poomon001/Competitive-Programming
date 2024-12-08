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
# 1:1 check solution - Runtime: O(n), Memory: O(n)
def isIsomorphic_M1(s: str, t: str) -> bool:
    if len(set(s)) != len(set(t)):
        return False

    # {s char, t cahr}
    sTot = {}

    # {t char, s char}
    tTos = {}

    for i, j in zip(s, t):
        # test 1:1 mapping (rediscover i that already in sTot,
        # but the value of sTot[i] already in sTot doesnt match new j value)
        if i in sTot and sTot[i] != j:
            return False

        # test 1:1 mapping
        if j in tTos and tTos[j] != i:
            return False

        sTot[i] = j
        tTos[j] = i

    return True

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
# hashmap solution - Runtime: O(n), Memory: O(n)
def isIsomorphic_M2(s: str, t: str) -> bool:
    if len(set(s)) != len(set(t)):
        return False

    # {s char, t cahr}
    sTot = {}

    for i, j in zip(s, t):
        if i not in sTot:
            sTot[i] = j

    newS = ""
    for i in s:
        newS += sTot[i]

    return newS == t

if __name__ == '__main__':
    print("=== solution 1 ===\n")
    print(isIsomorphic_M1(s = "egg", t = "add")) # True
    print(isIsomorphic_M1(s = "foo", t = "bar")) # False
    print(isIsomorphic_M1(s = "paper", t = "title")) # True
    print(isIsomorphic_M1(s="badc", t="baba")) #False
    print(isIsomorphic_M1(s="233", t="011"))  # True
    print(isIsomorphic_M1(s="100", t="987"))  # False
    print(isIsomorphic_M1(s="bbbaaaba", t="aaabbbba")) # False
    print(isIsomorphic_M1(s="aaabbbba", t="bbbaaaba"))  # False

    print("=== solution 2 ===\n")
    print(isIsomorphic_M2(s="egg", t="add"))  # True
    print(isIsomorphic_M2(s="foo", t="bar"))  # False
    print(isIsomorphic_M2(s="paper", t="title"))  # True
    print(isIsomorphic_M2(s="badc", t="baba"))  # False
    print(isIsomorphic_M2(s="233", t="011"))  # True
    print(isIsomorphic_M2(s="100", t="987"))  # False
    print(isIsomorphic_M2(s="bbbaaaba", t="aaabbbba"))  # False
    print(isIsomorphic_M2(s="aaabbbba", t="bbbaaaba"))  # False