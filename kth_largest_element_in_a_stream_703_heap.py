class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.data = nums
        if not self.data:
            return
        self.heapSort(self.data, len(self.data))

    def add(self, val):
        self.data.append(val)
        self.heapSort(self.data, len(self.data))
        return self.data[-self.k]

    def buildHeap(self, data, size):
        if not data:
            return
        for i in range(size/2-1, -1, -1):
            self.heapify(data, i, size)
        return size

    def heapify(self, data, i, size):
        leftChild = 2*i+1
        rightChild = 2*i+2
        max = i
        if leftChild < size and data[leftChild] > data[max]:
            max = leftChild
        if rightChild < size and data[rightChild] > data[max]:
            max = rightChild
        if max != i:
            data[i], data[max] = data[max], data[i]
            self.heapify(data, max, size)

    def heapSort(self, data, size):
        heapSize = self.buildHeap(data, size)
        while heapSize > 1:
            heapSize -= 1
            data[0], data[heapSize] = data[heapSize], data[0]
            self.heapify(data, 0, heapSize)

if __name__ == "__main__":
    a = KthLargest(3, [4,5,8,2])
    print a.add(3)
    print a.add(5)
    print a.add(10)
    print a.add(9)
    print a.add(4)

    b = KthLargest(1, [])
    print b.add(-3)
    print b.add(-2)
    print b.add(-4)
    print b.add(0)
    print b.add(2)
    print b.add(4)
