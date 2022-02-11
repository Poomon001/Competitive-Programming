class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoubleLinkedList:
    def __init__(self):
        self.head = None


    def printLinkedList_forward(self):
        if(self.head is None):
            return

        # dummy will move for head to remain head at front
        dummy = self.head
        while dummy:
            print(dummy.data, end="-->")
            dummy = dummy.next


    def printLinkedList_backward(self):
        if (self.head is None):
            return

        dummy = self.head

        # get to the end of linked list
        while dummy.next:
            dummy = dummy.next

        while dummy:
            print(dummy.data, end="-->")
            dummy = dummy.prev


    def insert_at_beginning(self, data):
        # case 1: double linked list is empty
        if self.head is None:
            # create a new node object
            node = Node(data, None, None) # node.next = head, node.prev = null

            # make this node as a head
            self.head = node
        # casae 2: linked list is not empty
        else:
            # create a new node object
            node = Node(data, self.head, None)

            # The front node point back to the new node
            self.head.prev = node
            self.head = node


    def insert_at_end(self, data):
        # case 1: double linked list is empty then just create a node
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        # casae 2: linked list is not empty
        else:
            node = Node(data, None, None)

            # connect back-most node to new node
            dummy = self.head
            while dummy.next:
                dummy = dummy.next
            node.prev = dummy
            dummy.next = node


    def insert_at(self, index, data):
        # case 1: zero node or insert at beginning
        if(self.head is None or index == 0):
            self.insert_at_beginning(data)
        # casae 2: linked list is not empty
        else:
            node = Node(data, None, None)
            dummy = self.head
            # find the spot to insert
            while (index != 1):
                dummy = dummy.next
                index -= 1

            # connect new node to both adjacent nodes
            dummy.next.prev = node
            node.prev = dummy
            node.next = dummy.next
            dummy.next = node


    def create_new_double_linked_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        dummy = self.head
        while dummy:
            count += 1
            dummy = dummy.next
        return count


    def remove_last(self):
        value = 0

        # case 1: no element in the linked list
        if (self.head is None):
            print("list is empty")
            return

        # case 2: only one element in the linked list
        elif (self.get_length() == 1):
            value = self.head.data
            self.head = None

        # case 3: more than one elements
        else:
            # find the last element
            dummy = self.head
            while(dummy.next):
                dummy = dummy.next

            # disconnect the last node
            value = dummy.data
            dummy.prev.next = None
            dummy.prev = None
        return value


    def remove_front(self):
        # case 1: no element in the linked list
        if (self.head is None):
            print("list is empty")
            return

        # case 2: only one element in the linked list
        elif (self.get_length() == 1):
            value = self.head.data
            self.head = None

        # case 3: more than one elements
        else:
            value = self.head.data
            # disconnect the first node
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None

        return value


    def peek(self):
        if (self.head is None):
            print("linked list is empty")
            return

        # find the last element and return
        dummy = self.head
        while (dummy.next):
            dummy = dummy.next
        return dummy.data


    def insert_after_value(self, data_after, data_to_insert):
        if (self.get_length() == 0):
            print("linked list is empty")
            return

        # find position to insert after
        dummy = self.head
        while(dummy):
            if dummy.data == data_after:
                break
            else:
                dummy = dummy.next
        else:
            print("data not find")
            return

        # insert value
        node = Node(data_to_insert, None, None)

        # connect new node to both adjacent nodes
        # case 1: insert after the middle node
        if (dummy.next):
            dummy.next.prev = node
            node.prev = dummy
            node.next = dummy.next
            dummy.next = node
        # case 2: insert after the last node
        else:
            dummy.next = node
            node.prev = dummy


    def remove_by_value(self, data_to_remove):
        if self.head is None:
            print("list is empty")
            return

        dummy = self.head

        # case 1: data_to_remove is at the front
        if dummy.data == data_to_remove:
            self.remove_front()
            return dummy.data

        # search for data_to_remove location in the linked list
        while(dummy.next):
            # case 2: data_to_remove is in the middle
            if dummy.data == data_to_remove:
                value = dummy.data
                # disconnect the curr node from its adjacent nodes
                dummy.next.prev = dummy.prev
                dummy.prev.next = dummy.next
                dummy.next = None
                dummy.prev = None
                break;
            else:
                dummy = dummy.next
        else:
            # case 3: data_to_remove at the end
            if data_to_remove == dummy.data:
                value = self.remove_last()
            # case 4: data_to_remove is not found
            else:
                print("data not find")
                return

        return value


if __name__ == '__main__':
    dll1 = DoubleLinkedList()
    dll1.insert_at_beginning(1)
    dll1.insert_at_beginning(2)
    dll1.insert_at_end(0)
    dll1.insert_at(0, 7)
    print("peek", dll1.peek())
    dll1.printLinkedList_forward()
    print("\n")
    dll1.insert_after_value(10, 9)
    dll1.insert_after_value(2, 3)
    dll1.insert_after_value(3, 5)
    dll1.insert_after_value(0, 9)
    dll1.insert_after_value(7, 6)
    dll1.printLinkedList_forward()
    print("\n")
    print("remove:", dll1.remove_by_value(3))
    dll1.printLinkedList_forward()
    print("\n")
    dll1.printLinkedList_backward()
    print("\n" + "dll1 length is:",  dll1.get_length())

    print("\n")

    dll2 = DoubleLinkedList()
    dll2.create_new_double_linked_list([6,7,8])
    print("peek", dll2.peek())
    print("remove:", dll2.remove_last())
    print("peek", dll2.peek())
    dll2.insert_after_value(7, 1)
    print("remove front:", dll2.remove_front())
    dll2.printLinkedList_forward()
    print("\n" + "dll2 length is:", dll2.get_length())