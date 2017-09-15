'''
Some classes to contstruct a Queue from two Stacks
'''

'''
Define a stack class and some member functions to operate on it
'''
class MyStack(object):
    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        if self.size() > 0:
            return self.items.pop()
        else:
            return 0

    def put(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

'''
Define the Queue class which uses Stack objects.
There is an Input stack and an Output stack
Stack is LIFO, Queue is FIFO
Input to the queue: push to the input stack
Output: if output stack is empty, pop the input stack, pushing each item to the
output stack to create the reverse list of entries. LIFO becomes FIFO. We can then
pop the Output stack to obtain items.
'''
class MyQueue(object):
    def __init__(self):
        self.inputQ = MyStack()
        self.outputQ = MyStack()

    def peek(self):
        if self.outputQ.size() == 0:
            while self.inputQ.size() > 0:
                self.outputQ.put(self.inputQ.pop())

        return self.outputQ.peek()

    def pop(self):
        if self.outputQ.size() > 0:
            return self.outputQ.pop()
        else:
            while self.inputQ.size() > 0:
                self.outputQ.put(self.inputQ.pop())
            return self.outputQ.pop()

    def put(self, value):
        self.inputQ.put(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())


