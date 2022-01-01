from typing import Optional

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    ''' note: <self> refers to the object of this class eg. self == ll '''
    ''' note2: <self> refers to a linked list but <self.next> refers to the first node of the list '''

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # insert the first element
        if self.head is None:
            self.head = Node(data, None)
            return

        # find the last node
        tail = self.head
        while(tail.next):
            tail = tail.next

        # point the last node to the new node
        tail.next = Node(data, None)

    def printLinkedList(self):
        if(self.head is None):
            print("Linked list is empty")
            return

        list = self.head
        while(list):
            print(list.data, end="-->")
            list = list.next

'''
    Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
    Purpose: Find the intersection of two linked list heads that may or may not share the same linked list. 
    parameter: Node headA - a linked list head
             : Node headB - a linked list head
    return: Optional[ListNode] - a head of the intersection if it is existing. Otherwise return none.
    Pre-Condition: The number of nodes of listA is in the m.
                 : The number of nodes of listB is in the n.
                 : 1 <= m, n <= 3 * 10^4
                 : 1 <= Node.val <= 10^5
    Post-Condition: none
'''
# run-time: O(n), memory: O(n)
def getIntersectionNode_M1(headA: Node, headB: Node) -> Optional[Node]:
    seen = set()
    while headA is not None:
        seen.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in seen:
            return headB
        headB = headB.next

    return None

'''
    Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
    Purpose: Find the intersection of two linked list heads that may or may not share the same linked list. 
    parameter: Node headA - a linked list head
             : Node headB - a linked list head
    return: Optional[ListNode] - a head of the intersection if it is existing. Otherwise return none.
    Pre-Condition: The number of nodes of listA is in the m.
                 : The number of nodes of listB is in the n.
                 : 1 <= m, n <= 3 * 10^4
                 : 1 <= Node.val <= 10^5
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def getIntersectionNode_M2(headA: Node, headB: Node) -> Optional[Node]:
    lengthA = 0
    lengthB = 0

    # find length A
    dummyA = headA
    while dummyA is not None:
        lengthA += 1
        dummyA = dummyA.next

    # find length B
    dummyB = headB
    while dummyB is not None:
        lengthB += 1
        dummyB = dummyB.next

    # match the length of 2 linked lists
    for _ in range(abs(lengthA - lengthB)):
        if lengthA > lengthB:
            headA = headA.next

        if lengthB > lengthA:
            headB = headB.next

    # find the intersection
    while headA is not None and headB is not None:
        if headA is headB:
            return headA
        else:
            headA = headA.next
            headB = headB.next

    return None

# to print linked list
def printLinkedList(node: Node):
    while node:
        if node.next:
            print(node.data, end=" -> ")
        else:
            print(node.data, end="\n")
        node = node.next


# main
if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_end(4)
    ll1.insert_at_end(1)
    ll1.insert_at_end(8)
    ll1.insert_at_end(4)
    ll1.insert_at_end(5)

    ll2 = LinkedList()
    ll2.insert_at_end(5)
    ll2.insert_at_end(6)
    ll2.insert_at_end(1)

    # make an intersection
    dummy1 = ll1.head
    dummy2 = ll2.head
    dummy1 = dummy1.next.next
    dummy2 = dummy2.next.next
    dummy2.next = dummy1

    ll3 = LinkedList()
    ll3.insert_at_end(1)
    ll3.insert_at_end(9)
    ll3.insert_at_end(1)
    ll3.insert_at_end(2)
    ll3.insert_at_end(4)

    ll4 = LinkedList()
    ll4.insert_at_end(3)

    # make an intersection
    dummy1 = ll3.head
    dummy2 = ll4.head
    dummy1 = dummy1.next.next.next
    dummy2.next = dummy1

    ll5 = LinkedList()
    ll5.insert_at_end(1)
    ll5.insert_at_end(2)
    ll5.insert_at_end(3)

    ll6 = LinkedList()
    ll6.insert_at_end(1)
    ll6.insert_at_end(2)

    print("\n+=== solution M1 ===+\n")
    printLinkedList(getIntersectionNode_M1(ll1.head, ll2.head)) # 8 -> 4 -> 5
    printLinkedList(getIntersectionNode_M1(ll3.head, ll4.head)) # 2 -> 4
    printLinkedList(getIntersectionNode_M1(ll5.head, ll6.head))  # no value because there is no intersection

    print("\n+=== solution M2 ===+\n")
    printLinkedList(getIntersectionNode_M2(ll1.head, ll2.head))  # 8 -> 4 -> 5
    printLinkedList(getIntersectionNode_M2(ll3.head, ll4.head))  # 2 -> 4
    printLinkedList(getIntersectionNode_M2(ll5.head, ll6.head))  # no value because there is no intersection