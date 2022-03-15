from collections import deque
'''
    Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    Purpose: Given a string s of '(' , ')' and lowercase English characters.
           : Find a valid parenthesis string. Valid if and only if:
           : It is the empty string, contains only lowercase characters, or
           : It can be written as AB (A concatenated with B), where A and B are valid strings, or
           : It can be written as (A), where A is a valid string.
    parameter: str s - a string 
    return: str answer - a valid parenthesis string
    Pre-Condition: 1 <= s.length <= 10^5
                 : s[i] is either'(' , ')', or lowercase English letter.
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def minRemoveToMakeValid(s: str) -> str:
    stack = deque()

    prefix = 0  # keep track of an open parenthesis
    suffix = 0  # keep track of a close parenthesis

    answer = ""

    # filter close parenthesis: make sure that all "closes" pair with "opens"
    for c in s:
        if c == "(":
            prefix += 1
            stack.append(c)
        elif c == ")":
            if prefix >= suffix + 1:
                suffix += 1
                stack.append(c)
        else:
            stack.append(c)

    # filter unpair open parenthesis: : make sure that all "opens" pair with "closes"
    while stack:
        c = stack.pop()
        if c == "(" and prefix != suffix:
            # found unpair an "open", ignore it
            prefix -= 1
        else:
            answer = c + answer

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minRemoveToMakeValid("abc(t(c)x)yz)")) # abc(t(c)x)yz
    print(minRemoveToMakeValid("a(bc(t(c)x)yz)")) # a(bc(t(c)x)yz)
    print(minRemoveToMakeValid("(a(bc(t(c)x)yz)")) # (a(bc(tc)x)yz)
    print(minRemoveToMakeValid("a)b(c)d")) # ab(c)d
    print(minRemoveToMakeValid("()()")) # ()()
    print(minRemoveToMakeValid("))((")) #
    print(minRemoveToMakeValid("())()(((")) # ()()
    print(minRemoveToMakeValid("foobar")) # foobar
