from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
    Link: https://leetcode.com/problems/palindrome-linked-list/
    Purpose: Find if the linked list is a palindrome
    parameter: Optional[ListNode] - head
    return: bool - true if a linkedlist is is a palindrome, otherwise false
    Pre-Condition: The number of nodes in the list is in the range [1, 105].
                 : 0 <= Node.val <= 9
    Post-Condition: none
'''
# runtime - O(n), memory - O(1)
def isPalindrome(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head

    # find the half
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # reverse second half
    reverse = slow
    i = slow.next
    reverse.next = None
    while i is not None:
        j = i
        i = i.next
        j.next = reverse
        reverse = j

    i = reverse

    # check palindrome
    while i is not None and head is not None:
        if i.val == head.val:
            head = head.next
            i = i.next
        else:
            return False

    return True

if __name__ == '__main__':
    head0 = ListNode(1)

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(2)
    head1.next.next.next = ListNode(1)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(2)

    head3 = ListNode(1)
    head3.next = ListNode(2)
    head3.next.next = ListNode(3)
    head3.next.next.next = ListNode(2)
    head3.next.next.next.next = ListNode(1)

    head4 = ListNode(1)
    head4.next = ListNode(2)
    head4.next.next = ListNode(3)
    head4.next.next.next = ListNode(2)
    head4.next.next.next.next = ListNode(2)

    print(isPalindrome(head0))  # true
    print(isPalindrome(head1)) # true
    print(isPalindrome(head2))  # False
    print(isPalindrome(head3))  # true
    print(isPalindrome(head4))  # False