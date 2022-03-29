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
    Link: https://leetcode.com/problems/odd-even-linked-list/
    Purpose: Group all the nodes with odd indices together followed by the nodes with even indices
    parameter: Optional[ListNode] head - a head of a linked list 
    return: Optional[ListNode] - a head of a result linked list
    Pre-Condition: n == number of nodes in the linked list
                 : 0 <= n <= 104
                 : -10^6 <= Node.val <= 10^6
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def oddEvenList_M1(head: Optional[ListNode]) -> Optional[ListNode]:

    if head is None:
        return head

    if head.next is None:
        return head
    init = ListNode(0)
    init.next = head

    ans = ListNode(0)
    dummy = init.next.next
    dummy2 = ans

    # odd
    while head and head.next:
        dummy2.next = ListNode(head.val)
        dummy2 = dummy2.next
        head = head.next.next

    if head:
        dummy2.next = ListNode(head.val)
        dummy2 = dummy2.next

    # even
    head = init.next.next
    while head and head.next:
        dummy2.next = ListNode(head.val)
        dummy2 = dummy2.next
        head = head.next.next

    if head:
        dummy2.next = ListNode(head.val)
        dummy2 = dummy2.next

    return ans.next

'''
    Link: https://leetcode.com/problems/odd-even-linked-list/
    Purpose: Group all the nodes with odd indices together followed by the nodes with even indices
    parameter: Optional[ListNode] head - a head of a linked list 
    return: Optional[ListNode] - a head of a result linked list
    Pre-Condition: n == number of nodes in the linked list
                 : 0 <= n <= 104
                 : -10^6 <= Node.val <= 10^6
    Post-Condition: none
'''
# runtime: O(n), memory: O(n)
def oddEvenList_M2(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head

    if head.next is None:
        return head

    init = ListNode(0, head)

    # point to the even position
    even = init.next.next

    # head of even linked list
    evenHead = even

    while head and even:
        # get odd linked list
        if head.next is not None:
            head.next = head.next.next

        # get even linked list
        if even.next is not None:
            even.next = even.next.next
        else:
            even.next = None
            break

        even = even.next
        head = head.next

    head.next = evenHead

    return init.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root1 = ListNode(1)
    root1.next = ListNode(2)
    root1.next.next = ListNode(3)
    root1.next.next.next = ListNode(4)
    root1.next.next.next.next = ListNode(5)
    root1.next.next.next.next.next = ListNode(6)

    root2 = ListNode(1)
    root2.next = ListNode(2)
    root2.next.next = ListNode(3)
    root2.next.next.next = ListNode(4)
    root2.next.next.next.next = ListNode(5)

    root3 = ListNode(1)

    print("+=== solution 1 ===+")
    oddEvenList_M1(root1).printList() # 1 3 5 2 4 6
    oddEvenList_M1(root2).printList() # 1 3 5 2 4
    oddEvenList_M1(root3).printList() # 1

    print("+=== solution 2 ===+")
    oddEvenList_M2(root1).printList() # 1 3 5 2 4 6
    oddEvenList_M2(root2).printList() # 1 3 5 2 4
    oddEvenList_M2(root3).printList() # 1
