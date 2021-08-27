
public class PlusOne {
    public static void main(String[] args) {
        // Test cases
        int[] t1 = {1,2,3};
        printResult(plusOne_Solution(t1)); // 124

        int[] t2 = {4,3,2,1};
        printResult(plusOne_Solution(t2)); // 4322

        int[] t3 = {0};
        printResult(plusOne_Solution(t3)); // 1

        int[] t4 = {1, 9};
        printResult(plusOne_Solution(t4)); // 20

        int[] t5 = {9};
        printResult(plusOne_Solution(t5)); // 10

        int[] t6 = {9,8,7,6,5,4,3,2,1,0};
        printResult(plusOne_Solution(t6)); // 9876543211

        int[] t7 = {7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6};
        printResult(plusOne_Solution(t7)); // 728509129536673284379577474947011174007
    }

    /*
     * Link: https://leetcode.com/problems/plus-one/
     * Purpose: Increment one to the array of integers
     * Parameters: int[] digits - the array of integers
     * Returns: int[] newDigits or digits - the array of integers after increment one
     * Pre-conditions: 1 <= digits.length <= 100
     *               : 0 <= digits[i] <= 9
     * Post-condition: None - digits can be modify
     */
    public static int[] plusOne_Solution(int[] digits) {
        // carrier to carry 1 if we add one to nine
        int carrier = 1;

        for(int i = digits.length - 1; i >= 0; i--){
            int digit = digits[i];

            // carrier is 1: add 1 to the next digit
            if (carrier == 1) {
                // case 1: add one to digit "9" then we will have carrier of 1 and Then set digit to 0
                if (digit + 1 > 9) {
                    digits[i] = 0;
                }

                // case 2: add one to digit "0-8" then we will have carrier of 0
                if (digit + 1 <= 9) {
                    carrier = 0;
                    digits[i] = digit + 1;
                }
            // carrier is 0: no operation
            }else{
                digits[i] = digit;
            }
        }

        // carrier is 1 here then we need to add digit 1 to the front of the digits array
        if (carrier == 1){
            int[] newDigits = new int[digits.length+1];
            for(int i = 0; i < newDigits.length; i++){
                // digits[i-1] b/c the first digit of newDigits is 1, so digits will be move by 1 position
                newDigits[i] = i == 0? 1:digits[i-1];
            }
            return newDigits;
        }

        return digits;
    }

    private static final void printResult(int[] numbers){
        for(int num:numbers){
            System.out.print(num);
        }
        System.out.print("\n");
    }

}
