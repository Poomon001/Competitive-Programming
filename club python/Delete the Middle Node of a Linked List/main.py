from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printListNode(self):
        root = self
        while root:
            print(root.val, end = " ")
            root = root.next
        print("")

'''
    Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
    Purpose: Find a linked list that is removed the middle element
    parameter: Optional[ListNode] - head of a linked list
    return: Optional[ListNode] head of a linked list whose the middle node is removed
    Pre-Condition: The number of nodes in the list is in the range [2, 10^5].
                 : 1 <= Node.val <= 105
    Post-Condition: none
'''
# two pointers: runtime - O(n), memory - O(1)
def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None

    fast = head
    slow = head
    dummy = head
    while fast and fast.next:
        dummy = slow
        slow = slow.next
        fast = fast.next.next

    if slow.next:
        dummy.next = slow.next
    else:
        dummy.next = None

    return head


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(3)
    head1.next.next = ListNode(4)
    head1.next.next.next = ListNode(2)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)
    head2.next.next.next = ListNode(2)
    head2.next.next.next.next = ListNode(1)
    head2.next.next.next.next.next = ListNode(6)
    head2.next.next.next.next.next.next = ListNode(3)

    head3 = ListNode(1)
    head3.next = ListNode(2)

    deleteMiddle(head1).printListNode() # 1 3 2
    deleteMiddle(head2).printListNode() # 1 3 4 1 6 3
    deleteMiddle(head3).printListNode() # 1
