from collections import deque

'''
     Link: https://leetcode.com/problems/reverse-only-letters/
     Purpose: reverse the string according to the following rules:
              1. All the characters that are not English letters remain in the same position.
              2. All the English letters (lowercase or uppercase) should be reversed.
     Parameter: string s - a string to be reversed 
     Returns: string - reveresd string according to the rules
    Pre-Condition: 1 <= s.length <= 100
                 : s consists of characters with ASCII values in the range [33, 122].
                 : s does not contain '\"' or '\\'.
    Post-Condition: none
'''
# two pointer: memory and runtime are O(n)
def reverseOnlyLetters_M1(s: str) -> str:
    l = 0
    r = len(s) - 1
    chars = [c for c in s]
    while l <= r:
        if chars[l].isalpha() and chars[r].isalpha():
            temp = chars[l]
            chars[l] = chars[r]
            chars[r] = temp
        elif(chars[l].isalpha()):
            r -= 1
            continue
        else:
            l += 1
            continue
        r -= 1
        l += 1
    return "".join(chars)


'''
     Link: https://leetcode.com/problems/reverse-only-letters/
     Purpose: reverse the string according to the following rules:
              1. All the characters that are not English letters remain in the same position.
              2. All the English letters (lowercase or uppercase) should be reversed.
     Parameter: string s - a string to be reversed 
     Returns: string - reveresd string according to the rules
    Pre-Condition: 1 <= s.length <= 100
                 : s consists of characters with ASCII values in the range [33, 122].
                 : s does not contain '\"' or '\\'.
    Post-Condition: none
'''
# stack: memory and runtime are O(n)
def reverseOnlyLetters_M2(s: str) -> str:
    reverseOnlyLetters = deque() # store only alphabet char
    result = ""

    # get all alphabet to stack
    for i in range(len(s)):
        if s[i].isalpha():
            reverseOnlyLetters.append(s[i])

    # insert special character back
    for i in range(len(s)):
        if s[i].isalpha():
            result += reverseOnlyLetters.pop()
        else:
            result += s[i]

    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === end M1 ===\n")
    print(reverseOnlyLetters_M1("ab-cd")) # dc-ba
    print(reverseOnlyLetters_M1("a-bC-dEf-ghIj")) # j-Ih-gfE-dCba
    print(reverseOnlyLetters_M1("Test1ng-Leet=code-Q!")) # Qedo1ct-eeLg=ntse-T!

    print("\n === end M2 ===")
    print(reverseOnlyLetters_M2("ab-cd")) # dc-ba
    print(reverseOnlyLetters_M2("a-bC-dEf-ghIj")) # j-Ih-gfE-dCba
    print(reverseOnlyLetters_M2("Test1ng-Leet=code-Q!")) # Qedo1ct-eeLg=ntse-T!


