from typing import Optional

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
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

def printLinkedList(head):
    if(head is None):
        print("Linked list is empty")
        return

    list = head
    while(list):
        print(list.data, end="-->")
        list = list.next

    print("")

'''
    Link: https://leetcode.com/problems/middle-of-the-linked-list/
    Purpose: Find the middle node of the linked list.
    parameter: Optional[Node] head - a linked list node containing integer node(s)
    return: Optional[Node] slowPointer - the middle node of the linked list.
    Pre-Condition: The number of nodes in the list is in the range [1, 100].
                 : 1 <= Node.val <= 100
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def middleNode(head: Optional[Node]) -> Optional[Node]:
    fastPointer = head
    slowPointer = head

    while fastPointer is not None and fastPointer.next is not None:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next

    return slowPointer

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_end(1)
    ll1.insert_at_end(0)
    printLinkedList(middleNode(ll1.head)) # 0

    ll2 = LinkedList()
    ll2.insert_at_end(1)
    ll2.insert_at_end(2)
    ll2.insert_at_end(3)
    ll2.insert_at_end(4)
    ll2.insert_at_end(5)
    printLinkedList(middleNode(ll2.head)) # 3,4,5

    ll3 = LinkedList()
    ll3.insert_at_end(1)
    ll3.insert_at_end(2)
    ll3.insert_at_end(3)
    ll3.insert_at_end(4)
    ll3.insert_at_end(5)
    ll3.insert_at_end(6)
    printLinkedList(middleNode(ll3.head))  # 4,5,6

    ll4 = LinkedList()
    ll4.insert_at_end(3)
    printLinkedList(middleNode(ll4.head))  # 3

