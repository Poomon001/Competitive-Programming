'''
    Link: https://leetcode.com/problems/first-unique-character-in-a-string/
    Purpose:  find the first non-repeating character in it and return its index. If it does not exist, return -1.
    parameter: str s - a string
    return: int - an index of the first non-repeating character. -1 if non-repeating char is not found
    Pre-Condition: 1 <= s.length <= 105
                 : s consists of only lowercase English letters.
    Post-Condition: none
'''

# mem O(1) and runtime O(n)
def firstUniqChar(s: str) -> int:
    # hashmap {alphabet: occurrence count}
    dic = {chr(i): 0 for i in range(97, 123)}

    # count all char occurrence in s
    for char in s:
        dic[char] += 1

    # find the first char that has only 1 count in the list and retrun its index.
    # If not found return -1.
    for i, char in enumerate(s):
        if dic[char] == 1:
            return i
            break
    else:
        return -1


if __name__ == '__main__':
    print(firstUniqChar("leetcode")) # 0
    print(firstUniqChar("loveleetcode")) # 2
    print(firstUniqChar("aabb")) # -1
