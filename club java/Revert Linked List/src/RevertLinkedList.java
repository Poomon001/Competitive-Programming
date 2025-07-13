import java.util.LinkedList;

// Definition for singly-linked list class.
public class RevertLinkedList {
    /* Node Class */
    ListNode head; // head of list
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
        /** Raw Test Case **/
        // declare LinkList
        RevertLinkedList list3 = new RevertLinkedList();

        // declare ListNode
        ListNode num1 = new ListNode(7);
        ListNode num2 = new ListNode(6);
        ListNode num3 = new ListNode(5);
        ListNode num4 = new ListNode(4);
        ListNode num5 = new ListNode(3);
        ListNode num6 = new ListNode(2);
        ListNode num7 = new ListNode(1);

        // connect node
        list3.head = num1;
        num1.next = num2;
        num2.next = num3;
        num3.next = num4;
        num4.next = num5;
        num5.next = num6;
        num6.next = num7;

        myFuncRawLinkedList_M1(revertLinkedList(list3.head));
    }

    /*
     * Link: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3966/
     * Purpose: Find a reversed Linked list
     * Parameters: ListNode head - a head pointer to a single linked list
     * Returns: ListNode reversedList - a head pointer to a reversed single linked list
     * Pre-Condition: The number of nodes in the list is the range [0, 5000].
                    : -5000 <= Node.val <= 5000
       Post-Condition : None
     */
    public static ListNode revertLinkedList(ListNode head) {
        // no need to reverse if head is null or there is only 1 node.
        if (head == null) {
            return head;
        }

        // unlink and prepare a reverse head
        ListNode reversedList = head;
        head = head.next;
        reversedList.next = null;

        while(head != null){
            ListNode dummy = head.next;
            head.next = reversedList;
            reversedList = head;
            head = dummy;
        }

        return reversedList;
    }

    public static void myFuncRawLinkedList_M1(ListNode list){
        // print list
        while(list != null){
            System.out.println(list.val);
            list = list.next;
        }
        System.out.println("=== End Raw LinkedList_M1 === \n");
    }
} // LinkList

