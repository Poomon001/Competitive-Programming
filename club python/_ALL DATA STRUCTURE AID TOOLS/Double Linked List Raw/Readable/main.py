class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

'''
    Link: https://leetcode.com/problems/design-linked-list
    Purpose: Impliment Double Linked List
    Parameter:  None
    return: None
    Pre-Condition: 0 <= index, val <= 1000
                 : At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
    Post-Condition: runtime under O(n^2)
'''
class MyLinkedList:
    def __init__(self):
        # init two dummy to avoid edge cases
        self.head = ListNode(-1)
        self.tail = ListNode(-2)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    def get(self, index: int) -> int:
        dummy = self.head.next
        while index > 0 and dummy != self.tail:
            index -= 1
            dummy = dummy.next

        return -1 if dummy == self.tail else dummy.val

    # Add a node of value val before the first element of the linked list.
    # After the insertion, the new node will be the first node of the linked list.
    def addAtHead(self, val: int) -> None:
        node, right, left = ListNode(val), self.head.next, self.head
        right.prev = node
        node.next = right
        left.next = node
        node.prev = left

    # Append a node of value val as the last element of the linked list.
    def addAtTail(self, val: int) -> None:
        node, right, left = ListNode(val), self.tail, self.tail.prev
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right

    # Add a node of value val before the index th node in the linked list.
    # If index equals the length of the linked list, the node will be appended to the end of the linked list.
    # If index is greater than the length, the node will not be inserted.
    def addAtIndex(self, index: int, val: int) -> None:
        # add before the index
        dummy = self.head.next
        while index > 0 and dummy:
            index -= 1
            dummy = dummy.next

        # index is greater than the length, the node will not be inserted
        if dummy and index == 0:
            node, right, left = ListNode(val), dummy, dummy.prev
            left.next = node
            node.next = right
            node.prev = left
            right.prev = node

    # Delete the index th node in the linked list, if the index is valid.
    def deleteAtIndex(self, index: int) -> None:
        dummy = self.head.next
        while index > 0 and dummy:
            index -= 1
            dummy = dummy.next

        if dummy and index == 0 and self.tail != dummy:
            left, right = dummy.prev, dummy.next
            right.prev = left
            left.next = right


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("=== Create Linked List ll1 ===")
    ll1 = MyLinkedList()
    print(ll1.get(10)) # -1

    print("=== Add to Head ll1 ===")
    ll1.addAtHead(5)
    print(ll1.get(0)) # 5

    print("=== Add to Tail ll1 ===")
    ll1.addAtTail(7)
    print(ll1.get(0))  # 5
    print(ll1.get(1))  # 7

    print("=== Add At Index ll1 ===")
    ll1.addAtIndex(1, 6)
    print(ll1.get(0))  # 5
    print(ll1.get(1))  # 6
    print(ll1.get(2))  # 7

    print("=== Delete At Index ll1 ===")
    ll1.deleteAtIndex(1)
    print(ll1.get(0))  # 5
    print(ll1.get(1))  # 7
    print(ll1.get(2))  # -1

    print("\n=== Create Linked List ll2 ===")
    ll2 = MyLinkedList()
    print(ll2.get(0))  # -1

    print("=== Create Linked List ll2 ===")
    ll2.deleteAtIndex(0)
    print(ll2.get(0))  # -1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
