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

        System.out.println("\n=== solution1: Build-in Linkedlist ==\n");
        printList(mergeTwoSortedList(list1, list2));
        System.out.println("\n=====\n");

        ListNode list3 = listNodeFromArray(new int[]{1,2,3,4});
        ListNode list4 = listNodeFromArray(new int[]{1,2,5});
        ListNode list7 = listNodeFromArray(new int[]{0,9});
        ListNode list8 = listNodeFromArray(new int[]{1,2,5});

        System.out.println("\n=== Solution2: new merge Linkedlist ==\n");
        printRawList(mergeTwoLists_m1(list3, list4));
        printRawList(mergeTwoLists_m1(list8, list7));
        System.out.println("\n=====\n");


        ListNode list5 = listNodeFromArray(new int[]{1,2,3,4});
        ListNode list6 = listNodeFromArray(new int[]{1,2,5});
        ListNode list9 = listNodeFromArray(new int[]{0,9});
        ListNode list10 = listNodeFromArray(new int[]{1,2,5});

        System.out.println("\n=== Solution3 inplace-merge Linkedlist ==\n");
        printRawList(mergeTwoLists_m2(list5, list6));
        printRawList(mergeTwoLists_m2(list9, list10));
        System.out.println("\n=====\n");
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
    // new node - runtime: O(n), memory: O(1)
    public static ListNode mergeTwoLists_m1(ListNode list1, ListNode list2) {
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

    /*
     * Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/
     * Purpose: Merge two sorted linked lists and return it as a sorted list.
     * Parameters: ListNode - the first linkedlist contains integer object
     *           : ListNode - a second linkedlist contains integer object
     * Returns: ListNode - a merge linkedlist
     * Post-Condition: none
     */
    // in-place - runtime: O(n), memory: O(1)
    public static ListNode mergeTwoLists_m2(ListNode list1, ListNode list2) {
        // if not last, then compare link1.node with link2.node
        ListNode prev = new ListNode(-1);
        prev.next = list1;
        ListNode head = prev;

        while(list1 != null && list2 != null){
            if(list2.val < list1.val) {
                prev.next = list2;
                prev = prev.next;
                list2 = list2.next;
                prev.next = list1;
            }else{
                prev = list1;
                list1 = list1.next;
            }
        }

        if(list1 == null) {
            prev.next = list2;
        }
        return head.next;
    }

    private static void printRawList(ListNode printList){
        while(printList!=null){
            System.out.print(printList.val);
            printList = printList.next;
        }
        System.out.println("");
    } // printRawList

    public static ListNode listNodeFromArray(int[] nums) {
        ListNode list = new ListNode();
        ListNode head = list;
        for(int i:nums){
            ListNode li = new ListNode(i);
            list.next = li;
            list = list.next;
        }
        return head.next;
    }
}
