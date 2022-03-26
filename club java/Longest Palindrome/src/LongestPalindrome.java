import java.util.*;
public class LongestPalindrome {
    public static void main(String[] args) {
        System.out.println(longestPalindrome("abccccdd")); // 7
        System.out.println(longestPalindrome("a")); // 1
        System.out.println(longestPalindrome("bb")); // 2
        System.out.println(longestPalindrome("AaAaBbZzzz")); // 7
        System.out.println(longestPalindrome("Aa")); // 1
    }

    /**
     * Link: https://leetcode.com/problems/longest-palindrome/
     * Purpose: Find the length of the longest palindrome that can be built with a string
     * Parameters: string s - a string contains upper and lowercase characters
     * Returns: int - the length of the longest palindrome that can be built with a string
     * Pre-Condition: 1 <= s.length <= 2000
     *              : s consists of lowercase and/or uppercase English letters only.
     * Post-Condition : none
     **/
    // runtime: O(n), space: O(1)
    public static int longestPalindrome(String s) {
        // {upper/lower alphabet, counter}
        Hashtable<Character, Integer> letters = new Hashtable<>();

        int sum = 0;
        boolean isOdd = false;

        // put all data to hash table
        for(char c:s.toCharArray()){
//            if(letters.containsKey(c)){
//                letters.put(c, letters.get(c)+1);
//            }else{
//                letters.put(c,1);
//            }
            letters.put(c, letters.getOrDefault(c, 0)+1);
        }

        // count palindrome
        for(char c:letters.keySet()){
            int value = letters.get(c);
            if(value%2 == 0){
                sum += value;
            }else{
                isOdd = true;
                sum += value-1;
            }
        }

        return isOdd?sum+1:sum;
    }
}
