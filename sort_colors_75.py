"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if not nums:
        #     return
        # length = len(nums)
        # colors = [0, 0, 0]
        # for num in nums:
        #     colors[num] += 1
        # nums[:] = [0]*colors[0] + [1]*colors[1] + [2]*colors[2]
        # return
        
        if not nums:
            return
        length = len(nums)
        i, j, k = 0, 0, length - 1
        while j <= k:
            if nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return
