import java.util.*;
import java.util.Arrays;

public class ValidAnagram {
    public static void main(String[] args) {
        String s1 = "anagram";
        String t1 = "nagaram";
        System.out.println(validAnagram_M1(s1, t1)); // true
        System.out.println(validAnagram_M2(s1, t1)); // true

        String s2 = "rat";
        String t2 = "cat";
        System.out.println(validAnagram_M1(s2, t2)); // false
        System.out.println(validAnagram_M2(s2, t2)); // false

        String s3 = "fried";
        String t3 = "fried";
        System.out.println(validAnagram_M1(s3, t3)); //true
        System.out.println(validAnagram_M2(s3, t3)); //true

        String s4 = "rat";
        String t4 = "tar";
        System.out.println(validAnagram_M1(s4, t4)); // true
        System.out.println(validAnagram_M2(s4, t4)); // true

        String s5 = "listen";
        String t5 = "silent";
        System.out.println(validAnagram_M1(s5, t5)); // true
        System.out.println(validAnagram_M2(s5, t5)); // true

        String s6 = "aacc";
        String t6 = "ccac";
        System.out.println(validAnagram_M1(s6, t6)); // false
        System.out.println(validAnagram_M2(s6, t6)); // false
    }

    /*
     * Link: https://leetcode.com/problems/valid-anagram/
     * Purpose: Determine if 2 string are anagram
     * Parameters: String s: the first string
     *           : String t: the second string
     * Returns: boolean - return true if t is an anagram of s, and false otherwise.
     * Pre-Condition: 1 <= s.length, t.length <= 5 * 104
                    : s and t consist of lowercase English letters.
       Post-Condition : None
     */

    // use array sort: runtime: O(n), memory: O(n)
    public static boolean validAnagram_M1(String s, String t){
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        // sort both char arrays
        Arrays.sort(sArray);
        Arrays.sort(tArray);

        return Arrays.equals(sArray, tArray); //O(n)
    }

    // use hashmap: runtime: O(n), memory: O(n)
    public static boolean validAnagram_M2(String s, String t){
        Hashtable<Character, Integer> seen = new Hashtable<>();

        // check length
        if (t.length() != s.length()){
            return false;
        }

        // if both are same
        if (t.equals(s)){
            return true;
        }

        // read char in string s
        for (int i = 0; i < s.length(); i++){
            // if key exist then add 1 to the value
            if (seen.containsKey(s.charAt(i))){
                int counter = seen.get(s.charAt(i));
                counter++;
                seen.put(s.charAt(i), counter);
            // if key doesnt exist then initilize 1 to the value
            }else {
                seen.put(s.charAt(i), 1);
            }
        }

        // cheack char in string t
        for (int i = 0; i < t.length(); i++){
            // found the same char (key) subtract one from value
            if(seen.containsKey(t.charAt(i))){
                int counter = seen.get(t.charAt(i));
                counter--;
                seen.put(t.charAt(i), counter);
            }
        }

        // check count and return result
        for (int i = 0; i < s.length(); i++){
            if (seen.get(s.charAt(i)) != 0){
                return false;
            }
        }
        return true;
    }
}
