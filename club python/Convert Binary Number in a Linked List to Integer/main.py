''' linked list does not need to swap elements when insert/remove a new element [O(1)] in a middle
    but array does [O(n)]'''
''' dynamic array need to copy the whole array to new large location when the current location is full but
    linked list does not because each element store in different location and linked by pointers '''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

'''
    Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
    Purpose: Determine the decimal value of a decimal number in a linkedlist
    parameter: Node: a head of a linked list contains binary numbers
    return: int: a decimal number
    Pre-Condition: The Linked List is not empty.
                 : Number of nodes will not exceed 30.
                 : Each node's value is either 0 or 1.
    Post-Condition: none
'''
def getDecimalValue_M1(head: Node) -> int:
    # formular: decimal = a*2^n + b*2^(n-1) + ... + n*2^(0)
    decimal = 0
    dummy = head
    length = 0

    # get length
    while dummy:
        length += 1
        dummy = dummy.next

    # find decimal
    while head:
        length -= 1
        decimal += head.data * (2 ** length)
        head = head.next

    return decimal

'''
    Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
    Purpose: Determine the decimal value of a decimal number in a linkedlist
    parameter: Node: a head of a linked list contains binary numbers
    return: int: a decimal number
    Pre-Condition: The Linked List is not empty.
                 : Number of nodes will not exceed 30.
                 : Each node's value is either 0 or 1.
    Post-Condition: none
'''
def getDecimalValue_M2(head: Node) -> int:
    s = ""

    # find binary in string
    while head:
        s += str(head.data)
        head = head.next

    return int(s, 2)

if __name__ == '__main__':
    # Start with the empty list
    list1 = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()
    list4 = LinkedList()

    # declare all nodes
    one = Node(1)
    two = Node(0)
    three = Node(1)

    # list1
    list1.head = one
    one.next = two
    two.next = three

    four = Node(0)

    # list2
    list2.head = four

    five = Node(1)
    # list3
    list3.head = five

    # list4
    list = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    list4.head = Node(list[0])
    dummy = list4.head
    for i in range(1, len(list)):
        dummy.next = Node(list[i])
        dummy = dummy.next

    print("\n+===== solution M1 =====\n")
    print(getDecimalValue_M1(list1.head)) # 5
    print(getDecimalValue_M1(list2.head)) # 0
    print(getDecimalValue_M1(list3.head)) # 1
    print(getDecimalValue_M1(list4.head)) # 18880

    print("\n+===== solution M2 =====\n")
    print(getDecimalValue_M2(list1.head))  # 5
    print(getDecimalValue_M2(list2.head))  # 0
    print(getDecimalValue_M2(list3.head))  # 1
    print(getDecimalValue_M2(list4.head))  # 18880


