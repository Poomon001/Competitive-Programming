from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    Purpose: Remove all duplicate node in a linked list
    parameter: Optional[Node] head - a head of a linked list
    return: Optional[Node] - a head of the linked list without any duplicate node
    Pre-Condition: The number of nodes in the list is in the range [0, 300].
                 : -100 <= Node.val <= 100
                 : The list is guaranteed to be sorted in ascending order.
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def deleteDuplicates(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return head

    front = Node(None, head)
    prev = head
    curr = head.next

    while curr:
        if curr.val == prev.val:
            curr = curr.next
            prev.next = curr
        else:
            prev = prev.next
            curr = curr.next

    return front.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(9)
    dummy = deleteDuplicates(head)
    while dummy:
        print(dummy.val, end=" ")  # 1 3 4 9
        dummy = dummy.next

    print("")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    dummy = deleteDuplicates(head)
    while dummy:
        print(dummy.val, end=" ")  # 1 2
        dummy = dummy.next

    print("")

    head = Node(1)
    head.next = Node(1)
    dummy = deleteDuplicates(head)
    while dummy:
        print(dummy.val, end=" ")  # 1
        dummy = dummy.next

    print("")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    dummy = deleteDuplicates(head)
    while dummy:
        print(dummy.val, end=" ")  # 1 2 3 4 5
        dummy = dummy.next

