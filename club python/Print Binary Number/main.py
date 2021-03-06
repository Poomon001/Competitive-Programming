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

'''
    Link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md
    Purpose: Print 1 to n binary numbers where n is positive integer   
    Parameter: int - positive integer
    return: String - String of n binary numbers
    Pre-Condition : num is a positive integer
    Post-Condition: none
'''
def printBinary(num):
    q1 = Queue()
    q1.enqueue("1")

    # the next 2 numbers can be generated by adding 0 and 1 to the previous numbers respectively
    # eg. 0b 1 = 1 || add 0 after 0b 1: 0b 10 || add 1 after 0b 1: 0b 11
    # eg. add 0 after 0b 10: 0b 100 || add 1 after 0b 10: 0b 101
    for i in range(0,num):
        front = q1.front()
        print(front)

        # append 0 and 1 to the current number
        q1.enqueue(front+"0") # 1, 1+0, 10+0, 11+0, 100+0, 101+0, ...
        q1.enqueue(front+"1") # 1, 1+1, 10+1, 11+1, 100+1, 101+1, ...

        # remove the current number to allow the second number to be front
        q1.dequeue()

if "__main__" == __name__:
    printBinary(20)


