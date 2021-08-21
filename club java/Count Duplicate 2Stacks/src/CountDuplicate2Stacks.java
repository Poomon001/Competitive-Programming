import java.util.*;
public class CountDuplicate2Stacks {
    public static void main(String[] args){
        // testers
        Stack<Integer> s0 = new Stack<>();
        s0.add(0);
        s0.add(2);
        s0.add(3);
        s0.add(4);
        s0.add(5);

        Stack<Integer> s1 = new Stack<>();
        s1.add(0);
        s1.add(2);
        s1.add(3);
        s1.add(4);
        s1.add(5);

        Stack<Integer> s2 = new Stack<>();
        s2.add(-1);
        s2.add(0);
        s2.add(1);
        s2.add(4);
        s2.add(5);

        Stack<Integer> s3 = new Stack<>();
        s3.add(0);
        s3.add(3);
        s3.add(4);

        Stack<Integer> s4 = new Stack<>();

        System.out.println(countDuplicate(s1,s2)); // expected 3
        System.out.println(countDuplicate(s2,s1)); // expected 3
        System.out.println(countDuplicate(s0,s1)); // expected 5
        System.out.println(countDuplicate(s1,s3)); // expected 3
        System.out.println(countDuplicate(s3,s2)); // expected 2
        System.out.println(countDuplicate(s3,s4)); // expected 0
    }

    /*
     * Purpose: Count the number of same elements in 2 sorted stacks.
     * Parameters: Stack<Integer> - the first stack that contain integer objects
     *           : Stack<Integer> - the second stack that contain integer objects
     * Returns: int - number of duplicate elements
     * Pre-condition: Must contain non-duplicate element with in a stack
     *              : Must be sorted stack
     * Post-Condition: Must maintain the original order of both stack
     */
    public static int countDuplicate(Stack<Integer>s1, Stack<Integer>s2){
        // maintain order of both stack
        Stack<Integer> temp1 =  new Stack<>();
        Stack<Integer> temp2 =  new Stack<>();

        // count duplicate
        int counterDup = 0;

        /* find duplicate. We pop the element that has a higher value from its stack to temp stack
           we will eventually found elements with the same value, then we increment the counter and pop both elements */
        while(!s1.isEmpty() && !s2.isEmpty()){
            if(s1.peek() > s2.peek()){
                temp1.push(s1.pop());
            }else if(s1.peek() < s2.peek()){
                temp2.push(s2.pop());
            }else{
                counterDup++;
                temp1.push(s1.pop());
                temp2.push(s2.pop());
            }
        }

        // maintain order of both stack
        while(!s1.isEmpty()){
            temp1.push(s1.pop());
        }

        while(!s2.isEmpty()){
            temp2.push(s2.pop());
        }

        while (!temp1.isEmpty()){
            s1.push(temp1.pop());
        }

        while (!temp2.isEmpty()){
            s2.push(temp2.pop());
        }

        return counterDup;
    }
}
