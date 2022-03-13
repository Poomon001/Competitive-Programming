public class PowerOfFour {
    public static void main(String[] args){
        System.out.println("\n+=== solution M1 ===+\n");
        System.out.println(isPowerOfFour_M1(0)); // false
        System.out.println(isPowerOfFour_M1(2)); // false
        System.out.println(isPowerOfFour_M1(-2)); // false
        System.out.println(isPowerOfFour_M1(-16)); // false
        System.out.println(isPowerOfFour_M1(-2147483648)); // false
        System.out.println(isPowerOfFour_M1(2147483647)); // false
        System.out.println(isPowerOfFour_M1(1)); // true
        System.out.println(isPowerOfFour_M1(4)); // true
        System.out.println(isPowerOfFour_M1(8)); // false
        System.out.println(isPowerOfFour_M1(16)); // true
        System.out.println(isPowerOfFour_M1(32)); // false
        System.out.println(isPowerOfFour_M1(64)); //true

        System.out.println("\n+=== solution M2 ===+\n");
        System.out.println(isPowerOfFour_M2(0)); // false
        System.out.println(isPowerOfFour_M2(2)); // false
        System.out.println(isPowerOfFour_M2(-2)); // false
        System.out.println(isPowerOfFour_M2(-16)); // false
        System.out.println(isPowerOfFour_M2(-2147483648)); // false
        System.out.println(isPowerOfFour_M2(2147483647)); // false
        System.out.println(isPowerOfFour_M2(1)); // true
        System.out.println(isPowerOfFour_M2(4)); // true
        System.out.println(isPowerOfFour_M2(8)); // false
        System.out.println(isPowerOfFour_M2(16)); // true
        System.out.println(isPowerOfFour_M2(32)); // false
        System.out.println(isPowerOfFour_M2(64)); //true
    }

    /**
     * Link: https://leetcode.com/problems/power-of-four/
     * Purpose:  Find if a given integer n a product of 4 power by some integer x (n == 4^x)?
     * Parameters: int n - an integer
     * Returns: boolean - true if n == 4^x. Otherwise false.
     * Pre-Condition: -2^31 <= n <= 2^31 - 1
     * Post-Condition : none
     **/
    // runtime: O(log(n)), memory: O(1)
    public static boolean isPowerOfFour_M1(int n) {
        while(n%4 == 0 && n >= 1){
            n /= 4;
        }
        return n==1;
    }

    /**
     * Link: https://leetcode.com/problems/power-of-four/
     * Purpose:  Find if a given integer n a product of 4 power by some integer x (n == 4^x)?
     * Parameters: int n - an integer
     * Returns: boolean - true if n == 4^x. Otherwise false.
     * Pre-Condition: -2^31 <= n <= 2^31 - 1
     * Post-Condition : none
     **/
    // runtime: O(1), memory: O(1)
    public static boolean isPowerOfFour_M2(int n) {
        if(n==1){
            return true;
        }

        // O(31) = O(1)
        for(int i = 0;i < 31; i++){
            // since 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 32, 2^5 = 64, ...
            // then 4^1 = 4, 4^2 = 16, 4^3 = 64, ...
            if(i%2==1){
                if((2 << i) == n){
                    return true;
                }
            }
        }
        return false;
    }

}
