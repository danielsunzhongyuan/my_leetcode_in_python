"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume DUPLICATE exists in the array.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(nums)
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + ((right - left) >> 1)
            if nums[right] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]
