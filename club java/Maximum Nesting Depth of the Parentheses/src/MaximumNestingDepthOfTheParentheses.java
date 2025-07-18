import java.util.Stack;
public class MaximumNestingDepthOfTheParentheses {
    public static void main(String[] args) {
        System.out.println(maxDepth("(1+(2*3)+((8)/4))+1")); // 3
        System.out.println(maxDepth("(1)+((2))+(((3)))"));  // 3
        System.out.println(maxDepth("()(())((()()))")); // 3
        System.out.println(maxDepth("aaaaa")); // 0
    }

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
