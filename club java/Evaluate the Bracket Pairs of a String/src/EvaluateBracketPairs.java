import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

public class EvaluateBracketPairs {
    public static void main(String[] args) {
        List<List<String>> list1 = Arrays.asList(
                Arrays.asList("name", "bob"),
                Arrays.asList("age", "two")
        );
        System.out.println(evaluate("(name)is(age)yearsold", list1)); // "bobistwoyearsold"

        List<List<String>> list2 = Arrays.asList(
                Arrays.asList("a", "b")
        );
        System.out.println(evaluate("hi(name)", list2)); // "hi?"

        List<List<String>> list3 = Arrays.asList(
                Arrays.asList("a", "yes")
        );
        System.out.println(evaluate("yesyesyesaaa", list3)); // "yesyesyesaaa"
    }

    /**
     * Link: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string
     * Purpose: Given a string s of english alphabets with valid (some words), replace (some word) with knowledge
     * Parameters: String s - a string
     *           : List<List<String>> knowledge - a valid pair of knowledge and value
     * Returns: String answer - the result string
     * Pre-Condition: 1 <= s.length <= 105
     *              : 0 <= knowledge.length <= 10^5
     *              : knowledge[i].length == 2
     *              : 1 <= keyi.length, valuei.length <= 10
     *              : s consists of lowercase English letters and round brackets '(' and ')'.
     *              : Every open bracket '(' in s will have a corresponding close bracket ')'.
     *              : The key in each bracket pair of s will be non-empty.
     *              : There will not be any nested bracket pairs in s.
     *              : keyi and valuei consist of lowercase English letters.
     *              : Each keyi in knowledge is unique.
     * Post-Condition : None
     **/

    // runtime: O(m + n), space O(m + n) where m is the knowledge size and n is character of s
    public static String evaluate(String s, List<List<String>> knowledge) {
        StringBuffer answer = new StringBuffer();
        ConcurrentHashMap<String, String> knowledgeToValue = new ConcurrentHashMap<>();
        for(List<String> pair : knowledge){
            knowledgeToValue.put(pair.get(0), pair.get(1));
        }

        int i  = 0;
        while(i < s.length()) {
            if (s.charAt(i) == '(') {
                StringBuffer temp = new StringBuffer();
                i += 1; // skip (

                while(s.charAt(i) != ')') {
                    temp.append(s.charAt(i));
                    i += 1;
                }
                answer.append(knowledgeToValue.getOrDefault(temp.toString(), "?"));
            } else {
                answer.append(s.charAt(i));
            }
            i += 1;
        }

        return answer.toString();
    }
}
