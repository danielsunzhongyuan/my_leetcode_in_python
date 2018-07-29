class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.data = nums
        if not self.data:
            self.heap = []
            return
        self.data.sort()
        self.heap = self.data[-k:]

    def add(self, val):
        self.data.append(val)
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.heap.sort()
        else:
            if val > self.heap[0]:
                self.heap[0] = val
                self.heap.sort()
        return self.heap[0]

