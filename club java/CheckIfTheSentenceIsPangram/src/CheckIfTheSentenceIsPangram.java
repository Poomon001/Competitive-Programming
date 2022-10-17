import java.sql.SQLOutput;
import java.util.*;
public class CheckIfTheSentenceIsPangram {
    public static void main(String[] args){
        String s1 = "abcdefghijklmnopqrstuvwxyz";
        String s2 = "thequickbrownfoxjumpsoverthelazydog";
        String s3 = "";
        String s4 = "hello";

        System.out.println("\n+=== solution 1 ===+\n");
        System.out.println(checkIfPangram_m1(s1)); // true
        System.out.println(checkIfPangram_m1(s2)); // true
        System.out.println(checkIfPangram_m1(s3)); // false
        System.out.println(checkIfPangram_m1(s4)); // false
        System.out.println("\n+=== solution 2 ===+\n");
        System.out.println(checkIfPangram_m2(s1)); // true
        System.out.println(checkIfPangram_m2(s2)); // true
        System.out.println(checkIfPangram_m2(s3)); // false
        System.out.println(checkIfPangram_m2(s4)); // false
    }

    /**
     * Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
     * Purpose: Determine Whether a string is pangram.
     *        : Pangram is a sentence where every letter of the English alphabet appears at least once.
     * Parameter: String sentence - a string
     * Returns: boolean: true if a string is pangram. Otherwise, false.
     * Pre-Condition: 1 <= sentence.length <= 1000
     *              : sentence consists of lowercase English letters.
     * Post-Condition: none
     **/
    // set: runtime - O(n), memory - O(1)
    public static boolean checkIfPangram_m1(String sentence) {
        // {char, counter}
        HashSet<Character> alphabets = new HashSet();
        for(int i = 0; i < sentence.length(); i++){
            alphabets.add(sentence.charAt(i));
        }
        return alphabets.size() == 26? true:false;
    }

    /**
     * Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
     * Purpose: Determine Whether a string is pangram.
     *        : Pangram is a sentence where every letter of the English alphabet appears at least once.
     * Parameter: String sentence - a string
     * Returns: boolean: true if a string is pangram. Otherwise, false.
     * Pre-Condition: 1 <= sentence.length <= 1000
     *              : sentence consists of lowercase English letters.
     * Post-Condition: none
     **/
    // hashmap: runtime - O(n), memory - O(1)
    public static boolean checkIfPangram_m2(String sentence) {
        // {char, counter}
        Hashtable<Character, Integer> alphabets = new Hashtable();
        for(Character c : sentence.toCharArray()){
            alphabets.put(c, alphabets.getOrDefault(c, 0) + 1);
        }

        for(int i = 97; i < 123; i++){
            char c = (char) i;
            if(alphabets.getOrDefault(c, 0) == 0){
                return false;
            }
        }
        return true;
    }
}
