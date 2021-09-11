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
def lengthOfLongestSubstring_M1(s:str) -> int:
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
# hashmap: O(2n)
def lengthOfLongestSubstring_M2(s:str) -> int:
    # pointer expanding the window
    curr = 0

    # pointer at front of the unique list of char
    front = 0

    # record highest length
    highestLength = 0

    # hashmap keep track of char
    mapChar = []

    while(curr < len(s)):
        # keep moving front pointer up and removing front char from hashmap
        # then repeat the loop to check if hashmap still contain duplicate char
        # eg: s = "poomon001$" -> "po", (remove p,o) "om", (remove o) "mon0", (remove m, o, n, 0) "01$"
        if s[curr] in mapChar:
            # remove first char in hashmap
            mapChar.remove(s[front])

            # move the front pointer to the next char
            front += 1

        # add new char to the hashmap, set current pointer to the nexr char, and update the max length
        else:
            # add a new char to hashmap
            mapChar.append(s[curr])

            # move expanding window pointer to the next char
            curr += 1

            # find the max lenght
            highestLength = max(highestLength, len(mapChar))

    return highestLength


if __name__ == '__main__':
    print(lengthOfLongestSubstring_M1("abcabcbb")) # 3 ("abc")
    print(lengthOfLongestSubstring_M1("aaaa")) # 1 ("a")
    print(lengthOfLongestSubstring_M1("pwwkew")) # 3 ("wke")
    print(lengthOfLongestSubstring_M1("poomon001$")) # 4 ("mon0")
    print(lengthOfLongestSubstring_M1("abcdefg"))  # 7 ("abcdfg")
    print(lengthOfLongestSubstring_M1("abcddefg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M1("abcddedfg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M1("a b cddedfg"))  # 4 ("b cd")
    print(lengthOfLongestSubstring_M1("aab"))  # 2 ("ab")
    print(lengthOfLongestSubstring_M1("abb"))  # 2 ("ab")

    print("=== finish M1 ===")

    print(lengthOfLongestSubstring_M2("abcabcbb")) # 3 ("abc")
    print(lengthOfLongestSubstring_M2("aaaa")) # 1 ("a")
    print(lengthOfLongestSubstring_M2("pwwkew")) # 3 ("wke")
    print(lengthOfLongestSubstring_M2("poomon001$")) # 4 ("mon0")
    print(lengthOfLongestSubstring_M2("abcdefg"))  # 7 ("abcdfg")
    print(lengthOfLongestSubstring_M2("abcddefg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M2("abcddedfg"))  # 4 ("abcd")
    print(lengthOfLongestSubstring_M2("a b cddedfg"))  # 4 ("b cd")
    print(lengthOfLongestSubstring_M2("aab"))  # 2 ("ab")
    print(lengthOfLongestSubstring_M2("abb"))  # 2 ("ab")

    print("=== finish M2 ===")