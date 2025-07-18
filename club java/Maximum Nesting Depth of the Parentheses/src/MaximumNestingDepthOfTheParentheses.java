import java.util.Stack;
public class MaximumNestingDepthOfTheParentheses {
    public static void main(String[] args) {
        System.out.println(maxDepth("(1+(2*3)+((8)/4))+1")); // 3
        System.out.println(maxDepth("(1)+((2))+(((3)))"));  // 3
        System.out.println(maxDepth("()(())((()()))")); // 3
        System.out.println(maxDepth("aaaaa")); // 0
    }

    /**
     Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses
     Purpose: Given a valid parentheses string s, find the nesting depth is the maximum number of nested parentheses.
     parameter: String s - a valid parentheses string
     return: int maxCount - the maximum number of nested parentheses
     Pre-Condition: 1 <= s.length <= 100
                  : s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
                  : It is guaranteed that parentheses expression s is a VPS.
     Post-Condition: none
     **/
    // rumtime: O(n), memory: O(n)
    public static int maxDepth(String s) {
        Stack<Character> myStack = new Stack<>();
        int count = 0;
        int maxCount = 0;

        for(Character c : s.toCharArray()) {
            if(c == '(') {
                myStack.push(c);
                count++;
            }else if(c == ')') {
                myStack.pop();
                count--;
            }
            maxCount = Math.max(maxCount, count);
        }

        return maxCount;
    }
}
