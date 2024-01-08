from typing import List
'''
    Link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
    Purpose: Given given an array of strings.
           :Determine if you can make/distribute every character in each string equal using any operations
    parameter: List[str] - a list of strings
    return: bool - true if you can make every character in each string equal. Otherwise, false.
    Pre-Condition: 1 <= words.length <= 100
                 : 1 <= words[i].length <= 100
                 : words[i] consists of lowercase English letters.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def makeEqual(words: List[str]) -> bool:
    numWrods = len(words)
    charCount = {}

    for word in words:
        for c in word:
            if c in charCount:
                charCount[c] += 1
            else:
                charCount[c] = 1

    # note: we dont need to handle the order of the character, since
    # we know that if each string has the same number of characters we can sort all of them
    for key, value in charCount.items():
        if value % numWrods != 0:
            return False
    return True

if __name__ == '__main__':
    print(makeEqual(["abc", "aabc", "cb", "abc"])) # True
    print(makeEqual(["abc","aabc","bc"])) # True
    print(makeEqual(["ab","a"])) # False
    print(makeEqual(["a", "ba"])) # False
    print(makeEqual(["abc"])) # True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
