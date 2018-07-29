# -*- encoding=utf-8 -*-
"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.cnt = 1

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        if len(nums) == 0:
            self.root = None
        else:
            self.root = TreeNode(nums[0])
            for num in nums[1:]:
                self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        runner = self.root
        if not runner:
            self.root = TreeNode(val)
        else:
            pre = runner
            while runner:
                if val < runner.val:
                    runner.cnt += 1
                    pre = runner
                    runner = runner.left
                else:
                    runner.cnt += 1
                    pre = runner
                    runner = runner.right
            if val < pre.val:
                pre.left = TreeNode(val)
            else:
                pre.right = TreeNode(val)
        return self.findKthLargest(self.root, self.k)
    
    def findKthLargest(self, node, kth):
        if kth == 1 and not node.right:
            return node.val
        if node.cnt < kth:
            return -1
        
        if node.right:
            if node.right.cnt >= kth:
                return self.findKthLargest(node.right, kth)
            elif node.right.cnt == kth - 1:
                return node.val
            else:
                return self.findKthLargest(node.left, kth-node.right.cnt-1)
        else:
            return self.findKthLargest(node.left, kth-1)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

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
    print b.add(4)

