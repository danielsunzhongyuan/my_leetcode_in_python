class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        length = len(envelopes)
        if length <= 1:
            return length
        a = sorted(envelopes)
        print a
        return self.lengthOfLIS(a)
        
    def lengthOfLIS(self, nums):
        import bisect
        if(len(nums) < 2): return len(nums)
        res = [nums[0]]
        for num in nums[1:]:
            if(num == res[-1]):
                continue
            if(num[0] > res[-1][0] and num[1] > res[-1][1]):
                res.append(num)
            elif num[0] == res[-1][0] and num[1] >= res[-1][1]:
                continue
            elif num[0] > res[-1][0] and num[1] < res[-1][1]:
                loc = bisect.bisect_left([i[1] for i in res], num[1])
                res[loc] = num
            print res
        return len(res)


def main():
	s = Solution()
	# a = [[4,5],[4,6],[6,7],[2,3],[1,1]]
	# print s.maxEnvelopes(a), 4
	# b = [[5,4],[6,4],[6,7],[2,3]]
	# print s.maxEnvelopes(b), 3
	# c = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
	# print s.maxEnvelopes(c), 7
	# d = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
	# print s.maxEnvelopes(d), 5
	e = [[30,50],[12,2],[3,4],[12,15]]
	print s.maxEnvelopes(e), 3


if __name__ == "__main__":
	main()
