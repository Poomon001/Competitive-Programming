'''
    Link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
    Purpose:  find the length of the longest substring between two equal characters. If there is no such substring return -1.
    parameter: String s - a string.
    return: int maxCount - the length of the longest substring between two equal characters
    Pre-Condition: 1 <= s.length <= 300
                 : s contains only lowercase English letters.
    Post-Condition: none
'''
# brute force: O(n^2), memory: O(1)
def maxLengthBetweenEqualCharacters_M1(s: str) -> int:
    maxCount = -1

    if len(s) == 1:
        return -1

    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                maxCount = max(maxCount, j - i - 1)

    return maxCount


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(maxLengthBetweenEqualCharacters_M1("aa")) # 0
    print(maxLengthBetweenEqualCharacters_M1("abca")) # 2
    print(maxLengthBetweenEqualCharacters_M1("cbzxy")) # -1
    print(maxLengthBetweenEqualCharacters_M1("abcaaa")) # 4
    print(maxLengthBetweenEqualCharacters_M1("abcaaabqwerc")) # 8

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
