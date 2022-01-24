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
def detectCapitalUse_M1(word: str) -> bool:
    isAllUpper = True
    isAllLower = True
    isOnlyFirstUpper = True

    # check if the first char upper case
    if 'A' <= word[0] <= 'Z':
        isAllLower = False
    else:
        isAllUpper = False
        isOnlyFirstUpper = False

    # check the rest of character
    for i in range(1, len(word)):
        # check if a char upper case
        if 'A' <= word[i] <= 'Z':
            isAllLower = False
            isOnlyFirstUpper = False
        else:
            isAllUpper = False

    return isAllUpper or isAllLower or isOnlyFirstUpper

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
def detectCapitalUse_M2(word: str) -> bool:
    return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())


if __name__ == '__main__':
    print("\n+=== Long solution ===+\n")
    print(detectCapitalUse_M1("USA")) # True
    print(detectCapitalUse_M1("leetcode")) # True
    print(detectCapitalUse_M1("Google")) # True
    print(detectCapitalUse_M1("FlaG")) # False
    print(detectCapitalUse_M1("flaG"))  # False

    print("\n+=== short solution ===+\n")
    print(detectCapitalUse_M2("USA"))  # True
    print(detectCapitalUse_M2("leetcode"))  # True
    print(detectCapitalUse_M2("Google"))  # True
    print(detectCapitalUse_M2("FlaG"))  # False
    print(detectCapitalUse_M1("flaG"))  # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
