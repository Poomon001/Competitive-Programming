'''
    Link: https://leetcode.com/problemset/all/
    Purpose: Return the index of the first occurrence of second String in first string, or -1 if not part matches.
    parameter: string - first string
             : string - second string
    Print: int - the index of the first occurrence of second string in first string
    Pre-Condition : all strings are in lowercase
    Post-Condition: none
'''
def strStr(haystack: str, needle: str) -> int:
    # O(1)
    if (len(needle) == 0 and len(haystack) == 0):
        return 0

    # O(1)
    if (needle == haystack):
        return 0

    # O(n)
    if (not needle in haystack):
        return -1

    # O(n^2)
    for i in range(len(haystack) + 1):
        if (needle in haystack[:i]):
            return (i - len(needle))

print(strStr("hello", "ll"))
print(strStr("",""))
print(strStr("l","l"))
print(strStr("sfdds", ""))
print(strStr("", "fsdf"))