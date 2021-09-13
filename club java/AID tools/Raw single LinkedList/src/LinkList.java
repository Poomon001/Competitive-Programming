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
        // test drivers //
        /** Raw LinkedList: method 1 **/
        ListNode list1 = new ListNode();
        ListNode dummy = list1;

        // add new nodes to the linked list
        ListNode num1 = new ListNode(1);
        /*list1.next = num1;*/
        dummy.next = num1;
        dummy = dummy.next; // same as <dummy = num1>

        ListNode num2 = new ListNode(2);
        /*num1.next = num2;*/
        dummy.next = num2;
        dummy = dummy.next; // same as <dummy = num2>

        ListNode num3 = new ListNode(3);
        /*num2.next = num3;*/
        dummy.next = num3;
        dummy = dummy.next; // same as <dummy = num3>

        ListNode num4 = new ListNode(4);
        /*num3.next = num4;*/
        dummy.next = num4;
        dummy = dummy.next; // same as <dummy = num4>

        myFuncRawLinkedList_M1(list1.next);

        /** build-in LinkedList **/
        // add new nodes to the linked list
        LinkedList<Integer> list2 = new LinkedList<Integer>();
        list2.add(6);
        list2.add(7);
        list2.add(8);
        list2.add(9);

        myFuncBuildInLinkedList(list2);

        /** Raw LinkedList: method 2 **/
        // declare LinkList
        LinkList list3 = new LinkList();

        // declare ListNode
        ListNode num5 = new ListNode(5);
        ListNode num6 = new ListNode(6);
        ListNode num7 = new ListNode(7);

        // connect node
        list3.head = num5;
        num5.next = num6;
        num6.next = num7;

        /*myFuncRawLinkedList_M1(list3.head);*/
        myFuncRawLinkedList_M2(list3);
    }

    public static void myFuncRawLinkedList_M1(ListNode list){
        // print list
        while(list != null){
            System.out.println(list.val);
            list = list.next;
        }
        System.out.println("=== End Raw LinkedList_M1 === \n");
    }

    public static void myFuncBuildInLinkedList(LinkedList list){
        // print list
        while(!list.isEmpty()){
            System.out.println(list.pop());
        }
        System.out.println("=== End build-in LinkedList === \n");
    }

    public static void myFuncRawLinkedList_M2(LinkList list){
        ListNode n = list.head;
        // print list
        while(n != null){
            System.out.println(n.val);
            n = n.next;
        }
        System.out.println("=== End Raw LinkedList_M2 === \n");
    }
} // LinkList

