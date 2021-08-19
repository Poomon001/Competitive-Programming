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

if __name__ == '__main__':
    # Start with the empty list
    list1 = LinkedList()

    # declare all nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)

    # link all nodes together: method 1
    list1.head = first
    first.next = second
    second.next = third

    list1.printList()

