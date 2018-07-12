class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        length = len(nums)
        if length < 1:
            return 0
        if length == 1:
            return nums[0]
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]
