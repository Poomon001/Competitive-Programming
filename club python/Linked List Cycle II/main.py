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
        while (tail.next):
            tail = tail.next

        # point the last node to the new node
        tail.next = Node(data, None)

    def printLinkedList(self):
        if (self.head is None):
            print("Linked list is empty")
            return

        list = self.head
        while (list):
            print(list.data, end="-->")
            list = list.next

'''
    Link: https://leetcode.com/problems/linked-list-cycle-ii/
    Purpose: Determine the first node of a cycle in a linked list. Return None if there is no cycle.
    parameter: Optional[Node] - a linked list node containing integer node(s)
    return: Node slow - the first node of the cycle. None if there is no cycle
    Pre-Condition: The number of the nodes in the list is in the range [0, 10^4].
                 : -10^5 <= Node.val <= 10^5
                 : pos is -1 or a valid index in the linked-list.
    Post-Condition: none
'''
# using hashtable solution - runtime: O(n), memory: O(n)
def detectCycle_M1(head: Node) -> Node:
    # {node location}
    seen = set()
    slow = head
    while (slow is not None and slow.next is not None):
        # store all seen node in a set
        seen.add(slow)

        # move slow pointer
        slow = slow.next

        # if we roop back to a seen node, return the index of the node
        if slow in seen:
            return slow

    return None

'''
    Link: https://leetcode.com/problems/linked-list-cycle-ii/
    Purpose: Determine the first node of a cycle in a linked list. Return None if there is no cycle.
    parameter: Optional[Node] - a linked list node containing integer node(s)
    return: Node slow - the first node of the cycle. None if there is no cycle
    Pre-Condition: The number of the nodes in the list is in the range [0, 10^4].
                 : -10^5 <= Node.val <= 10^5
                 : pos is -1 or a valid index in the linked-list.
    Post-Condition: none
'''
# Using fast and slow pointers solution - runtime: O(n), memory: O(1)
def detectCycle_M2(head: Node) -> Node or str:
    slow = head
    fast = head
    while (fast is not None and fast.next is not None):
        # move fast pointer
        fast = fast.next.next

        # move slow pointer
        slow = slow.next

        # we found a loop
        if fast is slow:
            # reset slow to head
            slow = head

            # this is still O(n) tun-time because the if statement will get execute only once
            # when fast == slow node, it is the first node of the loop because
            # The remaining steps to the beginning is equal to the steps from beginning to the cycle
            while (slow != fast):
                slow = slow.next
                fast = fast.next
            return slow

    return "None"


# main
if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_end(1)
    ll1.insert_at_end(1)
    ll1.insert_at_end(1)
    ll1.insert_at_end(1)
    print("solution M1:",detectCycle_M1(ll1.head))  # None
    print("solution M2:", detectCycle_M2( ll1.head))  # None
    print("\n+==== end ll1 ====+\n")

    ll2 = LinkedList()
    ll2.insert_at_end(1)
    ll2.insert_at_end(2)
    print("solution M1:", detectCycle_M1(ll2.head))  # None
    print("solution M2:", detectCycle_M2( ll2.head))  # None
    print("\n+==== end ll2 (without loop) ====+\n")
    # create a loop
    dummy = ll2.head
    dummy = dummy.next
    dummy.next = ll2.head
    print("solution M1:", detectCycle_M1(ll2.head).data)  # 1
    print("solution M2:",detectCycle_M2( ll2.head).data)  # 1
    print("\n+==== end ll2 (with loop) ====+\n")

    ll3 = LinkedList()
    ll3.insert_at_end(3)
    ll3.insert_at_end(2)
    ll3.insert_at_end(0)
    ll3.insert_at_end(3)
    # create a loop
    dummy = ll3.head
    dummy.next.next.next = ll3.head
    print("solution M1:",detectCycle_M1(ll3.head).data)  # 3
    print("solution M2:",detectCycle_M2( ll3.head).data)  # 3
    print("\n+==== end ll3 ====+\n")

    ll4 = LinkedList()
    ll4.insert_at_end(1)
    print("solution M1:",detectCycle_M1(ll4.head))  # None
    print("solution M2:",detectCycle_M2( ll4.head))  # None
    print("\n+==== end ll4 ====+\n")
