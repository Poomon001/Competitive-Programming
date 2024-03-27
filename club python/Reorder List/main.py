from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        root = self
        while root:
            print(root.val, end=" ")
            root = root.next

        print("")

'''
    Link: https://leetcode.com/problems/reorder-list
    Purpose: Given Linked List, reorder them (L0 → L1 → … → Ln - 1 → Ln) such that L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    parameter: Optional[ListNode] head - a head of linked list
    return: Optional[ListNode] head - a new ordered linked list
    Pre-Condition: The number of nodes in the list is in the range [1, 5 * 10^4].
                 : 1 <= Node.val <= 1000
    Post-Condition: The input linked list must be in the new order
'''
# run time: O(n), memory: O(1)
def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # find second half
    half = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        half = half.next

    # revere second half
    reversedHead = half
    reversedHead = reversedHead.next
    half.next = None
    while reversedHead:
        temp = reversedHead
        reversedHead = reversedHead.next
        temp.next = half
        half = temp

    # match head and tail, so on ...
    start = head
    while start != half and start.next != half:
        t1 = start
        t2 = half
        start = start.next
        half = half.next
        t1.next = t2
        t2.next = start

    return head


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = ListNode(1)

    root2 = ListNode(1)
    root2.next = ListNode(2)
    root2.next.next = ListNode(3)
    root2.next.next.next = ListNode(4)

    root3 = ListNode(1)
    root3.next = ListNode(2)
    root3.next.next = ListNode(3)
    root3.next.next.next = ListNode(4)
    root3.next.next.next.next = ListNode(5)

    root4 = ListNode(1)
    root4.next = ListNode(2)

    reorderList(root1).printList() # 1
    reorderList(root2).printList() # 1 4 2 3
    reorderList(root3).printList() # 1 5 2 4 3
    reorderList(root4).printList() # 1 2
