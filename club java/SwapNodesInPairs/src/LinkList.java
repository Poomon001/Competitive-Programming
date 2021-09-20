import java.util.LinkedList;

// Definition for singly-linked list class.
public class LinkList {
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
        System.out.println(" === Method 1 === \n");
        // declare LinkList
        LinkList list0 = new LinkList();

        // declare ListNode
        ListNode num1 = new ListNode(1);
        ListNode num2 = new ListNode(2);
        ListNode num3 = new ListNode(3);
        ListNode num4 = new ListNode(4);
        ListNode num5 = new ListNode(5);
        ListNode num6 = new ListNode(6);
        ListNode num7 = new ListNode(7);
        ListNode num8 = new ListNode(8);

        // Test cases
        list0.head = num1;
        num1.next = num2;
        num2.next = num3;
        num3.next = num4;
        num4.next = num5;
        num5.next = num6;
        num6.next = num7;
        num7.next = num8;

        myFuncRawLinkedList(swapNodesInPairs_M1(list0.head)); // 2->1->4->3->6->5->8->7

        System.out.println(" === Method 2 Round 1 === \n");

        // declare LinkList
        LinkList list1 = new LinkList();

        // declare ListNode
        num1 = new ListNode(1);
        num2 = new ListNode(2);
        num3 = new ListNode(3);
        num4 = new ListNode(4);
        num5 = new ListNode(5);
        num6 = new ListNode(6);
        num7 = new ListNode(7);
        num8 = new ListNode(8);

        // Test cases
        list1.head = num1;
        num1.next = num2;
        num2.next = num3;
        num3.next = num4;
        num4.next = num5;
        num5.next = num6;
        num6.next = num7;
        num7.next = num8;

        myFuncRawLinkedList(swapNodesInPairs_M2_R1(list1.head)); // 2->1->4->3->6->5->8->7

        System.out.println(" === Method 2 Round 2 === \n");

        LinkList list2 = new LinkList();

        // declare ListNode
        num1 = new ListNode(1);
        num2 = new ListNode(2);
        num3 = new ListNode(3);
        num4 = new ListNode(4);
        num5 = new ListNode(5);
        num6 = new ListNode(6);
        num7 = new ListNode(7);
        num8 = new ListNode(8);

        // Test cases
        list2.head = num1;
        num1.next = num2;
        num2.next = num3;
        num3.next = num4;
        num4.next = num5;
        num5.next = num6;
        num6.next = num7;
        num7.next = num8;

        myFuncRawLinkedList(swapNodesInPairs_M2_R2(list2.head));
    }

    /*
     * Link: https://leetcode.com/problems/swap-nodes-in-pairs/
     * Purpose: swap every two adjacent nodes.
     * Parameters: ListNode head - a head of integer linklist
     * Returns: ListNode - a head of integer swapped linklist
     * Pre-Conditions: The number of nodes in the list is in the range [0, 100].
     *               : 0 <= Node.val <= 100
     * Post-Condition: none
     */

    // Method 1: swap node
    public static ListNode swapNodesInPairs_M1(ListNode head){
        // to store the swapped linklist
        ListNode swapListNode = new ListNode(0);
        ListNode dummy = swapListNode;

        // to assist input linklist
        ListNode tempListNode = new ListNode(0);
        ListNode curr = tempListNode;

        // link temp node to the input node
        tempListNode.next = head;

        while(curr.next != null){
            // if there is even element, add it to the swapped list first
            if(curr.next.next != null) {
                ListNode newEvenNode = new ListNode(curr.next.next.val);
                dummy.next = newEvenNode;
                dummy = dummy.next;
            }

            // add odd element to the swapped list
            ListNode newOddNode = new ListNode(curr.next.val);
            dummy.next = newOddNode;
            dummy = dummy.next;

            // if there is next pair, move curr pointer to the next pair. Otherwise done
            if (curr.next.next != null){
                curr = curr.next.next;
            }else{
                break;
            }
        }
        return swapListNode.next;
    }

    /*
     * Link: https://leetcode.com/problems/swap-nodes-in-pairs/
     * Purpose: swap every two adjacent nodes.
     * Parameters: ListNode head - a head of integer linklist
     * Returns: ListNode - a head of integer swapped linklist
     * Pre-Conditions: The number of nodes in the list is in the range [0, 100].
     *               : 0 <= Node.val <= 100
     * Post-Condition: none
     */

    // Method 2: swap links - the first try (Round 1)
    public static ListNode swapNodesInPairs_M2_R1(ListNode head){
        // find length of the linklist
        int length = 0;
        ListNode front = head;
        while(front != null){
            front = front.next;
            length++;
        }

        // case 1: lenght is 0 or 1
        if(length == 0 || length == 1){
            return head;
        }

        // a pointer keeps track of all even and odd nodes
        ListNode even = head.next;
        ListNode odd = head;

        // a pointer that always point to the first element
        // even pointer will eventually swap to the front
        front = even;

        // case 2: length is not 0 or 1
        while (even.next != null && even.next.next != null) {
            // organize pointers (from pencil and paper works)
            odd.next = even.next.next;
            // dummy pointer to help manage odd pointer
            ListNode dummy = odd;
            odd = even.next;
            even.next = dummy;
            even = odd.next;
        }

        // organize the last two pointersat the end
        if(length%2 == 0){
            // even linklist
            even.next = odd;
            odd.next = null;
        }else{
            // odd linklist
            odd.next = even.next;
            even.next = odd;
        }

        return front;
    }

    /*
     * Link: https://leetcode.com/problems/swap-nodes-in-pairs/
     * Purpose: swap every two adjacent nodes.
     * Parameters: ListNode head - a head of integer linklist
     * Returns: ListNode - a head of integer swapped linklist
     * Pre-Conditions: The number of nodes in the list is in the range [0, 100].
     *               : 0 <= Node.val <= 100
     * Post-Condition: none
     */

    // Method 2: swap links - the second try (Round 2)
    public static ListNode swapNodesInPairs_M2_R2(ListNode head){
        ListNode dummy = new ListNode(0);
        ListNode prev = dummy;
        ListNode curr = head;

        // case 2: length is not 0 or 1
        while (curr != null && curr.next != null) {
            // organize pointers (from pencil and paper works)
            prev.next = curr.next;
            curr.next = curr.next.next;
            prev.next.next = curr;
            curr = curr.next;
            prev = prev.next.next;
        }

        return dummy.next;
    }

    public static void myFuncRawLinkedList(ListNode list){
        // print list
        while(list != null){
            System.out.print(list.val);
            if(list.next != null){
                System.out.print("->");
            }
            list = list.next;
        }
        System.out.println("\n");
    }
} // LinkList
