from typing import List

'''
    Link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
    Purpose: Find the maximum possible length if string s formed formed by a subsequence of arr that has unique characters.
    parameter: List[str] - an array of string
    return: int maxLength - the maximum possible length if string s formed formed by a subsequence of arr that has unique characters.
    Pre-Condition: 1 <= arr.length <= 16
                 : 1 <= arr[i].length <= 26
                 : arr[i] contains only lowercase English letters.
    Post-Condition: none
'''
# backtrck - runtime: O(n*2^n), memory: O(n*2^n) -> n^2 is the powerset strings, n is max of n character per string
def maxLength(arr: List[str]) -> int:
    subset = []
    maxLength = 0

    def backtrack(i):
        nonlocal maxLength

        if i >= len(arr):
            word = "".join(subset)
            length = len(word)
            uniqueLength = len("".join(set(word)))

            if length == uniqueLength:
                maxLength = max(maxLength, uniqueLength)
            return

        subset.append(arr[i])
        backtrack(i + 1)

        subset.pop()
        backtrack(i + 1)

    backtrack(0)

    return maxLength


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(maxLength(["un","iq","ue"])) # 4 -> "uniq" or "ique"
    print(maxLength(["cha","r","act","ers"])) # 6 -> "chaers" or "acters"
    print(maxLength(["abcdefghijklmnopqrstuvwxyz"])) # 26
    print(maxLength(["a"])) # 1
    print(maxLength(["a", "a", "aa", "aaa", "aaaa"]))  # 1
    print(maxLength(["e", "d", "b", "c", "a"]))  # 5
