from typing import Optional


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    '''     
        Purpose: insert an integer at the front of the list
        Parameter: int data - an integer
        Returns: none
        Pre-Condition: data is an integer
        Post-Condition: none
    '''
    def insert_at_beginning(self, data):
        # create a node
        node = Node(data, self.head)

        # make this node as a head
        self.head = node

    '''     
        Link: https://leetcode.com/problems/remove-linked-list-elements/
        Purpose: remove all the nodes of the linked list that has Node.val == val
        Parameter: int val - an integer
        Returns: none
        Pre-Condition: The number of nodes in the list is in the range [0, 104].
                     : 1 <= Node.val <= 50
                     : 0 <= val <= 50
        Post-Condition: none
    '''
    def removeAllElements(self, val: int) -> None:
        dummy = Node(-1)
        dummy.next = self.head
        self.head = dummy

        while dummy.next:
            # remove all matching numbers on the middle
            if dummy.next.data == val:
                dummy.next = dummy.next.next;
            # remove the matching number at the end of the linklist
            elif dummy.next.data == val and not dummy.next.next:
                dummy.next = None
            else:
                dummy = dummy.next

        self.head = self.head.next

    '''     
        Purpose: print a linklist
        Parameter: none
        Returns: none
        Pre-Condition: none
        Post-Condition: none
    '''
    def printLinkedList(self):
        if self.head is None:
            return

        dummy = self.head
        while dummy:
            print(dummy.data, end="-->")
            dummy = dummy.next



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_beginning(1)
    ll1.insert_at_beginning(1)
    ll1.insert_at_beginning(12)
    ll1.insert_at_beginning(1)
    ll1.insert_at_beginning(76)
    ll1.insert_at_beginning(1)
    ll1.insert_at_beginning(1)
    ll1.removeAllElements(1)
    ll1.printLinkedList()
