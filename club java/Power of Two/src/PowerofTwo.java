public class PowerofTwo {
    public static void main(String[] args) {
        System.out.println("\n+===== M1 =====+\n");
        System.out.println(isPowerOfTwo_M1(1)); // true
        System.out.println(isPowerOfTwo_M1(16)); // true
        System.out.println(isPowerOfTwo_M1(3)); // false
        System.out.println(isPowerOfTwo_M1(0)); // false
        System.out.println(isPowerOfTwo_M1(1073741825)); // false
        System.out.println(isPowerOfTwo_M1(1024)); // true
        System.out.println(isPowerOfTwo_M1(10)); // false
        System.out.println(isPowerOfTwo_M1(2147483646)); // false

        System.out.println("\n+===== M2 =====+\n");
        System.out.println(isPowerOfTwo_M2(1)); // true
        System.out.println(isPowerOfTwo_M2(16)); // true
        System.out.println(isPowerOfTwo_M2(3)); // false
        System.out.println(isPowerOfTwo_M2(0)); // false
        System.out.println(isPowerOfTwo_M2(1073741825)); // false
        System.out.println(isPowerOfTwo_M2(1024)); // true
        System.out.println(isPowerOfTwo_M2(10)); // false
        System.out.println(isPowerOfTwo_M2(2147483646)); // false
    }

    /**
     * Link: https://leetcode.com/problems/sqrtx/
     * Purpose: Determine if n is a power of two.
     * Parameters: int n - an integer
     * Returns: boolean - true id n is a power of 2. Otherwise false.
     * Pre-Condition: -2^31 <= n <= 2^31 - 1
     * Post-Condition : None
     **/
    // a loop method: runtime: O(log(n)), memory: (1)
    public static boolean isPowerOfTwo_M1(int n) {
        long number = 1;

        // multiply number by 2 until it is or over the answer
        while(number <= n){
            if(n == number){
                return true;
            }
            number = number * 2;
        }
        return false;
    }

    /**
     * Link: https://leetcode.com/problems/sqrtx/
     * Purpose: Determine if n is a power of two.
     * Parameters: int n - an integer
     * Returns: boolean - true id n is a power of 2. Otherwise false.
     * Pre-Condition: -2^31 <= n <= 2^31 - 1
     * Post-Condition : None
     **/
    // bit manipulation: runtime: O(1), memory: O(1)
    public static boolean isPowerOfTwo_M2(int n) {
        // if n is a number that is powered by 2 then bit representation of n contains only one 1 "0b 100...0"
        // Check if bits of n contains only one 1 by doing AND operation between n and n-1
        // if n bit contains contains only one 1, then n-1 will has one less digits and all digits will be 1
        // eg n = 4: Ob 1000  then n - 1: Ob 0111
        return n > 0 && (n & (n-1)) == 0?true:false;
    }
}

