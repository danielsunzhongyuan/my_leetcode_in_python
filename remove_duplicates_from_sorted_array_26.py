class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        ret = 0
        for i in range(1, length):
            if nums[i] == nums[ret]:
                continue
            ret += 1
            if ret != i:
                nums[ret] = nums[i]
        return ret+1
