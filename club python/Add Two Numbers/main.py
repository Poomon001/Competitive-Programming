from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        root = self
        while root:
            print(root.val, end=" ")
            root = root.next
        print("")

'''
    Link: https://leetcode.com/problems/add-two-numbers/description/
    Purpose: Find the sum of positive integer in two linked list
    parameter: Optional[ListNode] l1 - linked list of positive integer between 0 to 9
             : Optional[ListNode] l2 - linked list of positive integer between 0 to 9
    return: Optional[ListNode] - a linked list contains integers from a sum of l1 and l1
    Pre-Condition: The number of nodes in each linked list is in the range [1, 100].
                 : 0 <= Node.val <= 9
                 : It is guaranteed that the list represents a number that does not have leading zeros.
    Post-Condition: none
'''
# runtime: O(n), memory: O(1) exclude the answer
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # reverse two liked list
    root = ListNode(-1)
    dummy = root
    remainder = 0

    while l1 or l2:
        if l1 and l2:
            n = l1.val + l2.val + remainder
            l1 = l1.next
            l2 = l2.next
        elif l1 and not l2:
            n = l1.val + 0 + remainder
            l1 = l1.next
        elif not l1 and l2:
            n = 0 + l2.val + remainder
            l2 = l2.next

        remainder = 0

        if n > 9:
            remainder = 1
            n = int(str(n)[1])

        dummy.next = ListNode(n)
        dummy = dummy.next

    if remainder == 1:
        dummy.next = ListNode(1)

    return root.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list11 = ListNode(2)
    list11.next = ListNode(4)
    list11.next.next = ListNode(3)

    list12 = ListNode(5)
    list12.next = ListNode(6)
    list12.next.next = ListNode(4)

    addTwoNumbers(list11, list12).print() # 7 0 8
    addTwoNumbers(list12, list11).print() # 7 0 8

    list21 = ListNode(0)
    list22 = ListNode(0)

    addTwoNumbers(list21, list22).print() # 0

    list31 = ListNode(9)
    list31.next = ListNode(1)
    list32 = ListNode(3)

    addTwoNumbers(list31, list32).print() # 2 2

    list41 = ListNode(9)
    list42 = ListNode(3)
    list42.next = ListNode(1)

    addTwoNumbers(list41, list42).print() # 2 2

    list51 = ListNode(9)
    list51.next = ListNode(9)
    list51.next.next = ListNode(9)
    list51.next.next.next = ListNode(9)
    list51.next.next.next.next = ListNode(9)
    list51.next.next.next.next.next = ListNode(9)
    list51.next.next.next.next.next.next = ListNode(9)
    list52 = ListNode(9)
    list52.next = ListNode(9)
    list52.next.next = ListNode(9)
    list52.next.next.next = ListNode(9)

    addTwoNumbers(list51, list52).print()  # 8 9 9 9 0 0 0 1
    addTwoNumbers(list52, list51).print()  # 8 9 9 9 0 0 0 1

    list61 = ListNode(9)
    list61.next = ListNode(4)
    list61.next.next = ListNode(2)
    list62 = ListNode(9)
    list62.next = ListNode(4)
    list62.next.next = ListNode(6)
    list62.next.next.next = ListNode(5)

    addTwoNumbers(list61, list62).print()  # 8 9 8 5
    addTwoNumbers(list62, list61).print()  # 8 9 8 5


    


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
