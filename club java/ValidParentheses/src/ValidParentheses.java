import java.util.*; //importing the stack class
public class ValidParentheses {
    public static void main(String[] args){
        String s1 = "()[]{}";
        String s2 = "(([]){})";
        String s3 = "(]";
        String s4 = "([)]";
        String s5 = "{[]}";
        String s6 = "[]";
        System.out.println(ValidParentheses(s1)); // true
        System.out.println(ValidParentheses(s2)); // true
        System.out.println(ValidParentheses(s3)); // false
        System.out.println(ValidParentheses(s4)); // false
        System.out.println(ValidParentheses(s5)); // true
        System.out.println(ValidParentheses(s6)); // true
        System.out.println("Done method 1 \n");

        System.out.println(ValidParenthesesStack(s1)); // true
        System.out.println(ValidParenthesesStack(s2)); // true
        System.out.println(ValidParenthesesStack(s3)); // false
        System.out.println(ValidParenthesesStack(s4)); // false
        System.out.println(ValidParenthesesStack(s5)); // true
        System.out.println(ValidParenthesesStack(s6)); // true
        System.out.println("Done method 2");

    }

    /**
     * Link: https://leetcode.com/problems/valid-parentheses/
     * Purpose: Determine if the input string contain all valid pairs: '(', ')', '{', '}', '[' and ']'
     * Parameters: string - a string contain parentheses, brackets, and/or braces
     * Returns: boolean - true is the input string contain all valid pairs. Othersies, false
     * pre-Condition: 1 <= s.length <= 104
     *               : s consists of parentheses only '()[]{}'
     * Post-Condition: none
     **/
    // method1: using build-in sting methods O(n^2)
    public static boolean ValidParentheses(String str){
        // the maximumIteration will be len(str)/2 because we will at least remove a pair each iteration for a True string
        int maximumLoopIteration = (int)Math.ceil(str.length()/2);

        for(int i = 0; i < maximumLoopIteration; i++) {
            // keep removing a pair of "()", "[]", and "{}" in the str
            str = str.replace("{}", "");
            str = str.replace("()", "");
            str = str.replace("[]", "");

            // string is empty == all pair is found and removed
            if(str.length() == 0){
                return true;
            }
        }
        return false;
    }

    /**
     * Link: https://leetcode.com/problems/valid-parentheses/
     * Purpose: Determine if the input string contain all valid pairs: '(', ')', '{', '}', '[' and ']'
     * Parameters: string - a string contain parentheses, brackets, and/or braces
     * Returns: boolean - true is the input string contain all valid pairs. Othersies, false
     * pre-Condition: 1 <= s.length <= 104
     *               : s consists of parentheses only '()[]{}'
     * Post-Condition: O(n)
     **/
    // method2: using stack O(n)
    public static boolean ValidParenthesesStack(String str){
        Stack<Character> charStack = new Stack<Character>();
        for(char c:str.toCharArray()){

            // found a parentheses pair, remove it from stack
            if (!charStack.isEmpty() && charStack.peek() == '(' && c == ')') {
                charStack.pop();
                continue;
            }

            // found a brackets pair, remove it from stack
            if (!charStack.isEmpty() && charStack.peek() == '[' && c == ']') {
                charStack.pop();
                continue;
            }

            // found a braces pair, remove it from stack
            if (!charStack.isEmpty() && charStack.peek() == '{' && c == '}') {
                charStack.pop();
                continue;
            } //if
            charStack.push(c);
        } // for

        if(charStack.isEmpty()){
            return true;
        }else{
            return false;
        }
    }
}
