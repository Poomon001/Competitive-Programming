# runtime: O(n), memory: O(1)
def bitRotationLeft_32bit_M1(num: int, position: int):
    temp = num
    for _ in range(0, position):
        mask = temp & 2**31
        temp = (temp  << 1 | mask >> 31)
        print(bin(temp))
    return temp

# runtime: O(1), memory: O(1)
def bitRotationLeft_32bit_M2(num: int, position: int):
    shift = 32 - position
    mask = num & 2**shift
    temp = num << position
    num = (temp | mask >> shift)

    return num




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+=== Solution M1 ===+\n")
    print(bitRotationLeft_32bit_M1(183, 1))  # 336 => 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0001 0110 1110
    print(bitRotationLeft_32bit_M1(183, 2))  # 732 => 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0010 1101 1100
    print(bitRotationLeft_32bit_M1(183, 3))  # 1464 => 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0101 1011 1000
    print(bitRotationLeft_32bit_M1(4026531847, 0)) # 4026531847
    print(bitRotationLeft_32bit_M1(4026531847, 1)) # 8053063695
    print(bitRotationLeft_32bit_M1(4026531847, 2)) # 16106127391
    print(bitRotationLeft_32bit_M1(4026531847, 3)) # 32212254783

    print("\n+=== Solution M2 ===+\n")
    print(bitRotationLeft_32bit_M2(183, 1))  # 336 => 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0001 0110 1110
    print(bitRotationLeft_32bit_M2(183, 2))  # 732 => 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0010 1101 1100
    print(bitRotationLeft_32bit_M2(183, 3))  # 1464 => 0000 0000 0000 0000 0000 0000 1011 0111 -> 0000 0000 0000 0000 0000 0101 1011 1000
    print(bitRotationLeft_32bit_M2(4026531847, 0))  # 4026531847
    print(bitRotationLeft_32bit_M2(4026531847, 1))  # 8053063695
    print(bitRotationLeft_32bit_M2(4026531847, 2))  # 16106127391
    print(bitRotationLeft_32bit_M2(4026531847, 3))  # 32212254783
