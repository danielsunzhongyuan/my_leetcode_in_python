# -*- encoding:utf-8 -*-

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # length = len(nums)
        # if length == 0:
        #     return 0
        # longest_increasing_number = [0]*length
        # longest_increasing_number[0] = 1
        # for i in range(1, length):
        #     before_max = 0
        #     for j in range(i):
        #         if nums[j] < nums[i] and longest_increasing_number[j] > before_max:
        #             before_max = longest_increasing_number[j]
        #     longest_increasing_number[i] = 1 + before_max
        # return max(longest_increasing_number)

        # 这个算法的精髓在于：
        # res 数组并不是真正的保存结果，即最长升序串，而是让最长升序串把这个数组撑起来
        # 最终从res的长度得知，最长升序串的长度

        # 如果后面的数，比res最后的数大，就填进去，
        # 如果后面的数，小于等于res第一个数，就换一下
        # 否则，就在 res 里找到响应的位置，替换进去。
        # 假如nums数组是 [10，100，101，102，11，12，13，14，2, 2，1]，那么res的变化是
        # [10]
        # [10, 100]
        # [10, 100, 101]
        # [10, 100, 101, 102]
        # [10, 11, 101, 102]
        # [10, 11, 12, 102]
        # [10, 11, 12, 13]
        # [10, 11, 12, 13, 14]
        # [2, 11, 12, 13, 14]
        # [2, 11, 12, 13, 14]
        # [1, 11, 12, 13, 14]
        # 最长升序串是 10，11，12，13，14，长度为 5
        import bisect
        if len(nums) < 2:
            return len(nums)
        res = [nums[0]]
        for num in nums[1:]:
            if num == res[-1]:
                continue
            if num > res[-1]:
                res.append(num)
            elif num <= res[0]:
                res[0] = num
            else:
                loc = bisect.bisect_left(res, num)
                res[loc] = num
        return len(res)
