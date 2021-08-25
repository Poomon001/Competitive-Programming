import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

public class SortStackAndQueue {
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
        System.out.println("");

        /** test cases: queue **/
        Queue<Integer> q1 = new LinkedList<>();
        q1.add(3);
        q1.add(1);
        q1.add(5);
        q1.add(4);
        q1.add(2);
        q1.add(0);

        Queue<Integer> q2 = new LinkedList<>();
        q2.add(1);
        q2.add(2);
        q2.add(3);
        q2.add(4);
        q2.add(5);

        Queue<Integer> q3 = new LinkedList<>();
        q3.add(5);
        q3.add(2);
        q3.add(1);
        q3.add(0);
        q3.add(-2);

        Queue<Integer> q4 = new LinkedList<>();
        q4.add(0);
        q4.add(10);
        q4.add(5);


        System.out.print("print sorted Queue: ");
        for(int x : sortedQueue(q1)){
            System.out.print(x+" ");
        }
    }

    /*
     * Purpose: Sort a stack
     * Parameters: Stack<Integer> s - a stack to be sorted
     * Returns: Stack<Integer> s - sorted stack containing elements from s#
     * Pre-Condition: s is not empty
     * Post-Condition: None
     */
    public static Stack<Integer> sortStack(Stack<Integer> s){
        // helper stack to store a sorted collection
        Stack<Integer> sortedCollection = new Stack<>();

        // Worse: O(n^2), Best: O(n)
        while(!s.isEmpty()){
            int curr = s.pop();

            // pop all elements from sortedCollection that is higher than curr back to s stack
            // (elements in sortedCollection are already sorted)
            // curr will be the highest value in sortedCollection
            while (!sortedCollection.isEmpty() && sortedCollection.peek() > curr){
                s.push(sortedCollection.pop());
            }

            // now curr is the highest value in sortedCollection, we push it on top
            sortedCollection.push(curr);
        }

        // push all value into the stack
        while(!sortedCollection.isEmpty()){
            s.add(sortedCollection.pop());
        }

        return s;
    }

    /*
     * Purpose: Sort a queue
     * Parameters: Queue<Integer> q - a queue to be sorted
     * Returns: Queue<Integer> q - sorted queue containing elements from q#
     * Pre-Condition: q is not empty
     * Post-Condition: None
     */
    public static Queue<Integer> sortedQueue(Queue<Integer> q){
        // helper stack to store a sorted collection
        Stack<Integer> sortedCollection = new Stack<>();

        // Worse: O(n^2), Best: O(n)
        while(!q.isEmpty()){
            int curr = q.poll();

            // pop all elements from sortedCollection that is higher than curr back to q queue
            // (elements in sortedCollection are already sorted)
            // curr will be the highest value in sortedCollection
            while(!sortedCollection.isEmpty() && sortedCollection.peek() > curr){
                q.add(sortedCollection.pop());
            }

            // now curr is the highest value in sortedCollection, we push it on top
            sortedCollection.push(curr);
        }

        // push all value into the queue
        while(!sortedCollection.isEmpty()){
            q.add(sortedCollection.pop());
        }
        return q;
    }
}
