public class MakeTheStringGreat {
    public static void main(String[] args) {
        System.out.println(makeGood("leEeetcode")); // leetcode
        System.out.println(makeGood("lEeeetcode")); // leetcode
        System.out.println(makeGood("Ee")); // ""
        System.out.println(makeGood("e")); // e
        System.out.println(makeGood("abBAcC")); // ""
    }

    /**
     Link: https://leetcode.com/problems/make-the-string-great/
     Purpose: Find String s where the two adjacent upper/lower characters s[i] and s[i + 1] get removed
     parameter: String s - a string
     return: String - s where the two adjacent upper/lower characters s[i] and s[i + 1] get removed
     Pre-Condition: 1 <= s.length <= 100
                  : s contains only lower and upper case English letters.
     Post-Condition: none
     **/
    // runtime: O(n), memory: O(n)
    public static String makeGood(String s) {
        StringBuffer ans = new StringBuffer();
        for(Character c : s.toCharArray()) {
            if (ans.isEmpty()) {
                ans.append(c);
                continue;
            }

            char top = ans.charAt(ans.length() - 1);
            if (Character.toLowerCase(top) == Character.toLowerCase(c) && top != c) {
                ans.deleteCharAt(ans.length() - 1);
            } else {
                ans.append(c);
            }
        }
        return ans.toString();
    }
}
