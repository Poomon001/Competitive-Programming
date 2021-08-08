
''' given t as an input to find a string s to generate t'''

''' ex1: t = aaaaa, s = aaaaa, s' = ""
    ex2: t = aacaababc, s = :( , s' = cbbc
    ex3: t = ababacac bbcc, s = ababacac, s'= bbcc
    t = bbcc|bbcc
    t = bbb|bbb
'''
# 0. if the input is a(s) then we imidately return t
# 1. use a loop...in to remove all a charachalf of the string t after I removed aters in string t
# 2. slicing first half and second
# 3. compare first half and second half: if first == second then the out put will return second half
#                                      : if the first != second then no solution, we return the sad face ":("
# **4. if s' contain "a' then return ":("  --> very tricky because I did not realize that s' can contain a (contradict the problem precondition)

'''
    Link: https://codeforces.com/problemset/problem/1146/B
    Purpose :t=s+s′; t, s and s' are string.  given a string t. Find some s that could have used to generate t.
    Input: sting - contains alphabet characters
    Print: string - s
    Pre-Condition : the input string is not empty and lowercase
    Post-Condition: none
'''
def hateA(t):
    withoutA = ""
    isAllA = True
    for char in t:
        # remove A from t
        if char != "a":
            isAllA = False
            withoutA += char

    index = len(withoutA) // 2
    first = withoutA[0:index] #s'
    second = withoutA[index:] #s'

    # if all a
    if isAllA:
        return t

    # if withoutA not even then return :(
    # because if left and right must match then it must be str*2 = even # of char
    if len(withoutA) % 2 == 1:
        return ":("

    # Check if s' contain "a".
    # We cannot check this directly eg. baba => ba|ba, s = ba, s' = ba therefore invalid = :(
    # but we can check it indirectly by seeing if the s' from t equal to the proper answer (second) or not
    # (proper answer <second> will contain no a) and the correct answer will show that s' of t == second
    # if s' of t (len(second) from the end of t) equals to <second>? nothing : :(
    if not t[len(t) - len(second):] == second:
        return ":("

    # compare first and second half: if equal the return t - first half otherwise return :(
    if first == second:
        return t[0:len(t) - len(first)]
    else:
        return ":("

input = input()
print(hateA(input))

# bcabca ---> bc|bc --> bc == bc then return bab incorrect
# ba|ba ---> baba --> :( because there is a in s' where s' is a string that should not contain a
# t = s + s'
