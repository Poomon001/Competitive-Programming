import java.util.ArrayList;
import java.util.HashMap;

public class UncommonWordsFromTwoSentences {
    public static void main(String[] args) {
        println(uncommonFromSentences("this apple is sour", "this apple is sweet")); // ["sour", "sweet"]
        println(uncommonFromSentences("this apple is sweet", "this apple is sweet")); // [""]
        println(uncommonFromSentences("this apple is sweet sour", "this apple is sweet")); // ["sour"]
        println(uncommonFromSentences("apple apple", "banana")); // ["banana"]
    }

    /**
     Link: https://leetcode.com/problems/uncommon-words-from-two-sentences/
     Purpose: Find a list of all the uncommon words.
            : A word is uncommon if it appears exactly once in one of the sentences and does not appear in the other sentence.
     parameter: String s1 - a string
              : String s2 - a string
     return: String[] - a list of all the uncommon words
     Pre-Condition: 1 <= s1.length, s2.length <= 200
                  : s1 and s2 consist of lowercase English letters and spaces.
                  : s1 and s2 do not have leading or trailing spaces.
                  : All the words in s1 and s2 are separated by a single space.
     Post-Condition: none
     **/
    // Hashmap - runtime: O(n), memory: O(n)
    public static String[] uncommonFromSentences(String s1, String s2) {
        String[] arr1 = s1.split("\\s+");
        String[] arr2 = s2.split("\\s+");
        HashMap<String, Integer> wordToFreq = new HashMap();
        ArrayList<String> ans = new ArrayList();

        for (String word: arr1){
            wordToFreq.put(word, wordToFreq.getOrDefault(word, 0) + 1);
        }

        for (String word: arr2){
            wordToFreq.put(word, wordToFreq.getOrDefault(word, 0) + 1);
        }

        for(String key:wordToFreq.keySet()){
            if (wordToFreq.get(key) == 1) {
                ans.add(key);
            }
        }

        return ans.toArray(new String[ans.size()]);
    }

    public static void println(String[] arr){
        for(String s:arr){
            System.out.print(s + " ");
        }
        System.out.println("");
    }
}
