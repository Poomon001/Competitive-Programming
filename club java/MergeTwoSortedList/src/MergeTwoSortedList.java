import java.util.LinkedList;

public class MergeTwoSortedList {
    /* Node Class */
    private static class ListNode {
        int val;
        ListNode next;

        // Constructor to create a new node
        ListNode() {}
        ListNode(int d) {
            val = d;
            next = null;
        }
    }

    public static void main(String[] args){
        /** build-in LinkedList **/
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

        System.out.println("\n=== End Build-in Linkedlist ==\n");

        /** Raw LinkedList **/
        ListNode list3 = new ListNode();
        ListNode dummy = list3;

        // add new nodes to the linked list
        ListNode num1 = new ListNode(1);
        /*list3.next = num1;*/
        dummy.next = num1;
        dummy = dummy.next;

        ListNode num2 = new ListNode(2);
        /*num1.next = num2;*/
        dummy.next = num2;
        dummy = dummy.next;

        ListNode num3 = new ListNode(3);
        /*num2.next = num3;*/
        dummy.next = num3;
        dummy = dummy.next;

        ListNode num4 = new ListNode(4);
        /*num3.next = num4;*/
        dummy.next = num4;

        ListNode list4 = new ListNode();
        dummy = list4;

        // add new nodes to the linked list
        ListNode num5 = new ListNode(1);
        /*list4.next = num5;*/
        dummy.next = num5;
        dummy = dummy.next;

        ListNode num6 = new ListNode(2);
        /*num5.next = num6;*/
        dummy.next = num6;
        dummy = dummy.next;

        ListNode num7 = new ListNode(5);
        /*num6.next = num7;*/
        dummy.next = num7;
        dummy = dummy.next;

        printRawList(mergeTwoLists(list3.next, list4.next));
        System.out.println("\n=== End Raw Linkedlist ==\n");
    } // main

    /** Build-in Linkedlist implimentation **/
     /*
     * Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/
     * Purpose: Merge two sorted linked lists and return it as a sorted list.
     * Parameters: LinkedList<Integer> - the first linkedlist contains integer object
     *           : LinkedList<Integer> - a second linkedlist contains integer object
     * Returns: LinkedList<Integer> - a merge linkedlist
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
    } // mergeTwoSortedList

    private static void printList(LinkedList<Integer> printList){
        while(!printList.isEmpty()){
            System.out.print(printList.remove());
        }
    }// printList

    /** Raw Linkedlist implimentation **/
    /*
     * Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/
     * Purpose: Merge two sorted linked lists and return it as a sorted list.
     * Parameters: ListNode - the first linkedlist contains integer object
     *           : ListNode - a second linkedlist contains integer object
     * Returns: ListNode - a merge linkedlist
     * Post-Condition: none
     */
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode printList = new ListNode();

        // need dummy node becase if we simply use printList, printList hea
        // will point to end of the list after the merging process.
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
    } // mergeTwoLists

    private static void printRawList(ListNode printList){
        while(printList!=null){
            System.out.print(printList.val);
            printList = printList.next;
        }
    } // printRawList
}
