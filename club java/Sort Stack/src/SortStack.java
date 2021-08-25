import java.util.LinkedList;
import java.util.Stack;
import java.util.Queue;

public class SortStack {
    public static void main(String[] args){
        /** test cases: stack **/
        Stack<Integer> s1 = new Stack<>();
        s1.push(2);
        s1.push(3);
        s1.push(1);
        s1.push(0);
        s1.push(-1);
        s1.push(5);

        Stack<Integer> s2 = new Stack<>();
        s2.push(11);
        s2.push(19);
        s2.push(3);
        s2.push(7);
        s2.push(10);
        s2.push(33);
        s2.push(8);

        Stack<Integer> s3 = new Stack<>();
        s3.push(1);
        s3.push(2);
        s3.push(3);
        s3.push(7);
        s3.push(10);
        s3.push(33);
        s3.push(100);
        s3.push(11);

        Stack<Integer> s4 = new Stack<>();
        s4.push(3);
        s4.push(4);
        s4.push(1);
        s4.push(0);

        System.out.print("print sorted Stack: ");
        for (int x :sortStack(s4)){
            System.out.print(x + " ");
        }
    }

    /*
     * Purpose: Sort a stack
     * Parameters: Stack<Integer> s - a stack to be sorted
     * Returns: Stack<Integer> s - sorted stack containing elements from s1
     * Pre-Condition: s is not empty
     * Post-Condition: None
     */
    public static Stack<Integer> sortStack(Stack<Integer> s){
        Stack<Integer> sortedStack = new Stack<>();

        // Worse: O(n^2), Best: O(n)
        while(!s.isEmpty()){
            int curr = s.pop();

            // pop all elements from sortedStack that is higher than curr back to s stack
            // (elements in sortedStack is already sorted)
            // curr will be the highest value in sortedStack
            while (!sortedStack.isEmpty() && sortedStack.peek() > curr){
                s.push(sortedStack.pop());
            }

            // now curr is the highest value in sortedStack, we push it on top
            sortedStack.push(curr);
        }

        return sortedStack;
    }
}
