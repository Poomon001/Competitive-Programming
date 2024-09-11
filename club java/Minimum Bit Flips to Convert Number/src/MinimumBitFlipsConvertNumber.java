public class MinimumBitFlipsConvertNumber {
    public static void main(String[] args) {
        System.out.println("\n === solution 1 === \n");
        System.out.println(minBitFlips_M1(10, 7)); // 3
        System.out.println(minBitFlips_M1(10, 10)); // 0
        System.out.println(minBitFlips_M1(7, 10)); // 3
        System.out.println(minBitFlips_M1(0, 0)); // 0
        System.out.println(minBitFlips_M1(0, 111)); // 6
        System.out.println(minBitFlips_M1(12345, 1001011)); // 11
        System.out.println(minBitFlips_M1(1000000000, 9)); // 15
        System.out.println(minBitFlips_M1(4, 3)); // 3

        System.out.println("\n === solution 2 === \n");
        System.out.println(minBitFlips_M2(10, 7)); // 3
        System.out.println(minBitFlips_M2(10, 10)); // 0
        System.out.println(minBitFlips_M2(7, 10)); // 3
        System.out.println(minBitFlips_M2(0, 0)); // 0
        System.out.println(minBitFlips_M2(0, 111)); // 6
        System.out.println(minBitFlips_M2(12345, 1001011)); // 11
        System.out.println(minBitFlips_M2(1000000000, 9)); // 15
        System.out.println(minBitFlips_M2(4, 3)); // 3
    }

    /**
     Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number
     Purpose: Find the minimum number of bit flips to convert start to goal
     parameter: int start - an integer
              : int goal - an integer
     return: int counting: the minimum number of bit flips to convert start to goal.
     Pre-Condition: 0 <= start, goal <= 10^9
     Post-Condition: none
     **/
    // Bit Mask Comparison - runtime: O(logn), memory: O(1)
    public static int minBitFlips_M1(int start, int goal) {
            int counting = 0;
            for(int i = 0; i < 32; i++) {
                int startBit = (start >> i) & 1;
                int goalBit = (goal >> i) & 1;
                if(startBit != goalBit) {
                    counting++;
                }
            }
            return counting;
    }

    /**
     Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number
     Purpose: Find the minimum number of bit flips to convert start to goal
     parameter: int start - an integer
     : int goal - an integer
     return: int counting: the minimum number of bit flips to convert start to goal.
     Pre-Condition: 0 <= start, goal <= 10^9
     Post-Condition: none
     **/
    // XOR - runtime: O(logn), memory: O(1)
    public static int minBitFlips_M2(int start, int goal) {
        int diffBits = start ^ goal;
        int counting = 0;
        while(diffBits > 0) {
            if((diffBits & 1) == 1) {
                counting++;
            }
            diffBits >>= 1;
        }
        return counting;
    }
}
