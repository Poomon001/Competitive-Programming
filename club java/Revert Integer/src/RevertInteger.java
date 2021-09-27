public class RevertInteger {
    public static void main(String[] args) {
        System.out.println(" \n=== revert integr M1 ===\n");
        System.out.println(reverse_M1(123));
        System.out.println(reverse_M1(-321));
        System.out.println(reverse_M1(0));
        System.out.println(" \n=== revert integr M2 ===\n");
        System.out.println(reverse_M2(123));
        System.out.println(reverse_M2(-321));
        System.out.println(reverse_M2(0));
    }

    /*
    * Link: https://leetcode.com/problems/reverse-integer/
    * Purpose: revert a signed 32-bit integer
    *        : return 0 if the innteger is outside the signed 32-bit integer range [-231, 231 - 1]
    * Parameters: int - a signed integer
    * Returns: int - a revert integer
    * Pre-Condition: -231 <= x <= 231 - 1
      Post-Condition : None
    */

    // convert to string and reverse: O(m) where m is length of input
    public static int reverse_M1(int x) {
        // try if the input is in a valid range
        try {
            // convert input to string
            String strX = String.valueOf(x);
            String result = "";

            // case 1: zero and positive
            if (x >= 0) {
                // reverse and return
                for (int i = strX.length() - 1; i >= 0; i--) {
                    result += strX.charAt(i);
                }
                return Integer.valueOf(result);
                // case 2: negative
            } else {
                // reverse, add negative, and return
                for (int i = strX.length() - 1; i >= 1; i--) {
                    result += strX.charAt(i);
                }
                return -Integer.valueOf(result);
            }
        } catch (IllegalArgumentException e) {
            // return 0 if input is not in a valid range
            return 0;
        }
    }

    /*
    * Link: https://leetcode.com/problems/reverse-integer/
    * Purpose: revert a signed 32-bit integer
    *        : return 0 if the innteger is outside the signed 32-bit integer range [-231, 231 - 1]
    * Parameters: int - a signed integer
    * Returns: int - a revert integer
    * Pre-Condition: -231 <= x <= 231 - 1
      Post-Condition : None
    */

    // use integer reverse logic: O(m) where m is length of input
    public static int reverse_M2(int x) {
        // try if the input is in a valid range
        try {
            // case 1: input is zero then return
            if (x == 0) {
                return 0;
            }

            // check if the input is negative
            boolean isNegative = x < 0 ? true : false;

            // store result
            String result = "";

            // convert negative input to positive
            if (isNegative) {
                x *= -1;
            }

            // revert integer logic
            while (x != 0) {
                result += x % 10;
                x = x / 10;
            }
            // put negative sign back if the input is originally negative
            return isNegative ? -Integer.valueOf(result) : Integer.valueOf(result);
        } catch (IllegalArgumentException e) {
            // return 0 if input is not in a valid range
            return 0;
        }
    }
}
