public class CheckIfTwoStringArraysAreEquivalent {
    public static void main(String[] args) {
        System.out.println(arrayStringsAreEqual(new String[] {"ab", "c"}, new String[] {"a", "bc"})); // true
        System.out.println(arrayStringsAreEqual(new String[] {"ab", "c"}, new String[] {"a", "cb"})); // false
        System.out.println(arrayStringsAreEqual(new String[] {"ab", "c", "def", "gh"}, new String[] {"abcdefgh"})); // true
        System.out.println(arrayStringsAreEqual(new String[] {"ab", "c", "def", "gh"}, new String[] {"abcdefghi"})); // false
    }

    /**
     * Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
     * Purpose: Find if the two arrays represent the same string
     * Parameter: String[] word1 - an array of string
     *          : String[] word2 - an array of string
     * Returns: boolean - True if two array represent the same string. Otherwise false
     * Pre-Condition: 1 <= word1.length, word2.length <= 10^3
     *              : 1 <= word1[i].length, word2[i].length <= 10^3
     *              : 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
     *              : word1[i] and word2[i] consist of lowercase letters
     * Post-Condition: none
     **/
    public static boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String w1 = "";
        String w2 = "";

        for(String s:word1){
            w1 = w1 + s;
        }

        for(String s:word2){
            w2 = w2 + s;
        }

        return w1.equals(w2);
    }
}
