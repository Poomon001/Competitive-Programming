import java.util.*;
public class UniqueMorseCodeWords {
    public static void main(String[] args){
        String[] test1 = {"gin","zen","gig","msg"};
        String[] test2 = {"a"};
        String[] test3 = {"sip", "big", "bed", "gin", "four","zen"};
        String[] test4 = {"gin","sip", "big", "na", "x", "four","zen"};

        /*
        "gin" -> "--...-."
        "zen" -> "--...-."
        "gig" -> "--...--."
        "msg" -> "--...--."
        */
        System.out.println(uniqueMorseRepresentations(test1)); // 2
        System.out.println(uniqueMorseRepresentations(test2)); // 1
        System.out.println(uniqueMorseRepresentations(test3)); // 5
        System.out.println(uniqueMorseRepresentations(test4)); // 5
    }

    /**
     * Link: https://leetcode.com/problems/unique-morse-code-words/
     * Purpose: Find the number of different morse code words among all words we have
     * Parameter: String[] words - words array
     * Returns: int -  the number of different morse code words among all words we have
     * Pre-Condition: 1 <= words.length <= 100
     *              : 1 <= words[i].length <= 12
     *              : words[i] consists of lowercase English letters.
     * Post-Condition: none
     **/

    // run-time: O(mn), O(m) where m = number of word and n = number of characters in all words
    public static int uniqueMorseRepresentations(String[] words){
        // morse code 'a' to 'z'
        String[] morseCode = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        // {alphabet, morse code}
        Hashtable<Character,String> alphabets = new Hashtable();
        HashSet answer = new HashSet();
        int alphabet = 97;

        // create a look up table
        for(String s : morseCode){
            alphabets.put((char)alphabet++, s);
        }

        // convert alphabet words to morse code words
        for(String word:words){
            String morseWord = "";
            for(char c:word.toCharArray()){
                morseWord = morseWord + alphabets.get(c);
            }
            answer.add(morseWord);
        }
        return answer.size();
    }
}
