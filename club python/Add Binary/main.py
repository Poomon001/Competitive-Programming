'''
    Link: https://leetcode.com/problems/add-binary/
    Purpose: Find binary sum of two binary string
    parameter: str a - a binary string
             : str b - a binary string
    return: str -  a binary sum of a and b
    Pre-Condition: 1 <= a.length, b.length <= 104
                 : a and b consist only of '0' or '1' characters.
                 : Each string does not contain leading zeros except for the zero itself.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def addBinary_M1(a: str, b: str) -> str:
    # convert binary to decimal
    c = int(a, 2) + int(b, 2)

    # convert decimal to binary
    return (bin(c)[2:])

'''
    Link: https://leetcode.com/problems/add-binary/
    Purpose: Find binary sum of two binary string
    parameter: str a - a binary string
             : str b - a binary string
    return: str -  a binary sum of a and b
    Pre-Condition: 1 <= a.length, b.length <= 104
                 : a and b consist only of '0' or '1' characters.
                 : Each string does not contain leading zeros except for the zero itself.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def addBinary_M2(a: str, b: str) -> str:
    carrier = 0
    answer = ""

    # balance digit in a and b string
    if len(a) < len(b):
        a = "0"*(len(b) - len(a)) + a
    elif len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b

    # add a and b
    for i in range(len(a) - 1, -1, -1):
        A = int(a[i])
        B = int(b[i])

        if A + B + carrier == 0:
            answer = "0" + answer
            carrier = 0
        elif A + B + carrier == 1:
            answer = "1" + answer
            carrier = 0
        elif A + B + carrier == 2:
            answer = "0" + answer
            carrier = 1
        elif A + B + carrier == 3:
            answer = "1" + answer
            carrier = 1

    return answer if carrier == 0 else "1"+answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+==== M1 ====+\n")
    print(addBinary_M1("11", "1")) # 100
    print(addBinary_M1("1010", "1011")) # 10101
    print("\n+==== M2 ====+\n")
    print(addBinary_M2("11", "1"))  # 100
    print(addBinary_M2("1010", "1011"))  # 10101

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
