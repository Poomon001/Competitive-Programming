import java.util.LinkedList;

public class MergeTwoSortedList {
    public static void main(String[] args){
        LinkedList<Integer> list1 = new LinkedList<Integer>();
        list1.add(1);
        list1.add(2);
        list1.add(3);
        list1.add(4);

        LinkedList<Integer> list2 = new LinkedList<Integer>();
        list2.add(1);
        list2.add(2);
        list2.add(5);

        printList(mergeTwoSortedList(list1, list2));
    }

    /*
     * Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/
     * Purpose: Merge two sorted linked lists and return it as a sorted list.
     * Parameters: LinkedList<Integer> - the first linkedlist contains integer object
     *           : LinkedList<Integer> - a second linkedlist contains integer object
     * Returns: a merge linkedlist
     * Post-Condition: none
     */
    public static LinkedList<Integer> mergeTwoSortedList(LinkedList<Integer> list1, LinkedList<Integer> list2){
        LinkedList<Integer> printList = new LinkedList<Integer>();
        while(!list1.isEmpty()&&!list2.isEmpty()){
            int currElement1 = list1.get(0);
            int currElement2 = list2.get(0);

            if(currElement1 < currElement2){
                // remove element from list 1 to printList if the curr element from 1 is less than the curr element from 2
                printList.add(list1.remove());
            }else{
                // otherwise add to element from list 2 to printList
                printList.add(list2.remove());
            }// else
        }// while

        while(!list1.isEmpty()){
            printList.add(list1.remove());
        }

        while(!list2.isEmpty()){
            printList.add(list2.remove());
        }

        return printList;
    }

    private static void printList(LinkedList<Integer> printList){
        while(!printList.isEmpty()){
            System.out.print(printList.remove());
        }
    }

    /** impliment without helper functions **/
    /*
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode printList = new ListNode();

        // need dummy node becase if we simply use printList, printList head
           will point to end of the list after the merging process.
        // So we use dummy to not move printlist head and keep it at the beginning of the list
        ListNode dummy = printList;

        while(true){
            // if either list runs out, simply assign the rest of the other list to dummy
            if(list1 == null){
                dummy.next = list2;
                break;
            }
            if(list2 == null){
                dummy.next = list1;
                break;
            }

            // Compare the value of the two lists, append the smaller value into dummy and
            //  advance the head to the next Node
            if(list1.val <= list2.val){
                dummy.next = list1;
                list1 = list1.next;
            }else{
                dummy.next = list2;
                list2 = list2.next;
            }

            // Advance the dummy
            dummy = dummy.next;
        }// while

        // the very first print is 0 so we skip it
        return printList.next;
    }
    */
}
