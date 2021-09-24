public class TribonacciNumber {
    public static void main(String[] args) {
        System.out.println(" \n=== M1 ===\n");
        System.out.println(tribonacciNumber_M1(1));
        System.out.println(tribonacciNumber_M1(2));
        System.out.println(tribonacciNumber_M1(3));
        System.out.println(tribonacciNumber_M1(4));
        System.out.println(tribonacciNumber_M1(5));
        System.out.println(tribonacciNumber_M1(6));

        System.out.println(" \n=== M2 ===\n");

        System.out.println(tribonacciNumber_M2(1));
        System.out.println(tribonacciNumber_M2(2));
        System.out.println(tribonacciNumber_M2(3));
        System.out.println(tribonacciNumber_M2(4));
        System.out.println(tribonacciNumber_M2(5));
        System.out.println(tribonacciNumber_M2(6));
    }

    /*
     * Link: https://leetcode.com/problems/n-th-tribonacci-number/
     * Purpose: Find the value of the Tribonacci at num position
     *        : The Tribonacci sequence Tn is defined as follows:
     *        : T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
     * Parameters: int num - an integer number
     * Returns: int - a Tribonacci at at num position
     * Pre-Condition: 0 <= n <= 37
     * Post-Condition : None
     */

    // loop: O(n)
    public static int tribonacciNumber_M1(int num){
        int acc = 0;
        int[] sum = new int[num+3];

        // given by the question
        sum[0] = 0;
        sum[1] = 1;
        sum[2] = 1;

        // num is equal to the given
        if(num == 0){
            return 0;
        }else if(num == 1 || num ==2){
            return 1;
        }

        // from 3 or above
        for(int i = 3; i <= num; i++){
            acc = sum[i-3] + sum[i-2] + sum[i-1];
            sum[i] = acc;
        }
        return acc;
    }


    /*
     * Link: https://leetcode.com/problems/n-th-tribonacci-number/
     * Purpose: Find the value of the Tribonacci at num position
     *        : The Tribonacci sequence Tn is defined as follows:
     *        : T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
     * Parameters: int num - an integer number
     * Returns: int - a Tribonacci at at num position
     * Pre-Condition: 0 <= n <= 37
     * Post-Condition : None
     */
    // recursive: O(n)
    public static int tribonacciNumber_M2(int num){
        // base case
        if (num == 0){
            return 0;
        }
        if (num == 1 || num == 2){
            return 1;
        }

        // recursive call
        return tribonacciNumber_M2(num-1) + tribonacciNumber_M2(num-2) + tribonacciNumber_M2(num-3);
    }
}
