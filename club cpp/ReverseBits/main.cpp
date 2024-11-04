#include <iostream>
#include <bitset>


/**
     Link: https://leetcode.com/problems/reverse-bits/
     Purpose: Reverse bits of a given 32 bits unsigned integer.
     parameter: uint32_t n - a 32 bit unsigned integer
     return: uint32_t ans - the reverse of 32 bit unsigned integer
     Pre-Condition: The input must be a binary string of length 32
     Post-Condition: none
**/

// Add by value like 2 ^ x to ans - runtime: O(1), memory: O(1)
uint32_t reverseBits_M1(uint32_t n) {
    uint32_t ans = 0;

    // 0 to 31 will be considered for unit32_t bit
    for(int i = 0; i < 32; i++) {
        uint32_t j = 31 - i; // 31 to 0
        uint32_t bitmask = 1 & n;
        ans = ans + (bitmask << j);
        n = n >> 1;
    }
    return ans;
}

/**
     Link: https://leetcode.com/problems/reverse-bits/
     Purpose: Reverse bits of a given 32 bits unsigned integer.
     parameter: uint32_t n - a 32 bit unsigned integer
     return: uint32_t ans - the reverse of 32 bit unsigned integer
     Pre-Condition: The input must be a binary string of length 32
     Post-Condition: none
**/
// Add by bit like last bit to ans - runtime: O(1), memory: O(1)
uint32_t reverseBits_M2(uint32_t n) {
    uint32_t ans = 0;

    // 0 to 31 will be considered for unit32_t bit
    for(int i = 0; i < 32; i++) {
        ans = ans << 1;
        ans = ans | (1 & n);
        n = n >> 1;
    }
    return ans;
}



int main() {
    std::cout << "\n === Solution 1 === \n" << std::endl;
    std::cout << reverseBits_M1(0b1101) << std::endl; // 0b 1011 0000 0000 0000 0000 0000 0000 0000 = 2952790016
    std::cout << reverseBits_M1(0b10110000000000000000000000000000) << std::endl; // 0b 1101 = 13
    std::cout << reverseBits_M1(0b00000010100101000001111010011100) << std::endl; // 0b 0011 1001 0111 1000 0010 1001 0100 0000 = 964176192
    std::cout << reverseBits_M1(0b11111111111111111111111111111101) << std::endl; // 0b 1011 1111 1111 1111 1111 1111 1111 1111 = 3221225471

    std::cout << "\n === Solution 2 === \n" << std::endl;
    std::cout << reverseBits_M2(0b1101) << std::endl; // 0b 1011 0000 0000 0000 0000 0000 0000 0000 = 2952790016
    std::cout << reverseBits_M2(0b10110000000000000000000000000000) << std::endl; // 0b 1101 = 13
    std::cout << reverseBits_M2(0b00000010100101000001111010011100) << std::endl; // 0b 0011 1001 0111 1000 0010 1001 0100 0000 = 964176192
    std::cout << reverseBits_M2(0b11111111111111111111111111111101) << std::endl; // 0b 1011 1111 1111 1111 1111 1111 1111 1111 = 3221225471
    return 0;
}
