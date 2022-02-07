from collections import Counter
'''
    Link: https://leetcode.com/problems/find-the-difference/
    Purpose: Find an added char in string t.
    parameter: str s - a string
             : str t - the string s that is added one extra char and all chars are in a different order than string s.
    return: str -  an added char
    Pre-Condition: 0 <= s.length <= 1000
                 : t.length == s.length + 1
                 : s and t consist of lower-case English letters.
    Post-Condition: none
'''
# runtime: O(nlog(n)), memory: O(1)
def findTheDifference_M1(s: str, t: str) -> str:
    t = sorted(t)
    s = sorted(s)
    for sChar, tChar in zip(s, t):
        if sChar != tChar:
            return tChar

    return t[-1:][0]

'''
    Link: https://leetcode.com/problems/find-the-difference/
    Purpose: Find an added char in string t.
    parameter: str s - a string
             : str t - the string s that is added one extra char and all chars are in a different order than string s.
    return: str -  an added char
    Pre-Condition: 0 <= s.length <= 1000
                 : t.length == s.length + 1
                 : s and t consist of lower-case English letters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def findTheDifference_M2(s: str, t: str) -> str:
    # init a dic of a to z
    dic = {}
    for i in range(97, 123):
        dic[chr(i)] = 0

    # count all char in an original string
    for sChar in s:
        if sChar in dic:
            dic[sChar] = dic[sChar] + 1

    # discount all char in an temp string
    for tChar in t:
        if tChar in dic:
            dic[tChar] = dic[tChar] - 1

    return [key for key, value in dic.items() if value == -1][0]


'''
    Link: https://leetcode.com/problems/find-the-difference/
    Purpose: Find an added char in string t.
    parameter: str s - a string
             : str t - the string s that is added one extra char and all chars are in a different order than string s.
    return: str -  an added char
    Pre-Condition: 0 <= s.length <= 1000
                 : t.length == s.length + 1
                 : s and t consist of lower-case English letters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def findTheDifference_M3(s: str, t: str) -> str:
    # {char, occurance}
    sMap = Counter(s)
    tMap = Counter(t)

    for char in t:
        # if occurance is different, we get the answer
        if sMap[char] != tMap[char]:
            return char

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution M1 ===+\n")
    print(findTheDifference_M1("abcd", "abcde")) # e
    print(findTheDifference_M1("", "y")) # y
    print(findTheDifference_M1("abcd", "dakcb")) # k
    print(findTheDifference_M1("abcd", "zbcad")) # z
    print(findTheDifference_M1("a", "aa")) # a
    print(findTheDifference_M1("ae", "aea")) # a

    print("\n+=== solution M2 ===+\n")
    print(findTheDifference_M2("abcd", "abcde"))  # e
    print(findTheDifference_M2("", "y"))  # y
    print(findTheDifference_M2("abcd", "dakcb"))  # k
    print(findTheDifference_M2("abcd", "zbcad"))  # z
    print(findTheDifference_M2("a", "aa"))  # a
    print(findTheDifference_M2("ae", "aea"))  # a

    print("\n+=== solution M3 ===+\n")
    print(findTheDifference_M3("abcd", "abcde"))  # e
    print(findTheDifference_M3("", "y"))  # y
    print(findTheDifference_M3("abcd", "dakcb"))  # k
    print(findTheDifference_M3("abcd", "zbcad"))  # z
    print(findTheDifference_M3("a", "aa"))  # a
    print(findTheDifference_M3("ae", "aea"))  # a

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
