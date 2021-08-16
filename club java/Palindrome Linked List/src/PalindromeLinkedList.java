import java.util.LinkedList;

// Definition for singly-linked list class.
class PalindromeLinkedList {
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

        ListNode num4 = new ListNode(2);
        dummy.next = num4;
        dummy = dummy.next;

        ListNode num5 = new ListNode(1);
        dummy.next = num5;
        dummy = dummy.next;

        System.out.println(palindromeLinkedList(list1.next));
    }

    /*
     * Link: https://leetcode.com/problems/palindrome-linked-list/submissions/
     * Purpose: Determine if the Given the head of a singly linked list is a palindrome.
     * Parameters: ListNode - a head pointer to a single linked list
     * Returns: boolean - true if a singly linked list is a palindrome, otherwise false.
     * Pre-Condition: The number of nodes in the list is in the range [1, 10^5].
                    : 0 <= Node.val <= 9
       Post-Condition : O(n) time and O(1) space
     */
    public static boolean palindromeLinkedList(ListNode head){
        ListNode fast = head;
        ListNode slow = head;

        // get to the middle of the linked list
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode newHead = reverseLinkedList(slow);;

        // since we reversed the second half of the linked list
        // now we have the first half. And the second half is in the revered order
        // we can check if both first and second half metch to each other or not
        while(newHead != null && head != null){

            // one element does not match then the linked list is not palindrome
            if(newHead.val != head.val){
                return false;
            }
            newHead = newHead.next;
            head = head.next;
        }

        // all elements match, then it is palindrome
        return true;
    }

    // ref - https://www.educative.io/courses/coderust-hacking-the-coding-interview/lq2j
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

    private static boolean printLinkedList(ListNode list){
        while(list != null){
            System.out.println(list.val);
            list = list.next;
        }
        return false;
    }
}

