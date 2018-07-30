"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution 1: OK.
        # Space: O(n)
        # length = len(nums)
        # if length <= 1:
        #     return
        # k = k % length
        # nums[:] = nums[-k:] + nums[:-k]
        # return
        
        # Solution 2: OK
        # Space: O(1)
        # length = len(nums)
        # if length <= 1:
        #     return
        # k = k % length
        # def reverse(nums, start, end):
        #     i, j = start, end
        #     while i < j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #         j -= 1
        #     return
        # Solution 2.1:
        # reverse(nums, 0, length-1-k)
        # reverse(nums, length-k, length - 1)
        # reverse(nums, 0, length - 1)
        # Solution 2.2:
        # reverse(nums, 0, length - 1)
        # reverse(nums, 0, k - 1)
        # reverse(nums, k, length - 1)
        
        # Solution 3: OK
        # Space: O(1)
        length = len(nums)
        if length <= 1:
            return
        k = k % length
        k = length - k # it desides by rotating to left or rotating to right
        gcd = self.getGCD(k, length)
        if k == 0:
            return
        for i in range(gcd):
            tmp = nums[i]
            j = i
            next_j = (j + k)%length
            while next_j != i:
                nums[j] = nums[next_j]
                j = next_j
                next_j = (j + k)%length
            nums[j] = tmp
        return
    
    def getGCD(self, x, y):
        # while x != y:
        #     if x > y:
        #         x -= y
        #     else:
        #         y -= x
        # return x
        while x % y:
            x, y = y, x % y
        return y
