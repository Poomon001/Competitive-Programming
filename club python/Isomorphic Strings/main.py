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
# using 'in' solution - Runtime: O(n^2), Memory: O(n)
def isIsomorphic_M1(s: str, t: str) -> bool:
    dicS = {}
    dicT = {}

    # check each char of s map 1:1 to char of t
    for i, j in zip(s,t):
        # initialize new relationship of S char and T char
        if i not in dicS:
            dicS[i] = j

        # initialize new relationship of T char and S char
        if j not in dicT:
            dicT[j] = i

        # 1 unique S map to any t
        if i in dicS:
            if dicS[i] != j:
                return False

        # 1 unique t map to any s
        if j in dicT:
            if dicT[j] != i:
                return False

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
# access a dic solution - Runtime: O(n), Memory: O(n)
def isIsomorphic_M2(s: str, t: str) -> bool:
    dicS = {}
    dicT = {}

    # initialize a dictionary with keys in all ascii
    for i in range(128):
        dicS[chr(i)] = 0
        dicT[chr(i)] = 0

    # check each char of s map 1:1 to char of t
    for i, j in zip(s,t):
        # initialize new relationship of S char and T char
        if dicS[i] == 0:
            dicS[i] = j

        # initialize new relationship of T char and S char
        if dicT[j] == 0:
            dicT[j] = i

        # 1 unique S map to any t
        if dicS[i] != 0 and dicS[i] != j:
            return False

        # 1 unique t map to any s
        if dicT[j] != 0 and dicT[j] != i:
            return False

    return True



if __name__ == '__main__':
    print(" \n === method 1 === \n")
    print(isIsomorphic_M1(s = "egg", t = "add")) # True
    print(isIsomorphic_M1(s = "foo", t = "bar")) # False
    print(isIsomorphic_M1(s = "paper", t = "title")) # True
    print(isIsomorphic_M1(s="badc", t="baba")) #False
    print(isIsomorphic_M1(s="233", t="011"))  # True
    print(isIsomorphic_M1(s="100", t="987"))  # False

    print(" \n === method 2 === \n")
    print(isIsomorphic_M2(s="egg", t="add"))  # True
    print(isIsomorphic_M2(s="foo", t="bar"))  # False
    print(isIsomorphic_M2(s="paper", t="title"))  # True
    print(isIsomorphic_M2(s="badc", t="baba"))  # False
    print(isIsomorphic_M2(s="233", t="011"))  # True
    print(isIsomorphic_M2(s="100", t="987"))  # False
