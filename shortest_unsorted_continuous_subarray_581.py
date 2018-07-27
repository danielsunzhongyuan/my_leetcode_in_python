# -*- encoding=utf-8 -*-
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # length = len(nums)
        # if length <= 1:
        #     return 0
        # i, j = 0, length - 1
        # b = sorted(nums)
        # while i < length and nums[i] == b[i]:
        #     i += 1
        # while j >= 0 and nums[j] == b[j]:
        #     j -= 1
        # if i < j:
        #     return j - i + 1
        # return 0
        
        length = len(nums)
        if length <= 1:
            return 0
        i, j = 0, length - 1
        while i < length - 1 and nums[i] <= nums[i+1]:
            i += 1
        if i == j:
            return 0
        while j > i and nums[j] >= nums[j-1]:
            j -= 1
        if j == 0:
            return 0
        min_num, max_num = min(nums[i:j+1]), max(nums[i:j+1])
        while i >= 0 and nums[i] > min_num: # 这里不能 >=
            i -= 1
        while j < length and nums[j] < max_num: # 这里不能 <=
            j += 1
        return j - i - 1
