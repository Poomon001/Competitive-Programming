public class PowerofTwo {
    public static void main(String[] args) {
        System.out.println(isPowerOfTwo(1)); // true
        System.out.println(isPowerOfTwo(16)); // true
        System.out.println(isPowerOfTwo(3)); // false
        System.out.println(isPowerOfTwo(0)); // false
        System.out.println(isPowerOfTwo(1073741825)); // false
        System.out.println(isPowerOfTwo(1024)); // true
        System.out.println(isPowerOfTwo(10)); // false
        System.out.println(isPowerOfTwo(2147483646)); // false
    }

    /**
     * Link: https://leetcode.com/problems/sqrtx/
     * Purpose: Determine if n is a power of two.
     * Parameters: int n - an integer
     * Returns: boolean - true id n is a power of 2. Otherwise false.
     * Pre-Condition: -2^31 <= n <= 2^31 - 1
     * Post-Condition : None
     **/
    // a loop method: O(log(n)), memory: (1)
    public static boolean isPowerOfTwo(int n) {
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
}
