from collections import Counter
'''
    Link: https://leetcode.com/problems/ransom-note/
    Purpose: Find if 'ransomNote' can be constructed by using the letters from 'magazine'
    parameter: str ransomNote - a string
             : str magazine - a string
    return: bool - true if ransomNote can be constructed by using the letters from magazine and false otherwise.
    Pre-Condition: 1 <= ransomNote.length, magazine.length <= 105
                 : ransomNote and magazine consist of lowercase English letters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomNoteDic = Counter(ransomNote)
    magazineDic = Counter(magazine)

    for i in range(97, 123):
        i = chr(i)
        if i in ransomNoteDic and i not in magazineDic:
            return False

        if i in magazineDic and i in ransomNoteDic:
            if magazineDic[i] < ransomNoteDic[i]:
                return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(canConstruct("abc","abc")) # True
    print(canConstruct("a", "b")) # False
    print(canConstruct("aa", "ab")) # False
    print(canConstruct("aa","aba")) # True
    print(canConstruct("axyzz", "axyz")) # False



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
