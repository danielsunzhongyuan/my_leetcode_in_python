class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum / 2
        return self.helper(nums, len(nums) - 1, half_sum)

    def helper(self, nums, length, half_sum):
        if half_sum == 0:
            return True
        if length < 0 or half_sum < 0 or half_sum < nums[length]:
            return False
        return self.helper(nums, length - 1, half_sum - nums[length]) or self.helper(nums, length - 1, half_sum)
