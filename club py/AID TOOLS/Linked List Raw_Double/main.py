''' linked list does not need to swap elements when insert/remove a new element [O(1)] in a middle
    but array does [O(n)]'''
''' dynamic array need to copy the whole array to new large location when the current location is full but
    linked list does not because each element store in different location and linked by pointers '''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

if __name__ == '__main__':
    # Start with the empty list
    list1 = LinkedList() # LinkedList type

    # declare all nodes
    first = Node(1) # Node type
    second = Node(2)
    third = Node(3)

    # link all nodes together
    list1.head = first
    first.prev = list1.head

    first.next = second
    second.prev = first

    second.next = third
    third.prev = second

    list1.printList()


