class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            return 0
        ret = 0
        largest, second_largest = nums[0], nums[1]
        if largest < second_largest:
            largest, second_largest = second_largest, largest
            ret = 1
            
        for x in range(2, length):
            if nums[x] >= largest:
                second_largest = largest
                largest = nums[x]
                ret = x
            elif nums[x] >= second_largest:
                second_largest = nums[x]
            else:
                continue
        if largest >= 2*second_largest:
            return ret
        else:
            return -1
