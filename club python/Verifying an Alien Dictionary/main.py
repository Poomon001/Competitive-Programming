from typing import List

'''
    Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
    Purpose: Find if the given words are sorted lexicographically in this alien language.
    parameter: List[str] words - a list of words
             : str order - alphabet order in an alian language
    return: bool - return true if and only if the given words are sorted lexicographically in this alien language.
    Pre-Condition: 1 <= words.length <= 100
                 : 1 <= words[i].length <= 20
                 : order.length == 26
                 : All characters in words[i] and order are English lowercase letters.
    Post-Condition: none
'''
def isAlienSorted(words: List[str], order: str) -> bool:
    # {aphabet, order value}
    dic = {}
    value = 0

    # to store key and value
    for c in order:
        dic[c] = value
        value += 1

    # compare 2 words value
    for i in range(len(words) - 1):

        for j in range(len(words[i])):
            # if first word repeat second word but longer
            if len(words[i + 1]) < j + 1:
                return False

            # first is lower than second word's letter
            if dic[words[i][j]] < dic[words[i + 1][j]]:
                break
            if dic[words[i][j]] == dic[words[i + 1][j]]:
                continue
            else:
                return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
    print(isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # False
    print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # False
    print(isAlienSorted(["hello", "hello"], "hello")) # True
    print(isAlienSorted(["app", "apple"], "worldabcefghijkmnpqstuvxyz")) # True
