class MyStack(object):
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, x):
        self.stack.append(x)

    def peek(self):
        if self.isempty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.isempty():
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = MyStack()
        self.s2 = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None

        if self.s2.isempty():
            while not self.s1.isempty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None

        if self.s2.isempty():
            while not self.s1.isempty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1.isempty() and self.s2.isempty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
