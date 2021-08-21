from collections import deque
''' List vs collection.dequeue '''
''' List works because it is a dynamic array. Even if the list is full, Python will allocate a larger space to the list '''
''' Python needs to copy the entire list to a new location with a double size of the previous location: O(n) '''
''' Collection.dequeue is a preferred method over List because it is implimented by double-linked list. '''
''' We dont need to be worried about the space is will be full and need to copy the entire list to 
    a new memory location b/c linked list uses pointer to connect each node together: O(1) '''
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def front(self):
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

if "__main__" == __name__:
    q1 = Queue()

    q1.enqueue(10)
    q1.enqueue(5)
    q1.enqueue(1)
    print("front:", q1.front())
    print("dequeue:", q1.dequeue())
    print(q1.queue)

