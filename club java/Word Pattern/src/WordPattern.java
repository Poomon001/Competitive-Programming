import java.util.*;
public class WordPattern {
    public static void main(String[] args){
        System.out.println(wordPattern("abba", "dog cat cat dog")); // true
        System.out.println(wordPattern("abab", "dog cat dog cat")); // true
        System.out.println(wordPattern("abyz", "dog cat fish mouse")); // true
        System.out.println(wordPattern("abba", "dog cat cat fish")); // false
        System.out.println(wordPattern("aaaa", "dog cat fish mouse")); // false
        System.out.println(wordPattern("abcd", "dog dog dog dog")); // false
        System.out.println(wordPattern("abb", "dog cat cat dog")); // false
        System.out.println(wordPattern("abba", "dog cat cat")); // false
    }

    /**
     * Link: https://leetcode.com/problems/word-pattern/
     * Purpose: Given a pattern and a string s, find if s follows the same pattern.
     * Parameters: string patten - a pattern of string (all in lowercase)
     *           : string s - words follow by a space each (all in lowercase)
     * Returns: boolean - true if s follows the same pattern. Otherwise false.
     * Pre-Condition: 1 <= pattern.length <= 300
     *              : pattern contains only lower-case English letters.
     *              : 1 <= s.length <= 3000
     *              : s contains only lowercase English letters and spaces ' '.
     *              : s does not contain any leading or trailing spaces.
     *              : All the words in s are separated by a single space.
     * Post-Condition : None
     **/
    // runtime: O(n), memory: O(n)
    public static boolean wordPattern(String pattern, String s) {
        Hashtable<Character, String> seen = new Hashtable<>();
        String[] words = s.split(" ");

        // patter should equal to words
        if(pattern.length() != words.length){
            return false;
        }

        // store word
        for(int i = 0; i < pattern.length(); i++){
            if(seen.containsKey(pattern.charAt(i))){
                // check that every pattern contains a unique word: not accaptable (a, dog), (a, cat)
                if(!seen.get(pattern.charAt(i)).equals(words[i])){
                    return false;
                }
            }else{
                // check that every word contains a unique pattern: not accaptable (a, cat), (b, cat)
                // runtime: O(26) is O(1)
                if(seen.containsValue(words[i])){
                    return false;
                }
            }
            seen.put(pattern.charAt(i), words[i]);
        }

        return true;
    }
}
