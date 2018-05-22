class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return length
        ret = 0
        secondTime = False
        for i in range(1, length):
            if nums[i] == nums[ret]:
                if secondTime:
                    continue
                else:
                    secondTime = True
            else:
                secondTime = False
            ret += 1
            if ret != i:
                nums[ret] = nums[i]
        return ret + 1
