from collections import deque

'''
    Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
    Purpose: Find an answer string after removing all 2 adjacent duplicates
    parameter: str s - a string of lower case alphabets
    return: str - the final string after all such duplicate removals
    Pre-Condition: 1 <= s.length <= 10^5
                 : s only contains lower case English letters.
    Post-Condition: none
'''
# brute force: runtime - O(n^3), memory - O(1)
def removeDuplicates_M1(s: str) -> str:
    # loop n times, each time remove one pair of adjacent duplicate
    length = len(s)
    temp = s
    for _ in range(length):
        i = 0
        j = 1
        if len(s) <= 1:
            return s
        while j < len(s):
            if s[i] == s[j]:
                temp = s[:i] + s[j + 1:]
                break
            j += 1
            i += 1

        s = temp

    return s

'''
    Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
    Purpose: Find an answer string after removing all 2 adjacent duplicates
    parameter: str s - a string of lower case alphabets
    return: str - the final string after all such duplicate removals
    Pre-Condition: 1 <= s.length <= 10^5
                 : s only contains lower case English letters.
    Post-Condition: none
'''
# stack: runtime - O(n), memory - O(n)
def removeDuplicates_M2(s: str) -> str:
    stack = deque()
    length = len(s)
    ans = ""

    for i in range(length):
        curr = s[i]
        prev = ''
        if stack:
            prev = stack[-1]

        if prev == curr:
            # find a adjacent duplicate: remove both
            stack.pop()
        else:
            # not a adjacent duplicate: add to stack
            stack.append(curr)

    while stack:
        ans += stack.pop()

    return ans[::-1]

if __name__ == "__main__":
    print("\n+=== solution 1 ===+\n")
    print(removeDuplicates_M1("aabbabba")) # "'
    print(removeDuplicates_M1("a")) # a
    print(removeDuplicates_M1("aaaaaaaaaaa")) # a
    print(removeDuplicates_M1("azxxzy")) # ay
    print(removeDuplicates_M1("aba")) # aba
    print(removeDuplicates_M1("abbaca")) # ca
    print(removeDuplicates_M1("abcdefghij")) # abcdefghij

    print("\n+=== solution 2 ===+\n")
    print(removeDuplicates_M2("aabbabba")) # ""
    print(removeDuplicates_M2("a")) # a
    print(removeDuplicates_M2("aaaaaaaaaaa")) # a
    print(removeDuplicates_M2("azxxzy")) # ay
    print(removeDuplicates_M2("aba")) # aba
    print(removeDuplicates_M2("abbaca")) # ca
    print(removeDuplicates_M2("abcdefghij")) # abcdefghij
