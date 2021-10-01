'''
    Link: https://leetcode.com/problems/excel-sheet-column-number/
    Purpose: Find the corresponding Excel column number
    parameter: str columnTitle - a string contains uppercase alphabet(s)
    return: int answer - its corresponding column number
    Pre-Condition: 1 <= columnTitle.length <= 7
                 : columnTitle consists only of uppercase English letters.
                 : columnTitle is in the range ["A", "FXSHRXW"].
    Post-Condition: none
'''

# This is a simple question asking to convert base 26 to base 10
# The formula is base10 = "(26^0 x d1) + (26^1 x d2) + ... + (26^(n-1) x dn)"

# run-time: O(n), memory: O(1)
def titleToNumber(columnTitle: str) -> int:
    # index represent n-1
    index = len(columnTitle) - 1
    answer = 0
    for char in columnTitle:
        # convert alphabet to number (represend dn)
        number = ord(char) - 64

        # from the formula
        answer += (26**index) * number
        index -= 1

    return answer

if __name__ == '__main__':
    print(titleToNumber("A")) # 1
    print(titleToNumber("B")) # 2
    print(titleToNumber("AB")) # 28
    print(titleToNumber("ZY")) # 701
    print(titleToNumber("FXSHRXW")) # 2147483647