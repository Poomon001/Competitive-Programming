from collections import deque

'''
    Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
    Purpose: Find an answer string after removing all k number of adjacent duplicates
    parameter: str s - a string of lower case alphabets
             : int k - an integer 
    return: str - the final string after all such duplicate removals
    Pre-Condition: 1 <= s.length <= 10^5
                 : 2 <= k <= 104^
                 : s only contains lower case English letters.
    Post-Condition: none
'''
# stack: runtime - O(n), memory - O(n)
def removeDuplicates(s: str, k: int) -> str:
    # [char, count]
    stack = deque()
    ans = ""
    for char in s:
        curr = [char, 1]
        prev = ['', 0]

        if stack:
            prev = stack[-1]

        # if the adjacent a duplicate
        if prev[0] == curr[0]:
            # increase the count of the duplicate
            curr = [prev[0], prev[1] + 1]
            stack.pop()
            if curr[1] != k:
                stack.append(curr)
        else:
            stack.append(curr)

    # print
    while stack:
        item = stack.pop()
        ans += item[0] * item[1]

    return ans[::-1]

if __name__ == "__main__":
    print(removeDuplicates("abcd", 2)) # abcd
    print(removeDuplicates("deeedbbcccbdaa", 3)) # aa
    print(removeDuplicates("pbbcggttciiippooaais", 2)) # pa
    print(removeDuplicates("pbbcggttciiippooaais", 3)) # pbbcggttcppooaais
    print(removeDuplicates("ppppp", 5)) # ""
    print(removeDuplicates("p", 2)) # p
