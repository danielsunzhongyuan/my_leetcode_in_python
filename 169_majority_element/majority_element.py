class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summary = {}
        threshold = len(nums) / 2
        for num in nums:
            summary[num] = summary.get(num, 0) + 1
            if summary[num] > threshold:
                return num
