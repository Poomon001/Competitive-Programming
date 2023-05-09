public class SmallestStringWithAGivenNumericValue {
    public static void main (String[] args){
        System.out.println("\n+=== solution M1 ===+\n");
        System.out.println(getSmallestString_M1(3, 27)); // aay
        System.out.println(getSmallestString_M1(5, 27)); // aaaaw
        System.out.println(getSmallestString_M1(7, 27)); // aaaaaau
        System.out.println(getSmallestString_M1(5, 73)); // aaszz
        System.out.println(getSmallestString_M1(10, 73)); // aaaaaaanzz
        System.out.println(getSmallestString_M1(15, 73)); // aaaaaaaaaaaaizz
        System.out.println(getSmallestString_M1(20, 400)); // aaaafzzzzzzzzzzzzzzz
        System.out.println(getSmallestString_M1(30, 400)); // aaaaaaaaaaaaaaauzzzzzzzzzzzzzz
        System.out.println(getSmallestString_M1(40, 400)); // aaaaaaaaaaaaaaaaaaaaaaaaakzzzzzzzzzzzzzz
        System.out.println(getSmallestString_M1(50, 999)); // aaaaaaaaaaaayzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

        System.out.println("\n+=== solution M2 ===+\n");
        System.out.println(getSmallestString_M2(3, 27)); // aay
        System.out.println(getSmallestString_M2(5, 27)); // aaaaw
        System.out.println(getSmallestString_M2(7, 27)); // aaaaaau
        System.out.println(getSmallestString_M2(5, 73)); // aaszz
        System.out.println(getSmallestString_M2(10, 73)); // aaaaaaanzz
        System.out.println(getSmallestString_M2(15, 73)); // aaaaaaaaaaaaizz
        System.out.println(getSmallestString_M2(20, 400)); // aaaafzzzzzzzzzzzzzzz
        System.out.println(getSmallestString_M2(30, 400)); // aaaaaaaaaaaaaaauzzzzzzzzzzzzzz
        System.out.println(getSmallestString_M2(40, 400)); // aaaaaaaaaaaaaaaaaaaaaaaaakzzzzzzzzzzzzzz
        System.out.println(getSmallestString_M2(50, 999)); // aaaaaaaaaaaayzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    }

    /**
     * Link: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
     * Purpose:  Find the lexicographically smallest string with length 'n', and the sum of its ascii value is 'k'.
     *        : "lexicographically" is appearing in in dictionary alphabetic order. eg: a -> b -> aa -> ab -> aaa -> aab
     * Parameters: int n - an integer, a length of the string
     *           : int k - an integer, a sum of the string ascii value
     * Returns: String ans - the lexicographically smallest string with length 'n', and the sum of its ascii value is 'k'
     * Pre-Condition: 1 <= n <= 105
     *              : n <= k <= 26 * n
     * Post-Condition : none
     **/
    // runtime: O(n), memory: O(n)
    public static String getSmallestString_M1(int n, int k) {
        StringBuilder ans = new StringBuilder();
        // greedy
        while(k > 0){
            int balance = k - n + 1;
            for(int j = 26; j > 0;j--){
                // put the largest char until cannot
                if(balance >= j){
                    ans.append(Character.toString(j + 96));
                    k -= j;
                    n -= 1;
                    break;
                }
            }
        }

        return ans.reverse().toString();
    }

    /**
     * Link: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
     * Purpose:  Find the lexicographically smallest string with length 'n', and the sum of its ascii value is 'k'.
     *        : "lexicographically" is appearing in in dictionary alphabetic order. eg: a -> b -> aa -> ab -> aaa -> aab
     * Parameters: int n - an integer, a length of the string
     *           : int k - an integer, a sum of the string ascii value
     * Returns: String ans - the lexicographically smallest string with length 'n', and the sum of its ascii value is 'k'
     * Pre-Condition: 1 <= n <= 105
     *              : n <= k <= 26 * n
     * Post-Condition : none
     **/
    // runtime: O(n), memory: O(n)
    public static String getSmallestString_M2(int n, int k) {
        StringBuilder ans = new StringBuilder();
        int balance = k - n;

        while(balance > 0) {
            // enough space to put a "z" char
            if (balance >= 26) {
                ans.append(Character.toString(122));
                balance -= 25;
                n -= 1;
            } else {
                // not enough to put a "z" char
                ans.append(Character.toString(balance + 97));
                balance = 0;
                n -= 1;
            }
        }

        // once balacne is 0, we need to fill all the avaliable space wiht "a"
        while(n > 0){
            ans.append("a");
            n -= 1;
        }
        return ans.reverse().toString();
    }
}
