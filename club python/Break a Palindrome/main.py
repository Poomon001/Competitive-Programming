from typing import List

'''
    Link: https://leetcode.com/problems/break-a-palindrome/
    Purpose: replace exactly one character with any lowercase English letter so that the resulting 
             string is not a palindrome and that it is the lexicographically smallest
    Parameter: string palindrome - a palindrome string
    Returns: string - a string that is not a palindrome with the lexicographically smallest
    Pre-Condition: 1 <= palindrome.length <= 1000
            palindrome consists of only lowercase English letters.
    Post-Condition: none
'''

# brute force: O(n^2)
def breakPalindrome_M1(palindrome: str) -> str:
    result = ""
    # i represent index of each char in palindrome
    for i in range(0, len(palindrome)):
        # j represent a-z
        for j in range(97, 123):
            # try to break palindrome by replacing a-z on each char, index by index
            newWord = palindrome[:i] + chr(j) + palindrome[i + 1:]

            # if we find a newWord that is not palindrome, save it to result
            if not isPalindrome(newWord):
                # handle lexicographically smallest
                if (result == ""):
                    result = newWord
                elif (result > newWord):
                    result = newWord

    return result

def isPalindrome(string: str) -> bool:
    reverse = string[::-1]
    return reverse == string


'''
    Link: https://leetcode.com/problems/break-a-palindrome/
    Purpose: replace exactly one character with any lowercase English letter so that the resulting 
             string is not a palindrome and that it is the lexicographically smallest
    Parameter: string palindrome - a palindrome string
    Returns: string - a string that is not a palindrome with the lexicographically smallest
    Pre-Condition: 1 <= palindrome.length <= 1000
            palindrome consists of only lowercase English letters.
    Post-Condition: runtime O(n)
'''

# logic - break palindrome using only "a" and "b": O(n)
def breakPalindrome_M2(palindrome: str) -> str:
    length = len(palindrome)

    # case 1: palindrome length is 1 then impossible to break
    if length == 1:
        return ""

    # case 2: at least one char is non-'a', then change the first non-'a' char to 'a' to break and get the lexicographically smallest
    for i in range(length):
        # pointer moving backward
        j = length - i - 1

        # changing middle element cannot break palindrome, skip
        if i == j:
            continue

        # other first non-'a' can be changed to 'a' to break palindrome and get the lexicographically smallest
        if palindrome[i] != 'a':
            palindrome = palindrome[:i] + 'a' + palindrome[i + 1:]
            return palindrome

    # case 3: all char are 'a', then change the last 'a' to 'b' to break and get the lexicographically smallest
    palindrome = palindrome[:length - 1] + 'b'
    return palindrome

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(" \n=== Solution 1 ===\n")
    print(breakPalindrome_M1("abccba"))
    print(breakPalindrome_M1("a"))
    print(breakPalindrome_M1("aa"))
    print(breakPalindrome_M1("aba"))

    print(" \n=== Solution 2 ===\n")

    print(breakPalindrome_M2("abccba"))
    print(breakPalindrome_M2("a"))
    print(breakPalindrome_M2("aa"))
    print(breakPalindrome_M2("aba"))
