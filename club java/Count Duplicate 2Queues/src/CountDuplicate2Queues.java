import java.util.*;
public class CountDuplicate2Queues {
    public static void main(String[] args){
        // test cases
        Queue<Integer> q0 = new LinkedList<>();
        q0.add(5);
        q0.add(4);
        q0.add(3);
        q0.add(2);
        q0.add(0);

        Queue<Integer> q1 = new LinkedList<>();
        q1.add(5);
        q1.add(4);
        q1.add(3);
        q1.add(2);
        q1.add(0);

        Queue<Integer> q2 = new LinkedList<>();
        q2.add(5);
        q2.add(4);
        q2.add(1);
        q2.add(0);
        q2.add(-1);

        Queue<Integer> q3 = new LinkedList<>();
        q3.add(4);
        q3.add(3);
        q3.add(0);

        Queue<Integer> q4 = new LinkedList<>();

        System.out.println(countDuplicate(q1,q2)); // expected 3
        System.out.println(countDuplicate(q2,q1)); // expected 3
        System.out.println(countDuplicate(q0,q1)); // expected 5
        System.out.println(countDuplicate(q1,q3)); // expected 3
        System.out.println(countDuplicate(q3,q2)); // expected 2
        System.out.println(countDuplicate(q3,q4)); // expected 0
    }

    /*
     * Purpose: Count the number of same elements in 2 sorted queues.
     * Parameters: Queue<Integer> - the first queue that contain integer objects
     *           : Queue<Integer> - the second queue that contain integer objects
     * Returns: int - number of duplicate elements
     * Pre-condition: Must contain non-duplicate element with in a queue
     *              : Must be sorted queue
     * Post-Condition: Must maintain the original order of both queues
     */
    public static int countDuplicate(Queue<Integer> q1, Queue<Integer>q2){
        // count how many elements get removed from each queue
        int counterQ1 = 0;
        int counterQ2 = 0;

        // count duplicate
        int counterDup = 0;

        /* We know that the queues are sorted, so we will remove the element that is found the higher in value from its queue
           when compare with the other element from the other queue.
           We will eventually found when elements of 2 queues have the same value, then increase counter and dequeue both */
        while(counterQ1 < q1.size() && counterQ2 < q2.size()){
            if(q1.peek() > q2.peek()){
                q1.add(q1.poll());
                counterQ1++;
            }else if(q1.peek() < q2.peek()){
                q2.add(q2.poll());
                counterQ2++;
            }else{
                counterDup++;
                counterQ1++;
                counterQ2++;
                q1.add(q1.poll());
                q2.add(q2.poll());
            }
        }

        // maintain order of q1
        for(int i = 0; i < q1.size()-counterQ1; i++){
            q1.add(q1.poll());
        }

        // maintain order of q2
        for(int i = 0; i < q2.size()-counterQ2; i++){
            q2.add(q2.poll());
        }

        return counterDup;
    }
}
