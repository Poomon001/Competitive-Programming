public class RotateString {
    public static void main(String[] args) {
        System.out.println("\n brute force method");
        System.out.println(rotateString_M1("abcde", "cdeab")); // true
        System.out.println(rotateString_M1("abcde", "abced")); // false
        System.out.println(rotateString_M1("absd", "absd"));    // true
        System.out.println(rotateString_M1("gcmbf", "fgcmb")); // true

        System.out.println("\n KMP algo method");
        System.out.println(rotateString_M2("abcde", "cdeab")); // true
        System.out.println(rotateString_M2("abcde", "abced")); // false
        System.out.println(rotateString_M2("absd", "absd")); // true
        System.out.println(rotateString_M2("gcmbf", "fgcmb")); // true
    }

    /**
    * Link: https://leetcode.com/problems/rotate-string/
    * Purpose: Find if the goal a shift on s Strings
    * Parameters: String s, String goal - a s and goal Strings
    * Returns: bool - true if yes, otherwise false.
    * Pre-Condition: 1 <= s.length, goal.length <= 100
                   : s and goal consist of lowercase English letters.
      Post-Condition : None
    **/

    // brute force: runtime: O(n^2), memory: O(1)
    public static boolean rotateString_M1(String s, String goal) {
        int len = s.length();
        // rotate each char in s. Then compare it with goal
        for(int i = 0; i < len; i++){
            // runtime of s.subString is O(n)
            s = s.substring(1, len) + s.charAt(0);
            if(s.equals(goal)){
                return true;
            }
        }
        return false;
    }


    /**
    * Link: https://leetcode.com/problems/rotate-string/
    * Purpose: Find if the goal a shift on s Strings
    * Parameters: String s, String goal - a s and goal Strings
    * Returns: bool - true if yes, otherwise false.
    * Pre-Condition: 1 <= s.length, goal.length <= 100
                   : s and goal consist of lowercase English letters.
      Post-Condition : None
    **/

    // KMP algo: runtime: O(1), memory: O(1)
    // use the fact that s + s cover all possible shift. eg s = "abcde", goal = "cdeab", s + s = "abcdeabcde"
    public static boolean rotateString_M2(String s, String goal) {
        if(s.length() != goal.length()){
            return false;
        }
        String newS = s+s;
        return newS.indexOf(goal) > -1?true:false;
    }
}
