''' Linked List '''
'''
finding at index O(n)
insert/delete at start O(1)
insert/delete at middle/end O(n)
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    ''' note: <self> refers to the object of this class eg. self == ll '''
    ''' note2: <self> refers to a linked list but <self.next> refers to the first node of the list '''

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # create a new node object from data + point the next the head node
        node = Node(data, self.head)

        # make this node as a head
        self.head = node

    def insert_at_end(self, data):
        # insert the first element
        if self.head is None:
            self.head = Node(data, None)
            return

        # find the last node
        tail = self.head
        while(tail.next):
            tail = tail.next

        # point the last node to the new node
        tail.next = Node(data, None)

    def insert_at(self, index, data):
        # invalid insertion
        if(index > self.get_length()):
            print("invalid index")
            return

        # case 1: zero node or insert at beginning
        if(self.get_length() == 0 or index == 0):
            self.insert_at_beginning(data)

        # case 2: there is node and not insert on the middle
        else:
            middle = self.head
            while(index != 1):
                middle = middle.next
                index -= 1

            # insert
            node = Node(data, middle.next)
            middle.next = node

    def create_new_linkedlist(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        list = self.head
        while list:
            count += 1
            list = list.next
        return count


    def printLinkedList(self):
        if(self.head is None):
            print("Linked list is empty")
            return

        list = self.head
        while(list):
            print(list.data, end="-->")
            list = list.next

    def remove_last(self):
        # zero element
        if (self.get_length() == 0):
            print("list is empty")
            return

        middle = self.head

        # only one element
        if self.get_length() == 1:
            value = self.head.data
            self.head = None

        # more than one elements
        else:
            # find the last element
            while (middle.next.next):
                middle = middle.next

            # remove
            value = middle.next.data
            middle.next = None
        return value

    def remove_front(self):
        # zero element
        if (self.get_length() == 0):
            print("list is empty")
            return

        middle = self.head

        # only one element
        if self.get_length() == 1:
            value = self.head.data
            self.head = None

        # more than one element
        else:
            # move head to the second element
            self.head = self.head.next

            # remove
            value = middle.data
            middle.next = None
        return value

    def remove_at(self, index):
        # handle invalid index
        if index < -1:
            print("invalid index")
            return -1
        if self.get_length()-1 < index:
            print(f"does not have a node at {index} index")
            return -1

        middle = self.head

        # case 1: remove last element
        if (self.get_length()-1 == index):
            value = self.remove_last()

        # case 2: remove first element
        elif (index == 0):
            value = self.remove_front()

        # case 3: find the node at the index
        else:
            while(index != 1):
                middle = middle.next
                index -= 1

            # remove
            value = middle.next.data
            middle.next = middle.next.next
        return value

    def peek(self):
        if(self.get_length() == 0):
            print("linked list is empty")
            return

        # find last node and return its value
        last = self.head
        while(last.next):
            last = last.next
        return last.data

    def insert_after_value(self, data_after, data_to_insert):
        if(self.get_length() == 0):
            print("data not found")
            return

        list = self.head
        index = 1

        # find the correct index to insert
        while(list is not None):
            if(list.data == data_after):
                self.insert_at(index, data_to_insert)
                return
            list = list.next
            index += 1
        print("data not found")

    def removeAllElements(self, val: int) -> None:
        dummy = Node(-1)
        dummy.next = self.head
        self.head = dummy

        while dummy.next:
            # remove all matching numbers on the middle
            if dummy.next.data == val:
                dummy.next = dummy.next.next;
            # remove the matching number at the end of the linklist
            elif dummy.next.data == val and not dummy.next.next:
                dummy.next = None
            else:
                dummy = dummy.next

        self.head = self.head.next

    def remove_by_value(self, data_to_remove):
        if (self.get_length() == 0):
            print("list is empty")
            return

        list = self.head
        index = 0

        # find the correct index of the data to remove
        while (list is not None):
            if (list.data == data_to_remove):
                self.remove_at(index)
                return
            list = list.next
            index += 1

        print("data not found")



# main
if __name__ == '__main__':
    ll1 = LinkedList()
    print("peek:", ll1.peek())
    ll1.insert_at_end(2)
    print("peek:", ll1.peek())
    ll1.insert_at_end(11)
    ll1.insert_at_end(4)
    ll1.insert_at_end(22)
    ll1.insert_at(0,0)
    ll1.insert_at(3, 110)
    print("remove:", ll1.remove_at(1))
    print("peek:", ll1.peek())
    ll1.printLinkedList()

    print("\n")

    ll2 = LinkedList()
    ll2.create_new_linkedlist([9,8,7,6])
    print("remove:", ll2.remove_at(1))
    ll2.insert_at_beginning(2)
    ll2.insert_at_end(12)
    ll2.insert_at_end(12)
    ll2.insert_at_end(12)
    ll2.insert_at_end(12)
    ll2.insert_at_end(12)
    ll2.insert_at(5,3)
    ll2.printLinkedList()