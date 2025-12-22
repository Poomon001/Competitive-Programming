import typing

'''
    Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Purpose: find the length of the longest substring without repeating characters.
    Parameter:  string s - a string
    return: int highestLength - length of the longest substring
    Pre-Condition: 0 <= s.length <= 5 * 104
                 :s consists of English letters, digits, symbols and spaces.
    Post-Condition: None
'''

# brute force: O(n^2log(n))
def lengthOfLongestSubstring_M1(s: str) -> int:
    # record highest length
    highestLength = 0

    # find each possible string with unique
    # go char by char [totle string will be len(s)]
    # eg: s = "poomon001$" -> "Po", "O", "Om", "Mon0", "On0", "N0", "0", "01$", "1$", "$"
    for i in range(len(s)):
        # substring with unique char
        string = ""
        for j in range(i, len(s)):
            if not s[j] in string:
                string = string + s[j]
            else:
                break

        # virtual aid to see each substring with unique char
        # print(string)

        # find the longest string in the list
        highestLength = max(len(string), highestLength)

    return highestLength


'''
    Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Purpose: find the length of the longest substring without repeating characters.
    Parameter:  string s - a string
    return: int highestLength - length of the longest substring
    Pre-Condition: 0 <= s.length <= 5 * 104
                 :s consists of English letters, digits, symbols and spaces.
    Post-Condition: runtime under O(n^2)
'''

# sliding window I: runtime - O(n), memory - (1)
def lengthOfLongestSubstring_M2(s: str) -> int:
    word = set()
    maxLength = 0

    # keep track of the current char index
    right = 0
    left = 0

    while (right < len(s)):
        if s[right] in word:
            # duplicated char is found, remove tail
            word.remove(s[left])
            left += 1
        else:
            # duplicated char is not found, add head
            word.add(s[right])
            right += 1

        maxLength = max(maxLength, right - left)

    return maxLength


'''
    Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Purpose: find the length of the longest substring without repeating characters.
    Parameter:  string s - a string
    return: int highestLength - length of the longest substring
    Pre-Condition: 0 <= s.length <= 5 * 104
                 :s consists of English letters, digits, symbols and spaces.
    Post-Condition: runtime under O(n^2)
'''

# sliding window II: runtime - O(n), memory - (1)
def lengthOfLongestSubstring_M3(s: str) -> int:
    word = set()
    maxLength = 0
    tail = 0

    for head in range(len(s)):
        while s[head] in word:
            word.remove(s[tail])
            tail += 1

        word.add(s[head])
        maxLength = max(maxLength, head - tail + 1)

    return maxLength


if __name__ == '__main__':
    print("=== finish M1 ===")
    print(lengthOfLongestSubstring_M1("abcabcbb"))  # 3 ("abc")
    print(lengthOfLongestSubstring_M1("aaaa"))  # 1 ("a")
    print(lengthOfLongestSubstring_M1("pwwkew"))  # 3 ("wke")
    print(lengthOfLongestSubstring_M1("poomon001$"))  # 4 ("mon0")
    print(lengthOfLongestSubstring_M1("abcdefg"))  # 7 ("abcdfg")
    print(lengthOfLongestSubstring_M1("abcddefg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M1("abcddedfg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M1("a b cddedfg"))  # 4 ("b cd")
    print(lengthOfLongestSubstring_M1("aab"))  # 2 ("ab")
    print(lengthOfLongestSubstring_M1("abb"))  # 2 ("ab")

    print("=== finish M2 ===")

    print(lengthOfLongestSubstring_M2("abcabcbb"))  # 3 ("abc")
    print(lengthOfLongestSubstring_M2("aaaa"))  # 1 ("a")
    print(lengthOfLongestSubstring_M2("pwwkew"))  # 3 ("wke")
    print(lengthOfLongestSubstring_M2("poomon001$"))  # 4 ("mon0")
    print(lengthOfLongestSubstring_M2("abcdefg"))  # 7 ("abcdfg")
    print(lengthOfLongestSubstring_M2("abcddefg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M2("abcddedfg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M2("a b cddedfg"))  # 4 ("b cd")
    print(lengthOfLongestSubstring_M2("aab"))  # 2 ("ab")
    print(lengthOfLongestSubstring_M2("abb"))  # 2 ("ab")

    print("=== finish M3 ===")

    print(lengthOfLongestSubstring_M3("abcabcbb"))  # 3 ("abc")
    print(lengthOfLongestSubstring_M3("aaaa"))  # 1 ("a")
    print(lengthOfLongestSubstring_M3("pwwkew"))  # 3 ("wke")
    print(lengthOfLongestSubstring_M3("poomon001$"))  # 4 ("mon0")
    print(lengthOfLongestSubstring_M3("abcdefg"))  # 7 ("abcdfg")
    print(lengthOfLongestSubstring_M3("abcddefg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M3("abcddedfg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M3("a b cddedfg"))  # 4 ("b cd")
    print(lengthOfLongestSubstring_M3("aab"))  # 2 ("ab")
    print(lengthOfLongestSubstring_M3("abb"))  # 2 ("ab")\

