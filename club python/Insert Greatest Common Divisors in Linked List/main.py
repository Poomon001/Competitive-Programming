import math
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self):
        temp = self
        list = []
        while temp:
            list.append(temp.val)
            temp = temp.next
        return list

def toListNode(nums: List[int]) -> Optional[ListNode]:
    head = ListNode(0)
    dummy = head
    for num in nums:
        dummy.next = ListNode(num)
        dummy = dummy.next
    return head.next

def gcd(a: int, b: int) -> int:
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a

'''
    Link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
    Purpose: Given a linked list of int nodes, insert gcd node between each pair of node.
    parameter: Optional[ListNode] head - a head of the linked list
    return: Optional[ListNode] head - a head of the result linked list
    Pre-Condition: The number of nodes in the list is in the range [1, 5000].
                 : 1 <= Node.val <= 1000
    Post-Condition: none
'''
# auto gcd - runtime: O(n), space: O(1)
def insertGreatestCommonDivisors_m1(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = head
    while dummy.next:
        new_node = ListNode(math.gcd(dummy.val, dummy.next.val))
        temp = dummy.next
        dummy.next = new_node
        new_node.next = temp
        dummy = temp
    return head

'''
    Link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
    Purpose: Given a linked list of int nodes, insert gcd node between each pair of node.
    parameter: Optional[ListNode] head - a head of the linked list
    return: Optional[ListNode] head - a head of the result linked list
    Pre-Condition: The number of nodes in the list is in the range [1, 5000].
                 : 1 <= Node.val <= 1000
    Post-Condition: none
'''
# manual gcd - runtime: O(n), space: O(1)
def insertGreatestCommonDivisors_m2(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = head
    while dummy.next:
        new_node = ListNode(gcd(dummy.val, dummy.next.val))
        temp = dummy.next
        dummy.next = new_node
        new_node.next = temp
        dummy = temp
    return head

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    list1 = toListNode([18,6,10,3])
    print(insertGreatestCommonDivisors_m1(list1).toList()) # [18,6,6,2,10,1,3]

    list2 = toListNode([7])
    print(insertGreatestCommonDivisors_m1(list2).toList())  # [7]

    list3 = toListNode([18,6,10,3,12])
    print(insertGreatestCommonDivisors_m1(list3).toList())  # [18, 6, 6, 2, 10, 1, 3, 3, 12]

    print("\n === Solution 2 === \n")
    list1 = toListNode([18, 6, 10, 3])
    print(insertGreatestCommonDivisors_m2(list1).toList())  # [18,6,6,2,10,1,3]

    list2 = toListNode([7])
    print(insertGreatestCommonDivisors_m2(list2).toList())  # [7]

    list3 = toListNode([18, 6, 10, 3, 12])
    print(insertGreatestCommonDivisors_m2(list3).toList())  # [18, 6, 6, 2, 10, 1, 3, 3, 12]

