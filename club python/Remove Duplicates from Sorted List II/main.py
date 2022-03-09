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
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    Purpose: Given a sorted linked list. Delete all nodes that have duplicate numbers. 
           : eg: 1 -> 2 -> 2 -> 2 -> 3 -> 3 -> 4. return 1 -> 4
    parameter: Optional[Node] head - a head of a sorted linked list
    return: Optional[Node] - a head of a linked list which all duplicated nodes are deleted
    Pre-Condition: The number of nodes in the list is in the range [0, 300].
                 : -100 <= Node.val <= 100
                 : The list is guaranteed to be sorted in ascending order.
    Post-Condition: none
'''
# 3 pointer solutions: runtime: O(n), memory: O(1)
def deleteDuplicates_M1(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(-101, head)
    slow = fast = sentinel

    while head:
        # found duplicate
        if head.val == fast.val:
            # get slow pointer to a node before fast pointer
            while slow.next is not fast:
                slow = slow.next

            # move head forward until it find a new different node value
            while head and head.val == fast.val:
                head = head.next

            # remove all duplicates
            slow.next = head
        else:
            fast = head
            head = head.next

    return sentinel.next

'''
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    Purpose: Given a sorted linked list. Delete all nodes that have duplicate numbers. 
           : eg: 1 -> 2 -> 2 -> 2 -> 3 -> 3 -> 4. return 1 -> 4
    parameter: Optional[Node] head - a head of a sorted linked list
    return: Optional[Node] - a head of a linked list which all duplicated nodes are deleted
    Pre-Condition: The number of nodes in the list is in the range [0, 300].
                 : -100 <= Node.val <= 100
                 : The list is guaranteed to be sorted in ascending order.
    Post-Condition: none
'''
# 2 pointer solutions: runtime: O(n), memory: O(1)
def deleteDuplicates_M2(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(-101, head)
    temp = sentinel

    while head:
        # found duplicate
        if head.next and head.val == head.next.val:
            # move head to the last duplicate node
            while head.next and head.val == head.next.val:
                head = head.next

            # move temp to a node before the first duplicate node
            while temp.next.val != head.val:
                temp = temp.next

            # remove
            head = head.next
            temp.next = head
        else:
            head = head.next

    return sentinel.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(3)
    list1.next.next.next.next = ListNode(4)
    list1.next.next.next.next.next = ListNode(4)
    list1.next.next.next.next.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(3)
    list2.next.next.next = ListNode(3)
    list2.next.next.next.next = ListNode(4)
    list2.next.next.next.next.next = ListNode(4)
    list2.next.next.next.next.next.next = ListNode(4)

    list3 = ListNode(1)
    list3.next = ListNode(1)
    list3.next.next = ListNode(1)
    list3.next.next.next = ListNode(3)
    list3.next.next.next.next = ListNode(4)

    list4 = ListNode(1)

    print("\n+=== solution M1 ===+\n")
    deleteDuplicates_M1(list1).printList() # 1 2 5
    deleteDuplicates_M1(list2).printList() # 1 2
    deleteDuplicates_M1(list3).printList() # 3 4
    deleteDuplicates_M1(list4).printList() # 1

    print("\n+=== solution M2 ===+\n")
    deleteDuplicates_M2(list1).printList() # 1 2 5
    deleteDuplicates_M2(list2).printList() # 1 2
    deleteDuplicates_M2(list3).printList() # 3 4
    deleteDuplicates_M2(list4).printList() # 1
