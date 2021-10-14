from collections import deque
'''     
    Link: https://leetcode.com/problems/min-stack/
    Purpose: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    Parameter: none
    Returns: none
    Pre-Condition: -231 <= val <= 231 - 1
                 : Methods pop, top and getMin operations will always be called on non-empty stacks.
                 : At most 3 * 104 calls will be made to push, pop, top, and getMin.
    Post-Condition: none
'''
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
        return len(self.stack) == 0


    def getMin(self):
        return min(self.stack)


if __name__ == "__main__":
    s1 = Stack()
    s1.push(2)
    s1.push(1)
    s1.push(3)

    print(s1.stack)
    print(s1.getMin())
    s1.pop()
    print("peek:", s1.peek())
    print(s1.getMin())

