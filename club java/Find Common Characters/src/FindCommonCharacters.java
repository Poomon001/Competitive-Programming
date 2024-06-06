import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class FindCommonCharacters {
    public static void main(String[] args) {
        System.out.println(commonChars(new String[]{"bella","label","roller"})); // [e, l, l]
        System.out.println(commonChars(new String[]{"cool","lock","cook"})); // [c, o]
        System.out.println(commonChars(new String[]{"cool","lock","cook","hello","world"})); // [o]
        System.out.println(commonChars(new String[]{"aaa","bbb","ccc"})); // []
        System.out.println(commonChars(new String[]{"abc","aabbcc","bcass"})); // [a, b, c]
    }

    /*
     * Link: https://leetcode.com/problems/find-common-characters
     * Purpose: Find an array of all characters that show up in all strings
     * Parameters: String[] words: an array of words
     * Returns: List<String> - return an array of all characters that show up in all strings
     * Pre-Condition: 1 <= words.length <= 100
                    : 1 <= words[i].length <= 100
                    : words[i] consists of lowercase English letters.
       Post-Condition : None
     */
    public static List<String> commonChars(String[] words) {
        HashMap<Character, Integer> globalCount = new HashMap();
        ArrayList<String> ans = new ArrayList();

        // the first word will be a benchmark such that all other words need to contain
        // the character from this word
        for(Character c: words[0].toCharArray()) {
            int total = globalCount.getOrDefault(c, 0) + 1;
            globalCount.put(c, total);
        }

        // take the minimum freq of cheracter that occur in any word to the globalCount
        for(String word:words) {
            HashMap<Character, Integer> localCount = new HashMap();
            for(Character c: word.toCharArray()) {
                int total = localCount.getOrDefault(c, 0) + 1;
                localCount.put(c, total);
            }

            // find the minimum frequency
            for(Character key:globalCount.keySet()) {
                int globalFreq = globalCount.getOrDefault(key, 0);
                int localFreq = localCount.getOrDefault(key, 0);
                globalCount.put(key, Math.min(globalFreq, localFreq));

            }
        }

        // store tha answer in array
        for(Character key:globalCount.keySet()) {
            int globalFreq = globalCount.getOrDefault(key, 0);
            while(globalFreq > 0) {
                globalFreq--;
                ans.add(key + "");
            }
        }

        return ans;
    }
}
