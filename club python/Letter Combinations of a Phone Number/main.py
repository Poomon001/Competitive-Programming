from typing import List

digit_to_char_list = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'i', 'h'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']
}

'''
    Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
    Purpose: Given a string containing digits from 2-9 inclusive, 
           : find all possible letter combinations that the number could represent.
    parameter: str digits - a string of digits
    return: List[int] answers - all possible letter combinations that the number could represent.
    Pre-Condition: 0 <= digits.length <= 4
                 : digits[i] is a digit in the range ['2', '9']
    Post-Condition: none
'''
# recursive: runtime: O(4^n), memory: O(4^n)
def letterCombinations_M1(digits: str) -> List[str]:
    # digits = '23'
    #                           []
    #       [a]                [b]               [c]
    # [[ad] [ae] [af]     [bd] [be] [bf]     [cd] [ce] [cf]]

    answers = []
    if digits == "":
        return answers

    def backtracking(n, answer):
        if n == len(digits):
            answers.append("".join(answer))
            return

        for c in digit_to_char_list[digits[n]]:
            answer.append(c)
            backtracking(n + 1, answer)
            answer.pop()

    backtracking(0, [])
    return answers

'''
    Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
    Purpose: Given a string containing digits from 2-9 inclusive, 
           : find all possible letter combinations that the number could represent.
    parameter: str digits - a string of digits
    return: List[int] answers - all possible letter combinations that the number could represent.
    Pre-Condition: 0 <= digits.length <= 4
                 : digits[i] is a digit in the range ['2', '9']
    Post-Condition: none
'''
# iteration: runtime: O(4^n), memory: O(4^n)
def letterCombinations_M2(digits: str) -> List[str]:
    # 23
    # [[a], [b], [c]]
    # [[ad], [ae], [af], ...]
    if digits == "":
        return []

    answers = [""]

    for digit in digits:
        char_list = digit_to_char_list[digit]
        n = len(answers)
        new_answers = []

        for i in range(n):
            for c in char_list:
                new_answers.append(answers[i] + c)
        answers = new_answers
    return answers

'''
    Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number
    Purpose: Given a string containing digits from 2-9 inclusive, 
           : find all possible letter combinations that the number could represent.
    parameter: str digits - a string of digits
    return: List[int] answers - all possible letter combinations that the number could represent.
    Pre-Condition: 0 <= digits.length <= 4
                 : digits[i] is a digit in the range ['2', '9']
    Post-Condition: none
'''
# post-filtering + iteration: runtime: O(4^n), memory: O(4^n)
def letterCombinations_M3(digits: str) -> List[str]:
    # 23
    # [[a], [b], [c]]
    # [[ad], [ae], [af], ...]
    if digits == "":
        return []

    answers = [""]

    for digit in digits:
        char_list = digit_to_char_list[digit]
        n = len(answers)

        for i in range(n):
            for c in char_list:
                answer = answers[i]
                answer += c
                answers.append(answer)

    return [answer for answer in answers if len(answer) == len(digits)]


if __name__ == '__main__':
    print("\n === solution 1 === \n")
    print(letterCombinations_M1(""))  # []
    print(letterCombinations_M1("2"))  # ['a', 'b', 'c']
    print(letterCombinations_M1("23"))  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print(letterCombinations_M1("239"))  # ['adw', 'adx', 'ady', 'adz', 'aew', 'aex', 'aey', 'aez', 'afw', 'afx', 'afy', 'afz', 'bdw', 'bdx', 'bdy', 'bdz', 'bew', 'bex', 'bey', 'bez', 'bfw', 'bfx', 'bfy', 'bfz', 'cdw', 'cdx', 'cdy', 'cdz', 'cew', 'cex', 'cey', 'cez', 'cfw', 'cfx', 'cfy', 'cfz']

    print("\n === solution 2 === \n")
    print(letterCombinations_M2(""))  # []
    print(letterCombinations_M2("2"))  # ['a', 'b', 'c']
    print(letterCombinations_M2("23"))  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print(letterCombinations_M2("239"))  # ['adw', 'adx', 'ady', 'adz', 'aew', 'aex', 'aey', 'aez', 'afw', 'afx', 'afy', 'afz', 'bdw', 'bdx', 'bdy', 'bdz', 'bew', 'bex', 'bey', 'bez', 'bfw', 'bfx', 'bfy', 'bfz', 'cdw', 'cdx', 'cdy', 'cdz', 'cew', 'cex', 'cey', 'cez', 'cfw', 'cfx', 'cfy', 'cfz']

    print("\n === solution 3 === \n")
    print(letterCombinations_M3("")) # []
    print(letterCombinations_M3("2")) # ['a', 'b', 'c']
    print(letterCombinations_M3("23")) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print(letterCombinations_M3("239")) # ['adw', 'adx', 'ady', 'adz', 'aew', 'aex', 'aey', 'aez', 'afw', 'afx', 'afy', 'afz', 'bdw', 'bdx', 'bdy', 'bdz', 'bew', 'bex', 'bey', 'bez', 'bfw', 'bfx', 'bfy', 'bfz', 'cdw', 'cdx', 'cdy', 'cdz', 'cew', 'cex', 'cey', 'cez', 'cfw', 'cfx', 'cfy', 'cfz']

