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
    Link: https://leetcode.com/problems/merge-in-between-linked-lists
    Purpose: Given two linked lists: list1 and list2 of sizes n and m respectively.
           : Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
    parameter: ListNode list1 - a head of linked list 1
             : int a - an integer
             : int b - an integer
             : ListNode list2 - a head of linked list 2
    return: ListNode list1 - a merged linked list
    Pre-Condition: 3 <= list1.length <= 10^4
                 : 1 <= a <= b < list1.length - 1
                 : 1 <= list2.length <= 10^4
    Post-Condition: None
'''
# brute force - run time: O(n), memory: O(1)
def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    h1 = list1
    h2 = list2
    t2 = list2
    i = 0

    while t2.next:
        t2 = t2.next

    while i <= b:
        if i == a - 1:
            temp = h1
            h1 = h1.next
            temp.next = h2
        elif i == b:
            t2.next = h1.next
        else:
            h1 = h1.next

        i += 1
    return list1

if __name__ == "__main__":
    root1 = ListNode(10)
    root1.next = ListNode(1)
    root1.next.next = ListNode(13)
    root1.next.next.next = ListNode(6)
    root1.next.next.next.next = ListNode(9)
    root1.next.next.next.next.next = ListNode(5)

    root2 = ListNode(100)
    root2.next = ListNode(101)
    root2.next.next = ListNode(102)
    root2.next.next.next = ListNode(103)

    root3 = ListNode(10)
    root3.next = ListNode(1)
    root3.next.next = ListNode(13)
    root3.next.next.next = ListNode(6)
    root3.next.next.next.next = ListNode(9)
    root3.next.next.next.next.next = ListNode(5)

    root4 = ListNode(100)
    root4.next = ListNode(101)
    root4.next.next = ListNode(102)
    root4.next.next.next = ListNode(103)

    root5 = ListNode(1)
    root5.next = ListNode(2)
    root5.next.next = ListNode(3)
    root5.next.next.next = ListNode(4)
    root5.next.next.next.next = ListNode(5)
    root5.next.next.next.next.next = ListNode(6)

    root6 = ListNode(100)
    root6.next = ListNode(101)
    root6.next.next = ListNode(102)
    root6.next.next.next = ListNode(103)
    root6.next.next.next.next = ListNode(104)

    root7 = ListNode(1)
    root7.next = ListNode(2)
    root7.next.next = ListNode(3)
    root7.next.next.next = ListNode(4)
    root7.next.next.next.next = ListNode(5)
    root7.next.next.next.next.next = ListNode(6)

    root8 = ListNode(100)
    root8.next = ListNode(101)
    root8.next.next = ListNode(102)
    root8.next.next.next = ListNode(103)
    root8.next.next.next.next = ListNode(104)

    root9 = ListNode(1)
    root9.next = ListNode(2)
    root9.next.next = ListNode(3)

    root10 = ListNode(100)

    mergeInBetween(root1, 3, 4, root2).printList() # 10 1 13 100 101 102 5
    mergeInBetween(root4, 2, 2, root3).printList() # 100 101 10 1 13 6 9 5 103
    mergeInBetween(root5, 2, 5, root6).printList()  # 1 2 100 101 102 103 104\
    mergeInBetween(root8, 1, 3, root7).printList()  # 100 1 2 3 4 5 6 104
    mergeInBetween(root9, 1, 2, root10).printList()  # 1 100 