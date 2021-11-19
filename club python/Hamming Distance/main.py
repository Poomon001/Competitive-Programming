# runtime: O(n), memory: O(1) where n is max(len(bin(x), len(bin(y)))
def hammingDistance(x: int, y: int) -> int:
    # perform exclusive OR: 0 XOR 1 => 1, 1 XOR 1 => 1, otherwise => 0
    EOR = x^y

    # convert EOR (decimal) to (binary)
    binaryEOR = bin(EOR)
    count = 0

    # count 1
    for bit in binaryEOR:
        if bit == "1":
            count += 1

    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(hammingDistance(1,4)) # Ob 0001 and Ob 0100 => 2
    print(hammingDistance(3, 1)) # Ob 0011 and Ob 0001 => 1
    print(hammingDistance(3, 11)) # Ob 0011 and Ob 1011 => 1
    print(hammingDistance(34321, 1111)) # Ob 1000 0110 0001 0001 and Ob 0100 0101 0111 => 5

