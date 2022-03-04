'''
 * Bit mask use & eg: 1100 1101 & 0000 0001 == 0000 0001
 * Bit union use | eg: 0011 0001 | 1000 0000 === 1011 0001
'''

# Delete the most significant bit (left-most), and add 0 at the least significant bit (right-most)
# move all bits to left
def bitShiftingLeft(num, amount):
    return num << amount

# Delete the least significant bit (right-most), and add 0 at the most significant bit (left-most)
# move all bits to right
def bitShiftingRight(num, amount):
    return num >> amount

# bit mask is to focus on a target bit by making other bit 0
# achieve bit mask by using &
# eg 1 : 0000 000X = num & 0000 0001 = num & 2^0 = 0000 000X
# eg 2 : 0000 00X0 = num & 0000 0010 = num & 2^1 = 0000 00X0
# eg 3 : 0000 0X00 = num & 0000 0100 = num & 2^2 = 0000 0X00
# eg 4 : 0000 0XXX = num & 0000 0111 = num & 7 = 0000 0XXX
def bitMask(num, positionFromRight):
    return num & 2**positionFromRight

# move the last bit mask to any offset position
# eg 1   : 0000 000X = (num & 0000 0001) << 0 = 0000 000X
# eg 2   : 0000 00X0 = (num & 0000 0001) << 1 = 0000 000X << 1 = 0000 00X0
# eg 3   : 0000 0X00 = (num & 0000 0001) << 2 = 0000 000X << 2 = 0000 0X00
# **eg 4 : X000 0000 = (num & 0000 0001) << len(bit_num) - 1 = (num & 0000 0001) << 8 - 1 = X000 0000
def bitMaskManipulation(num, offset):
    return (num & 1) << offset - 1

# bit right rotation is to remove right-most bit and put them on left-most
#        Given: 0011 0111, Expect: Ob(1001 1011)
# step - 1. bit mask to save the "one last right-most bit" (we will put it to the front left-most later)
#           0011 0111 => 0000 0001
#      - 2. move the "one last right-most bit" bit to the left-most by left bit shifting
#           0000 0001 => 1000 0000
#      - 3. move bit in temp by 1 to the right to make a space at the left-most for the "one last right-most bit"
#           0011 0111 => X001 1011
#      - 4. insert the "one last right-most bit" by bit union (|)
#           X001 1011 | 1000 0000 => Ob(1001 1011)
def bitRotationRight_32bit(num, position):
    temp = num
    for _ in range(0, position):
        mask = (temp & 1)
        temp = (temp >> 1) | (mask << 31)
    return temp

# bit left rotation is to remove left-most bit and put them on right-most
#        Given: 1011 0111, Expect: Ob(0110 1111)
# step - 1. bit mask to save the "one first left-most bit" (we will put it to the last right-most later)
#           1011 0111 => 1000 0000
#      - 2. move the "one first left-most bit" bit to the the right-most by right bit shifting
#           1000 0000 => 0100 0000 => 0010 0000 => ... => 0000 0001
#      - 3. move bit in temp by 1 to the left to make a space at the right-most for the "one first left-most bit"
#           1011 0111 => 0110 111X
#      - 4. insert the "one last right-most bit" by bit union (|)
#           0110 111X | 0000 0001 => Ob(0110 1111)
def bitRotationLeft_32bit(num, position):
    temp = num
    for _ in range(0, position):
        mask = (temp & 2**31)
        temp = (temp << 1 | mask >> 31)
    return temp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== Bit Shifting Left ===+\n")
    print(bitShiftingLeft(10, 1)) # 0000 1010 -> 0001 0100 = 20
    print(bitShiftingLeft(10, 2))  # 0000 1010 -> 0010 1000 = 40
    print(bitShiftingLeft(10, 3))  # 0000 1010 -> 0101 0000 = 80

    print("\n+=== Bit Shifting Right ===+\n")
    print(bitShiftingRight(10, 1))  # 0000 1010 -> 0000 0101 = 5
    print(bitShiftingRight(10, 2))  # 0000 1010 -> 0010 0010 = 2
    print(bitShiftingRight(10, 3))  # 0000 1010 -> 0000 0001 = 1

    print("\n+=== Bit Mask ===+\n")
    print(bitMask(55, 0))  # 0011 0111 & 2^0 -> 0000 000X -> 0000 0001 = 1
    print(bitMask(55, 1))  # 0011 0111 & 2^1 -> 0000 00X0 -> 0000 0010 = 2
    print(bitMask(55, 2))  # 0011 0111 & 2^2 -> 0000 0X00 -> 0000 0100 = 4
    print(bitMask(55, 6))  # 0011 0111 & 2^6 -> 0X00 0000 -> 0000 0000 = 0
    print(bitMask(55, 7))  # 0011 0111 & 2^7 -> X000 000X -> 0000 0000 = 0

    print("\n+=== Bit Mask Manipulation ===+\n")
    print(bitMaskManipulation(55, 1))  # (0011 0111 & 1) << 0 = 0000 0001 << 0 = 0000 0001 = 1
    print(bitMaskManipulation(55, 2))  # (0011 0111 & 1) << 1 = 0000 0001 << 1 = 0000 0010 = 2
    print(bitMaskManipulation(55, 3))  # (0011 0111 & 1) << 2 = 0000 0001 << 2 = 0000 0100 = 4
    print(bitMaskManipulation(55, 8))  # (0011 0111 & 1) << 7 = 0000 0001 << 7 = 1000 0000 = 128

    print("\n+=== Bit Right Rotation ===+\n")
    print(bitRotationRight_32bit(55, 1)) # 0000 0000 0000 0000 0000 0000 0011 0111 -> 1000 0000 0000 0000 0000 0000 0001 1011 = 2147483675
    print(bitRotationRight_32bit(55, 2))  # 0000 0000 0000 0000 0000 0000 0011 0111 -> 1100 0000 0000 0000 0000 0000 0000 1101 = 3221225485
    print(bitRotationRight_32bit(55, 3))  # 0000 0000 0000 0000 0000 0000 0011 0111 -> 1110 0000 0000 0000 0000 0000 0000 0110 = 3758096390

    print("\n+=== Bit Left Rotation ===+\n")
    print(bitRotationLeft_32bit(183, 1)) # 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0001 0110 1110
    print(bitRotationLeft_32bit(183, 2)) # 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0010 1101 1100
    print(bitRotationLeft_32bit(183, 3)) # 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0101 1011 1000

    print("\n+=== Find the max from all possible right rotation ===+\n")

    print("\n+=== Note bit manipulation: bit mask, bit union, bit shifting, and bit rotation on the book ===+\n")

