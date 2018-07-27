"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1: 7329ms
        # length = len(nums)
        # i = 0
        # while i < length:
        #     j = i + 1
        #     while j < length:
        #         if nums[i] + nums[j] == target :
        #             return [i, j]
        #         else:
        #             j += 1
        #     i += 1
        # return [i, j]

        # Solution 2: 1552ms
        # for i in range(len(nums)):
        #     if target-nums[i] in nums and i != nums.index(target-nums[i]):
        #         return [i, nums.index(target-nums[i])]

        # Solution 3: 35ms
        a = sorted(nums)
        length = len(a)
        i, j = 0, length - 1
        while i < j:
            if a[i] + a[j] == target:
                x = nums.index(a[i])
                y = nums.index(a[j])
                if x == y:
                    return [x, nums.index(nums[x], x + 1)]
                return [x, y]
            elif a[i] + a[j] > target:
                j -= 1
            elif a[i] + a[j] < target:
                i += 1
        return [i, j]
