public class ReveredSingleLinkedlist {
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
        // test drivers //
        /** Raw LinkedList **/
        ListNode list1 = new ListNode();
        ListNode dummy = list1;

        // add new nodes to the linked list
        ListNode num1 = new ListNode(1);
        dummy.next = num1;
        dummy = dummy.next;

        ListNode num2 = new ListNode(2);
        dummy.next = num2;
        dummy = dummy.next;

        ListNode num3 = new ListNode(3);
        dummy.next = num3;
        dummy = dummy.next;

        ListNode num4 = new ListNode(4);
        dummy.next = num4;
        dummy = dummy.next;

        ListNode num5 = new ListNode(5);
        dummy.next = num5;
        dummy = dummy.next;

        printLinkedList(reverseLinkedList(list1.next));
    }

    // ref - https://www.educative.io/courses/coderust-hacking-the-coding-interview/lq2j
    // reverse linked list
    private static ListNode reverseLinkedList(ListNode head){
        // no need to reverse if head is null or there is only 1 node.
        if (head == null || head.next == null) {
            return head;
        }

        ListNode toDo = head.next;
        ListNode reversedList = head;

        // this will be the "tail" of the list
        reversedList.next = null;

        // reversing process
        while (toDo != null) {
            ListNode dummy = toDo;
            toDo = toDo.next;
            dummy.next = reversedList;

            // set reversedList to initial state
            reversedList = dummy;
        }

        return reversedList;
    }

    // print linkedlist
    private static boolean printLinkedList(ListNode list){
        while(list != null){
            System.out.println(list.val);
            list = list.next;
        }
        return false;
    } // printLinkedList
} // ReveredSingleLinkedList
