from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

'''
    Link: https://leetcode.com/problems/sort-list/
    Purpose: return the list after sorting it in ascending order
    parameter: Optional[Node] head - a head of a linked list
    return: Optional[Node] - a head of a sorted linked list
    Pre-Condition: The number of nodes in the list is in the range [0, 5 * 104].
                 : -10^5 <= Node.val <= 10^5
    Post-Condition: none
'''

# runtime: O(n), memory: O(n)
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = head
    length = 0
    while dummy:
        length += 1
        dummy = dummy.next

    if length <= 1:
        return head

    # divide
    left = head
    dummy = head
    right = head
    for _ in range((length // 2)):
        right = right.next

    for _ in range((length // 2) - 1):
        dummy = dummy.next
    dummy.next = None

    left = sortList(left)
    right = sortList(right)

    return mergeTwoSortedList(left, right)

''' merge two sorted linked lists '''
# runtime: O(n), memory: O(n)
def mergeTwoSortedList(h1, h2):
    h3 = ListNode(0)
    d1 = h1
    d2 = h2
    d3 = h3

    while d2 and d1:
        if d1.val > d2.val:
            d3.next = ListNode(d2.val)
            d3 = d3.next
            d2 = d2.next
        else:
            d3.next = ListNode(d1.val)
            d3 = d3.next
            d1 = d1.next

    while d2:
        d3.next = ListNode(d2.val)
        d3 = d3.next
        d2 = d2.next

    while d1:
        d3.next = ListNode(d1.val)
        d3 = d3.next
        d1 = d1.next
    return h3.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = ListNode(10)
    head.next = ListNode(9)
    head.next.next = ListNode(8)
    head.next.next.next = ListNode(7)
    dummy = sortList(head)
    while dummy:
        print(dummy.val, end=" ") # 7 8 9 10
        dummy = dummy.next

    print("")

    head = ListNode(3)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    dummy = sortList(head)
    while dummy:
        print(dummy.val, end=" ") # 1 2 3
        dummy = dummy.next

    print("")

    head = ListNode(1)
    dummy = sortList(head)
    while dummy:
        print(dummy.val, end=" ")  # 1
        dummy = dummy.next

    print("")

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(1)
    dummy = sortList(head)
    while dummy:
        print(dummy.val, end=" ")  # 1 1 1 2 3 3
        dummy = dummy.next

