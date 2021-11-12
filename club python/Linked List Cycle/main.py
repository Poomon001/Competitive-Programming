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

# runtime: O(n), memory: O(1)
def hasCycle(head: Optional[Node]) -> bool:
    fast = head
    slow = head
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if fast is not None and slow is not None:
            if fast is slow:
                return True

    return False

# main
if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_end(1)
    ll1.insert_at_end(1)
    ll1.insert_at_end(1)
    ll1.insert_at_end(1)
    print(hasCycle(ll1.head)) # false

    ll2 = LinkedList()
    ll2.insert_at_end(1)
    ll2.insert_at_end(2)
    print(hasCycle(ll2.head)) # false
    # create a loop
    dummy = ll2.head
    dummy = dummy.next
    dummy.next = ll2.head
    print(hasCycle(ll2.head)) # true

    ll3 = LinkedList()
    ll3.insert_at_end(3)
    ll3.insert_at_end(2)
    ll3.insert_at_end(0)
    ll3.insert_at_end(3)
    # create a loop
    dummy = ll3.head
    dummy.next.next.next = ll2.head
    print(hasCycle(ll3.head)) # true

    ll4 = LinkedList()
    ll4.insert_at_end(1)
    print(hasCycle(ll4.head)) # false
