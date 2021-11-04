public class uglyNumber {
    public static void main(String[] args){
        System.out.println(isUgly(6)); // true
        System.out.println(isUgly(8)); // true
        System.out.println(isUgly(14)); // false
        System.out.println(isUgly(5)); // true
        System.out.println(isUgly(2)); // true
        System.out.println(isUgly(3)); // true
        System.out.println(isUgly(1)); // true
        System.out.println(isUgly(0)); // false
        System.out.println(isUgly(-2)); // false
    }


    /**
     * Link: https://leetcode.com/problems/ugly-number/
     * Purpose: Determine if a positive integer whose prime factors are limited to 2, 3, and 5.
     * Parameters: int n - an integer
     * Returns: boolean - true if all prime factors of n are 2,3, or 5. Otherwise, false.
     * Pre-Condition : -231 <= n <= 231 - 1
     * Post-Condition  : none
     **/
    // runtime: O(n), memory: O(1)
    public static boolean isUgly(int n) {
        // catch all non positive number
        if(n < 1){
            return false;
        }

        // try to keep dividing n by 2,3, and 5. if not possible return false.
        while(n != 1){
            if(n%5 == 0){
                n /= 5;
            }else if(n%3==0){
                n /= 3;
            }else if(n%2==0){
                n /= 2;
            }else{
                return false;
            }
        }
        return true;
    }
}
