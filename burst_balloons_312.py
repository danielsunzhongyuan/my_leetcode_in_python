"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        dp = [[0]*length for _ in range(length)]
        return self.helper(nums, length, 0, length-1, dp)
    
    def helper(self, nums, size, start, end, dp):
        if start > end:
            return 0
        if dp[start][end]!=0:
            return dp[start][end]
        cur_max = nums[start]
        for i in range(start, end+1):
            val = self.helper(nums, size, start, i-1, dp) + \
                self.get(nums, i, size) * self.get(nums, start-1, size) * self.get(nums, end+1, size) + \
                self.helper(nums, size, i+1, end, dp)
            cur_max = max(cur_max, val)
        dp[start][end] = cur_max
        return cur_max
    
    def get(self, nums, i, size):
        if i == -1 or i == size:
            return 1
        return nums[i]
