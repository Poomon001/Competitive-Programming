import java.util.*;

public class FirstUniqueCharacterInString {
    public static void main (String[] arg){
        String s1 = "leetcode";
        String s2 = "loveleetcode";
        String s3 = "aabb";
        String s4 = "z";

        System.out.println("\n+=== solution1 ===+\n");
        System.out.println(firstUniqChar_M1(s1)); // 0
        System.out.println(firstUniqChar_M1(s2)); // 2
        System.out.println(firstUniqChar_M1(s3)); // -1
        System.out.println(firstUniqChar_M1(s4)); // 0

        System.out.println("\n+=== solution2 ===+\n");
        System.out.println(firstUniqChar_M2(s1)); // 0
        System.out.println(firstUniqChar_M2(s2)); // 2
        System.out.println(firstUniqChar_M2(s3)); // -1
        System.out.println(firstUniqChar_M2(s4)); // 0

        System.out.println("\n+=== solution3 ===+\n");
        System.out.println(firstUniqChar_M3(s1)); // 0
        System.out.println(firstUniqChar_M3(s2)); // 2
        System.out.println(firstUniqChar_M3(s3)); // -1
        System.out.println(firstUniqChar_M3(s4)); // 0
    }

    /**
     * Link: https://leetcode.com/problems/first-unique-character-in-a-string/
     * Purpose:  find the first non-repeating character in a string
     * Parameter: String s - a string
     * Returns: int the index of the first non repeated character
     * Pre-Condition: 1 <= s.length <= 105
     *              : s consists of only lowercase English letters.
     * Post-Condition: none
     **/
    // brute force: run time - O(n^2), memory: O(1)
    public static int firstUniqChar_M1(String s) {
        int answer = -1;

        if(s.length() == 1){
            return 0;
        }

        for(int i = 0; i < s.length(); i++){
            if(answer != -1){
                return answer;
            }
            for(int j = 0; j < s.length();j++){
                if(i!=j){
                    if(s.charAt(i) == s.charAt(j)){
                        answer = -1;
                        break;
                    }else{
                        answer = i;
                    }
                }
            }
        }
        return answer;
    }

    /**
     * Link: https://leetcode.com/problems/first-unique-character-in-a-string/
     * Purpose:  find the first non-repeating character in a string
     * Parameter: String s - a string
     * Returns: int the index of the first non repeated character
     * Pre-Condition: 1 <= s.length <= 105
     *              : s consists of only lowercase English letters.
     * Post-Condition: none
     **/
    // hash table counter: runtime: O(n), memory: O(1)
    public static int firstUniqChar_M2(String s) {
        // 26 char at max so it is a constant
        Hashtable<Character, Integer> characters = new Hashtable();

        if(s.length() == 1){
            return 0;
        }

        // counter characters in the string
        for(Character c:s.toCharArray()){
            if(characters.containsKey(c)){
                characters.put(c, characters.get(c)+1);
            }else{
                characters.put(c, 1);
            }
        }

        // return the first  index of a non duplicate
        for(int i = 0; i < s.length(); i++){
            if(characters.get(s.charAt(i)) == 1){
                return i;
            }
        }
        return -1;
    }

    /**
     * Link: https://leetcode.com/problems/first-unique-character-in-a-string/
     * Purpose:  find the first non-repeating character in a string
     * Parameter: String s - a string
     * Returns: int the index of the first non repeated character
     * Pre-Condition: 1 <= s.length <= 105
     *              : s consists of only lowercase English letters.
     * Post-Condition: none
     **/
    // first and last search index: runtime: O(n), memory: O(1)
    public static int firstUniqChar_M3(String s) {
        HashSet<Character> uniqueSet = new HashSet();
        for (int i = 97; i < 123; i++) {
            char c = (char) i;

            // if the first and the last index are the same then it is a unique character in a char
            if (s.indexOf(c) == s.lastIndexOf(c) && s.indexOf(c) != -1) {
                uniqueSet.add(c);
            }
        }

        // return the first index of a non duplicate
        for (int i = 0; i < s.length(); i++) {
            if (uniqueSet.contains(s.charAt(i))) {
                return i;
            }
        }
        return -1;
    }
}
