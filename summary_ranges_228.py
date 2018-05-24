class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length = len(nums)
        if length < 1:
            return []
        ret = []
        i = 0
        while i < length:
            continuous_range = str(nums[i])
            tmp = i
            i += 1
            while i<length and (nums[i]-nums[tmp])==(i-tmp):
                i+=1
            if i != tmp+1:
                continuous_range += "->" + str(nums[i-1])
            ret.append(continuous_range)
            
        return ret
