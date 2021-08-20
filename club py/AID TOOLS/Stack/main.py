from collections import deque
''' List vs collection.dequeue '''
''' List works because it is a dynamic array. Even if the list is full, Python will allocate a larger space to the list '''
''' Python needs to copy the entire list to a new location with a double size of the previous location: O(n) '''
''' Collection.dequeue is a preferred method over List because it is implimented by double-linked list. '''
''' We dont need to be worried about the space is will be full and need to copy the entire list to 
    a new memory location b/c linked list uses pointer to connect each node together: O(1) '''
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack.count() == 0

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s1 = Stack()
    s1.push(3)
    s1.push(10)
    s1.push(1)
    print(s1.stack)
    print("pop:", s1.pop())
    print("peek:", s1.peek())
    print("peek:", s1.peek())
    print(s1.size())

