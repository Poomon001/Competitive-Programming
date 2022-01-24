'''
    Link: https://leetcode.com/problems/detect-capital/
    Purpose: Determine if ONE of the following cases holds:
           : 1. All letters in this word are capitals, like "USA".
           : All letters in this word are not capitals, like "leetcode".
           : Only the first letter in this word is capital, like "Google".
    parameter: str word - a string
    return: bool - true if one of the  above-mentioned properties hold
    Pre-Condition: 1 <= word.length <= 100
                 : word consists of lowercase and uppercase English letters.
    Post-Condition: none
'''

# runtime: O(n), memory: O(1)
def detectCapitalUse(word: str) -> bool:
    isAllUpper = True
    isAllLower = True
    isOnlyFirstUpper = True

    # check if the first char upper case
    if 65 <= ord(word[0]) <= 90:
        isAllLower = False
    else:
        isAllUpper = False
        isOnlyFirstUpper = False

    # check the rest of character
    for i in range(1, len(word)):
        # check if a char upper case
        if 65 <= ord(word[i]) <= 90:
            isAllLower = False
            isOnlyFirstUpper = False
        else:
            isAllUpper = False

    return isAllUpper or isAllLower or isOnlyFirstUpper


if __name__ == '__main__':
    print(detectCapitalUse("USA")) # True
    print(detectCapitalUse("leetcode")) # True
    print(detectCapitalUse("Google")) # True
    print(detectCapitalUse("FlaG")) # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
