public class ValidPerfectSquare {
    public static void main(String args[]){
        System.out.println(isPerfectSquare(1)); // true
        System.out.println(isPerfectSquare(2)); // false
        System.out.println(isPerfectSquare(14)); // false
        System.out.println(isPerfectSquare(16)); // true
        System.out.println(isPerfectSquare(25)); // true
        System.out.println(isPerfectSquare(808201)); // true
    }

    /*
     * Link: https://leetcode.com/problems/valid-perfect-square/
     * Purpose: Given a positive integer num, Find if num is a perfect square.
     *        : Perfect square is x * x = num where x is an integer
     * Parameters: int num - a number
     * Returns: boolean - true if num is a perfect square or false otherwise.
     * Pre-Condition: 1 <= num <= 2^31 - 1
     * Post-Condition: None
     */

    // binary search - runtime: O(log(n)), memory: O(1)
    public static boolean isPerfectSquare(int num) {
        int half = (num + 1) / 2;

        // since it is sorted from 1 to half, use binary search
        long front = 1;
        long back = half;
        long middle = front + (back - front)/2;

        while(front <= back) {
            long pow = middle * middle;
            if(pow == num){
                return true;
            }

            if(pow < num) {
                front = middle + 1;
            } else {
                back = middle - 1;
            }

            middle = front + (back - front)/2;
        }
        return false;
    }
}
