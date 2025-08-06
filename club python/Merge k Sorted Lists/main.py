import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        while self:
            print(self.val, end="->" if self.next else "\n")
            self = self.next

def build_list(vals) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

'''
    Link: https://leetcode.com/problems/merge-k-sorted-lists
    Purpose: Find the merged sorted linked list, given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    parameter: List[Optional[ListNode]] lists - a list of sorted linked-list in ascending
    return: Optional[ListNode] head - a merged linked-list in ascending
    Pre-Condition: k == lists.length
                 : 0 <= k <= 10^4
                 : 0 <= lists[i].length <= 500
                 : -10^4 <= lists[i][j] <= 10^4
                 : lists[i] is sorted in ascending order.
                 : The sum of lists[i].length will not exceed 10^4.
    Post-Condition: none
'''
# bruce force: runtime: O(n*k), memory: O(n) where n = number of nodes, k = number of linked lists
def mergeKLists_M1(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeLists(head1: Optional[ListNode], head2: Optional[ListNode]):
        root = ListNode(-1)
        dummy = root

        while head1 and head2:
            if head1.val < head2.val:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next

        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
        return root.next

    head = None
    for li in lists:
        head = mergeLists(head, li)
    return head

'''
    Link: https://leetcode.com/problems/merge-k-sorted-lists
    Purpose: Find the merged sorted linked list, given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    parameter: List[Optional[ListNode]] lists - a list of sorted linked-list in ascending
    return: Optional[ListNode] head - a merged linked-list in ascending
    Pre-Condition: k == lists.length
                 : 0 <= k <= 10^4
                 : 0 <= lists[i].length <= 500
                 : -10^4 <= lists[i][j] <= 10^4
                 : lists[i] is sorted in ascending order.
                 : The sum of lists[i].length will not exceed 10^4.
    Post-Condition: none
'''
# min heap: runtime: O(nlogk), memory: O(n) where n = number of nodes, k = number of linked lists
def mergeKLists_M2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    min_heap = []  # sorted by the head of each list

    # Initialize the heap with the head node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))  # i for tie breaker

    dummy = ListNode(-1)
    current = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lists1 = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]

    lists2 = [
        build_list([]),
        build_list([2, 3]),
        build_list([1])
    ]

    lists3 = [
        build_list([0, 2, 3])
    ]

    lists4 = [
        build_list([-10, -5, 0]),
        build_list([-6, 1, 2]),
        build_list([3, 4])
    ]

    lists5 = [
        build_list([1, 1, 1]),
        build_list([1, 1]),
        build_list([1])
    ]

    print("\n === Solution 2 === \n")
    mergeKLists_M1(lists1).print_list() # 1->1->2->3->4->4->5->6
    mergeKLists_M1(lists2).print_list() # 1->2->3
    mergeKLists_M1(lists3).print_list() # 0->2->3
    mergeKLists_M1(lists4).print_list() # -10->-6->-5->0->1->2->3->4
    mergeKLists_M1(lists5).print_list() # 1->1->1->1->1->1

    lists1 = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6])
    ]

    lists2 = [
        build_list([]),
        build_list([2, 3]),
        build_list([1])
    ]

    lists3 = [
        build_list([0, 2, 3])
    ]

    lists4 = [
        build_list([-10, -5, 0]),
        build_list([-6, 1, 2]),
        build_list([3, 4])
    ]

    lists5 = [
        build_list([1, 1, 1]),
        build_list([1, 1]),
        build_list([1])
    ]

    print("\n === Solution 2 === \n")
    mergeKLists_M2(lists1).print_list()  # 1->1->2->3->4->4->5->6
    mergeKLists_M2(lists2).print_list()  # 1->2->3
    mergeKLists_M2(lists3).print_list()  # 0->2->3
    mergeKLists_M2(lists4).print_list()  # -10->-6->-5->0->1->2->3->4
    mergeKLists_M2(lists5).print_list()  # 1->1->1->1->1->1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
