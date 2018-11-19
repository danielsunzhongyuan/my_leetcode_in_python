class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if 0 == length:
            return [-1, -1]

        i, j = -1, length
        while i + 1 != j:
            mid = (i + j) >> 1
            if nums[mid] < target:
                i = mid
            else:
                j = mid
        if j >= length or nums[j] != target:
            return [-1, -1]
        x = j
        while x < length and nums[x] == target:
            x += 1
        return [j, x - 1]
