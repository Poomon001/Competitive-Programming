from typing import Optional

class Node:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

'''
    Link: https://leetcode.com/problems/swap-nodes-in-pairs/
    Purpose: Given a linked list, swap every two adjacent nodes
    parameter: Optional[Node] head - a head of a linked list
    return: Optional[Node] - a head of a swapped linked list
    Pre-Condition: The number of nodes in the list is in the range [0, 100].
                 : 0 <= Node.val <= 100
    Post-Condition: none
'''
def swapPairs(head: Optional[Node]) -> Optional[Node]:
    """
    :type head: ListNode
    :rtype: ListNode
    """
    front = Node(None, head)
    prev = front
    curr = head

    while curr and curr.next:
        prev.next = curr.next
        curr.next = curr.next.next
        prev.next.next = curr
        prev = curr
        curr = curr.next

    return front.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    dummy = swapPairs(head)
    while dummy:
        print(dummy.val, end=" ") # 2 1 4 3
        dummy = dummy.next

    print("")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    dummy = swapPairs(head)
    while dummy:
        print(dummy.val, end=" ") # 2 1 3
        dummy = dummy.next

    print("")

    head = Node(1)
    dummy = swapPairs(head)
    while dummy:
        print(dummy.val, end=" ")  # 1
        dummy = dummy.next

    print("")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    dummy = swapPairs(head)
    while dummy:
        print(dummy.val, end=" ")  # 2 1 4 3 5
        dummy = dummy.next

