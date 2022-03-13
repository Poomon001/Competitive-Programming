import java.util.*;
public class ReversString {
    public static void main(String[] args) {
        char[] s1 = "Hello".toCharArray();
        char[] s2 = "hello".toCharArray();
        char[] s3 = "leo".toCharArray();
        char[] s4 = "a".toCharArray();

        reverseString_inplace(s1);
        reverseString_inplace(s2);
        reverseString_inplace(s3);
        reverseString_inplace(s4);


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
    public static void reverseString_inplace(char[] s) {
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
}
