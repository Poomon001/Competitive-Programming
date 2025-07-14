class MyQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.outStack:
            while self.inStack:
                num = self.inStack.pop()
                self.outStack.append(num)

        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            while self.inStack:
                num = self.inStack.pop()
                self.outStack.append(num)
        return self.outStack[-1]

    def empty(self) -> bool:
        return len(self.outStack) + len(self.inStack) == 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Queue 1 === \n")
    queue1 = MyQueue()
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    queue1.push(4)
    print(queue1.pop()) # 1
    queue1.push(5)
    print(queue1.pop()) # 2
    print(queue1.pop()) # 3
    print(queue1.pop()) # 4
    print(queue1.pop()) # 5

    print("\n === Queue 2 === \n")
    queue2 = MyQueue()
    queue2.push(1)
    queue2.push(2)
    print(queue2.peek()) # 1
    print(queue2.pop()) # 1
    print(queue2.empty()) # False

    print("\n === Queue 2 === \n")
    queue2 = MyQueue()
    print(queue2.empty()) # True