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
    Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list
    Purpose: Given the head of a linked list, remove the nth node from the end of the list and return its head.
    parameter: Optional[ListNode] head - a head of linked list
    return: int n - an integer
    Pre-Condition: The number of nodes in the list is sz.
                 : 1 <= size <= 30
                 : 0 <= Node.val <= 100
                 : 1 <= n <= size
    Post-Condition: None
'''
# brute force - run time: O(n), memory: O(1)
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    slow = head
    temp = slow
    dist = 0

    # make the distance between fast and slow pointer in n nodes
    # move fast until reach the end
    while fast:
        fast = fast.next
        if dist >= n:
            temp = slow
            slow = slow.next
        dist += 1

    if slow == head:
        head = head.next
    else:
        temp.next = slow.next

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
    root4.next.next = ListNode(3)
    root4.next.next.next = ListNode(4)
    root4.next.next.next.next = ListNode(5)

    root5 = ListNode(1)
    root5.next = ListNode(2)
    root5.next.next = ListNode(3)
    root5.next.next.next = ListNode(4)
    root5.next.next.next.next = ListNode(5)

    root6 = ListNode(1)
    root6.next = ListNode(2)

    root7 = ListNode(1)
    root7.next = ListNode(2)

    print(removeNthFromEnd(root1, 1)) # None
    removeNthFromEnd(root2, 2).printList() # 1 2 4
    removeNthFromEnd(root3, 3).printList() # 1 2 4 5
    removeNthFromEnd(root4, 1).printList() # 1 2 3 4
    removeNthFromEnd(root5, 5).printList() # 2 3 4 5
    removeNthFromEnd(root6, 2).printList() # 2
    removeNthFromEnd(root7, 1).printList() # 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
