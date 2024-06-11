import java.util.*;
public class ReversString {
    public static void main(String[] args) {
        System.out.println("\n === solution 1 === \n");

        char[] s1 = "Hello".toCharArray();
        char[] s2 = "hello".toCharArray();
        char[] s3 = "leo".toCharArray();
        char[] s4 = "a".toCharArray();

        reverseString_inplace_m1(s1);
        reverseString_inplace_m1(s2);
        reverseString_inplace_m1(s3);
        reverseString_inplace_m1(s4);

        System.out.println(Arrays.toString(s1)); // [o, l, l, e, H]
        System.out.println(Arrays.toString(s2)); //[o, l, l, e, h]
        System.out.println(Arrays.toString(s3)); // [o, e, l]
        System.out.println(Arrays.toString(s4)); // [a]

        System.out.println("\n === solution 2 === \n");
        s1 = "Hello".toCharArray();
        s2 = "hello".toCharArray();
        s3 = "leo".toCharArray();
        s4 = "a".toCharArray();

        reverseString_inplace_m2(s1);
        reverseString_inplace_m2(s2);
        reverseString_inplace_m2(s3);
        reverseString_inplace_m2(s4);


        System.out.println(Arrays.toString(s1)); // [o, l, l, e, H]
        System.out.println(Arrays.toString(s2)); //[o, l, l, e, h]
        System.out.println(Arrays.toString(s3)); // [o, e, l]
        System.out.println(Arrays.toString(s4)); // [a]
    }

    /**
     * Link: https://leetcode.com/problems/reverse-string/
     * Purpose: Find a reverse of a char array
     * Parameters: int[] s - a char array
     * Returns: None
     * Pre-Condition: 1 <= s.length <= 105
     *              : s[i] is a printable ascii character.
     * Post-Condition : the input array is reversed
     **/
    public static void reverseString_inplace_m1(char[] s) {
        int j = 0;
        for(int i = 0; i < s.length/2; i++){
            j = s.length - 1 - i;
            swap(i, j, s);
        }
    }
    private static void swap(int i, int j, char[] s){
        char temp = s[j];
        s[j] = s[i];
        s[i] = temp;
    }

    public static void reverseString_inplace_m2(char[] s) {
        int i = 0;
        int j = s.length - 1;
        while (i < j) {
            s[i] = (char) (s[i] + s[j]);
            s[j] = (char) (s[i] - s[j]);
            s[i] = (char) (s[i] - s[j]);
            i++;
            j--;
        }
    }
}
