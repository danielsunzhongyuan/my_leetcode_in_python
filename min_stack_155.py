class MinStack(object):
    # Solution One: with two stacks
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.min_stack = []
    #     self.data = []
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: void
    #     """
    #     self.data.append(x)
    #     if not self.min_stack or x <= self.min_stack[-1]:
    #         self.min_stack.append(x)
    # def pop(self):
    #     """
    #     :rtype: void
    #     """
    #     if self.data:
    #         x = self.data.pop()
    #         if x == self.min_stack[-1]:
    #             self.min_stack.pop()
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.data[-1] if self.data else None
    # def getMin(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.min_stack[-1] if self.min_stack else None
    
    # Solution Two: with one stack
    # def __init__(self):
    #     self.data = []
    # def push(self, x):
    #     previous_min = self.getMin()
    #     current_min = previous_min if previous_min is not None and previous_min<x else x
    #     self.data.append((x,current_min))
    # def pop(self):
    #     self.data.pop()
    # def top(self):
    #     return self.data[-1][0] if self.data else None
    # def getMin(self):
    #     return self.data[-1][1] if self.data else None

    # Solution Three: with one stack, but store the diff with min
    def __init__(self):
        self.min = 0
        self.data = []
    def push(self, x):
        if not self.data:
            self.data.append(0)
            self.min = x
        else:
            self.data.append(x-self.min)
            if self.min > x:
                self.min = x
    def pop(self):
        if self.data:
            x = self.data.pop()
            if x < 0:
                self.min -= x
    def top(self):
        if self.data:
            return self.data[-1] + self.min if self.data[-1] > 0 else self.min
    def getMin(self):
        return self.min if self.data else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
