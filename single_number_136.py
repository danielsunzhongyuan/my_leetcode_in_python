class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        res = 0
        for num in nums:
            res ^= num
        return res
