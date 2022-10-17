'''
    Link: https://leetcode.com/problems/integer-to-roman/description/
    Purpose: Determine a numerical number to roman number
    parameter: int num - an integer
    return: str ans - a roman number
    Pre-Condition: 1 <= num <= 3999
    Post-Condition: none
'''
# math method: runtime - O(1), memory - O(1)
def intToRoman_m1(num: int) -> str:
    unit = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousand = ["", "M", "MM", "MMM"]

    return thousand[(num % 10000) // 1000] + hundred[(num % 1000) // 100] + ten[(num % 100) // 10] + unit[(num % 10)]

'''
    Link: https://leetcode.com/problems/integer-to-roman/description/
    Purpose: Determine a numerical number to roman number
    parameter: int num - an integer
    return: str ans - a roman number
    Pre-Condition: 1 <= num <= 3999
    Post-Condition: none
'''
# greedy method: runtime - O(1), memory - O(1)
def intToRoman_m2( num: int) -> str:
    dic = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
           900: "CM", 1000: "M"}
    li = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""

    # O(1)
    while num != 0:
        i = 0
        # O(1)
        while i < len(li):
            n = li[i]
            if num - n >= 0:
                ans = ans + str(dic[n])
                num = num - n
                break
            i += 1
    return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== solution1 ===+\n")
    print(intToRoman_m1(3)) # III
    print(intToRoman_m1(58)) # LVIII
    print(intToRoman_m1(199)) # CXCIX
    print(intToRoman_m1(2994)) # MMCMXCIV
    print(intToRoman_m1(3000)) # MMM

    print("\n+=== solution2 ===+\n")
    print(intToRoman_m2(3)) # III
    print(intToRoman_m2(58)) # LVIII
    print(intToRoman_m2(199)) # CXCIX
    print(intToRoman_m2(2994)) # MMCMXCIV
    print(intToRoman_m2(3000)) # MMM