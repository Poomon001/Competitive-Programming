'''
    Link: https://leetcode.com/problems/number-complement/
    Purpose: Find a complement of num.
           : The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's
           : in its binary representation
    parameter: int num - an integer
    return: int - a complement of num
    Pre-Condition: 1 <= num < 2^31
    Post-Condition: none
'''
# runtime: O(n) where n is a binary length of num, memory: O(1)
def findComplement(num: int) -> int:
    bNum = bin(num)[2:]
    complement = ""
    for n in bNum:
        if n == "1":
            complement += "0"
        else:
            complement += "1"

    return int(complement, 2)


if __name__ == '__main__':
    print(findComplement(5)) # 2 (5 => Ob 101, 2 => Ob 010)
    print(findComplement(2)) # 1 (2 => Ob 10, 1 => Ob 01)
    print(findComplement(1)) # 0 (1 => Ob 1, 0 => Ob 0)
    print(findComplement(100)) # 27 (100 => 1100100, 27 => 0011011)
    print(findComplement(27)) # 4 (27 => 11011, 4 => 100)
    print(findComplement(53)) # 10 (53 => 110101, 10 => 001010)



