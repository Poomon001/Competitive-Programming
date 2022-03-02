public class IsSubsequence {
    public static void main(String[] args){
        System.out.println(isSubsequence("abc", "ahbgdc")); // true
        System.out.println(isSubsequence("axc", "ahbgdc")); // false
        System.out.println(isSubsequence("ace", "abcde")); // true
        System.out.println(isSubsequence("ahbgdc", "ace")); // false
        System.out.println(isSubsequence("aec", "abcde")); // false
        System.out.println(isSubsequence("", "")); // true
    }

    /**
     * Link: https://leetcode.com/problems/is-subsequence/
     * Purpose: Determine if s is a subsequence of t.
     *        : A subsequence of a string is a new string that is formed from the original string by deleting some the characters.
     *        : i.e., "ace" is a subsequence of "abcde" while "aec" is not
     * Parameters: String s - a string
     *           : String t - a string
     * Returns: boolean - return true if s is a subsequence of t, or false otherwise.
     * Pre-Condition: 0 <= s.length <= 100
     *              : 0 <= t.length <= 104
     *              : s and t consist only of lowercase English letters.
     * Post-Condition : none
     **/
    // runtime: O(n), memory: O(1)
    public static boolean isSubsequence(String s, String t) {
        int i = 0; // keep track of char in s
        int j = 0; // keep track of char in t
        while(j < t.length() && i < s.length()){
            if(s.charAt(i) == t.charAt(j)){
                i++;
            }
            j++;
        }
        return i == s.length();
    }
}
