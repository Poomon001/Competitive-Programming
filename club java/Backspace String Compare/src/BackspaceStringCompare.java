import java.util.Stack;


public class BackspaceStringCompare {
    public static void main(String[] args) {
        System.out.println(backspaceCompare("ab#c", "ad#c")); // true
        System.out.println(backspaceCompare("ab##", "c#d#")); // true
        System.out.println(backspaceCompare("a#c", "b")); // false
        System.out.println(backspaceCompare("a##c", "#a#c")); // true
    }

    /**
     * Link: https://leetcode.com/problems/backspace-string-compare
     * Purpose: Find if two strings are equal when both are typed into empty text editors. '#' means a backspace character.
     * Parameters: String s - a string
     *           : String t - a string
     * Returns: boolean - true if two strings are equal after processing backspace
     * Pre-Condition: 1 <= s.length, t.length <= 200
     *              : s and t only contain lowercase letters and '#' characters.
     * Post-Condition : None
     **/
    // runtime: O(n + m), memory: O(n + m)
    public static boolean backspaceCompare(String s, String t) {
        Stack<Character> sStack = process(s);
        Stack<Character> tStack = process(t);

        return sStack.toString().equals(tStack.toString());
    }

    private static Stack<Character> process(String s) {
        Stack<Character> stack = new Stack<>();
        for(Character c:s.toCharArray()) {
            if(c == '#') {
                if(!stack.isEmpty()) {
                    stack.pop();
                }
            }else{
                stack.add(c);
            }
        }
        return stack;
    }
}
