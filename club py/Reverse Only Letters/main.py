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

# hashmap: memory and runtime are O(n)
def reverseOnlyLetters_M1(s: str) -> str:
    reverseOnlyLetters = ""
    nonEnglish = {} # non-alphabet:position
    result = ""

    # remove and get all non-alphabet char
    for i in range(len(s)):
        if not s[i].isalpha():
            nonEnglish[i] = s[i]
        else:
            reverseOnlyLetters += s[i]

    # reverse alphabet letter only
    reverseOnlyLetters = reverseOnlyLetters[::-1]

    # insert special character back
    i = 0
    for j in range(len(s)):
        if j in nonEnglish.keys():
            result = result + nonEnglish.get(j)
        else:
            result = result + reverseOnlyLetters[i]
            i += 1

    return result


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
    print(reverseOnlyLetters_M1("ab-cd"))
    print(reverseOnlyLetters_M1("a-bC-dEf-ghIj"))
    print(reverseOnlyLetters_M1("Test1ng-Leet=code-Q!"))
    print("\n === end M1 ===\n")
    print(reverseOnlyLetters_M2("ab-cd"))
    print(reverseOnlyLetters_M2("a-bC-dEf-ghIj"))
    print(reverseOnlyLetters_M2("Test1ng-Leet=code-Q!"))
    print("\n === end M2 ===")

