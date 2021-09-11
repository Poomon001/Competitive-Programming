import java.lang.*;
import java.util.HashSet;

public class HappyNumber {
    public static void main(String[] args) {
        /**
         * Test case 1:
         * Purpose: help to determine one digit number that converge to true
         * Use the result to define based case
         * Result: 1 and 7 will converge to 1, and the others will converge to non-1 .
         * **/
        for(int i = 0; i < 10; i++){
            System.out.println(i);
            System.out.println(isHappy1(i));
        }

        System.out.println("\n==== = end testcase1 =====\n");

        int n1 = 19;
        int n2 = 2;
        int n3 = 101;
        int n4 = 39;
        int n5 = 7;
        int n6 = 1111111;

        System.out.println(isHappy1(n1)); // true
        System.out.println(isHappy1(n2)); // false
        System.out.println(isHappy1(n3)); // false
        System.out.println(isHappy1(n4)); // false
        System.out.println(isHappy1(n5)); // true
        System.out.println(isHappy1(n6)); // true

        System.out.println("\n==== = end testcase2 =====\n");

        System.out.println(isHappy2(n1)); // true
        System.out.println(isHappy2(n2)); // false
        System.out.println(isHappy2(n3)); // false
        System.out.println(isHappy2(n4)); // false
        System.out.println(isHappy2(n5)); // true
        System.out.println(isHappy2(n6)); // true

        System.out.println("\n==== = end testcase3 =====\n");

    }

    /*
     * Link: https://leetcode.com/problems/happy-number/
     * Purpose: Determine if it is a happy number:
     *        : Starting with any positive integer, replace the number by the sum of the squares of its digits.
              : Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
              : Those numbers for which this process ends in 1 are happy.
     * Parameters: num n - a number to check if happy
     * Returns: boolean - true if happy. Otherwise false
     * Pre-Condition: 1 <= n <= 231 - 1
       Post-Condition : None
     */

    // Dont use hash map: know that only 1 and 7 will convert to 1 from test case#1
    public static boolean isHappy1(int n){
        char[] digits;
        do{
            // store sum
            int sum = 0;

            // store each digit in char array
            digits = Integer.toString(n).toCharArray();

            // the sum of the squares of all digits'
            for (int digit:digits){
                sum += Math.pow(Character.getNumericValue(digit), 2);
            }

            // virtual aid
            // System.out.println(sum+);

            // the only single digit that converge to true are 1 and 7
            if(sum == 1 || sum == 7){
                return true;
            }

            // set n to sum to prepare for the next iteration
            n = sum;
        }while(Integer.toString(n).toCharArray().length != 1);

        return false;
    }

    // use Hash map (Dynamic programming): if the duplicate is found then there is a loop and no way to convert to 1
    public static boolean isHappy2(int n){
        char[] digits;
        HashSet<Integer> seen = new HashSet<>();
        do{
            // store sum
            int sum = 0;

            // store each digit in char array
            digits = Integer.toString(n).toCharArray();


            // the sum of the squares of all digits'
            for (int digit:digits){
                sum += Math.pow(Character.getNumericValue(digit), 2);
            }

            // the only single digit that converge to true are 1 and 7
            if(sum == 1){
                return true;
            }

            // duplicate sum have found and we struck in a loop
            if(seen.contains(sum)){
                return false;
            }

            // add seen num
            seen.add(sum);

            // set n to sum to prepare for the next iteration
            n = sum;
        }while(n != 1);

        return true;
    }
}
