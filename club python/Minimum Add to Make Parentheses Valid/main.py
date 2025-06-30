from typing import List
from collections import deque
'''     
    Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
    Purpose: Find the minimum number of insertion to make parentheses valid.
    Parameter: str s - a string of parentheses
    Returns: int - a number of insertion to make valid parentheses
    Pre-Condition: 1 <= s.length <= 1000
                 : s[i] is either '(' or ')'.
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def minAddToMakeValid(s: str) -> int:
    stack = deque()
    counter = 0
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                counter += 1
                continue

            if stack[-1] == '(':
                stack.pop()
            else:
                counter += 1
    return counter + len(stack)


if __name__ == '__main__':
    print(minAddToMakeValid("(((")) # 3
    print(minAddToMakeValid("())")) # 1
    print(minAddToMakeValid("())((")) # 3
    print(minAddToMakeValid("))((")) # 4
    print(minAddToMakeValid("())(()))")) # 2
    print(minAddToMakeValid("()(())")) # 0

