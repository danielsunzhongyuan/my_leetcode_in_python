class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        
        # ugly
        # left, right = 0, 0
        # ret = length + 1
        # found = False
        # count = nums[0]
        # while right < length:
        #     if count < s:
        #         right += 1
        #         if right >= length:
        #             break
        #         count+= nums[right]
        #     else:
        #         found = True
        #         if right-left+1 < ret:
        #             ret = right-left+1
        #         count-=nums[left]
        #         left += 1
        # if found:
        #     return ret
        # return 0
        
        # more gentle
        ret = length + 1
        found = False
        sum_of_subarray = 0
        left = 0
        for i in range(length):
            sum_of_subarray += nums[i]
            while sum_of_subarray >= s:
                if i-left+1<ret:
                    ret = i-left+1
                sum_of_subarray -= nums[left]
                left += 1
        if ret > length:
            return 0
        return ret

def main():
	s = Solution()
	print s.minSubArrayLen(7, [2,3,1,2,4,3])


if __name__ == "__main__":
	main()
