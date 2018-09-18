"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 1
        for i in range(length):
            while nums[i]<=length and nums[i]>0 and nums[i]!=i+1 and nums[nums[i]-1] !=nums[i]:
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1


if __name__ == "__main__":
    a = Solution()
    print a.firstMissingPositive([3, 4, -1, 1])
