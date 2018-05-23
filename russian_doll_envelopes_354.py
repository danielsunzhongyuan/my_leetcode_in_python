class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        length = len(envelopes)
        if length <= 1:
            return length
        # 这里关键先把envelopes排序这个样子：[[2, 3], [5, 4], [6, 7], [6, 4]]
        # 即先按照每个pair的第一个元素升序，然后如果pair的第一个元素相同，则按照第二个元素倒序！
        # 最后按照每个pair的第二个元素组成的数组，进行LIS，即得到结果
        a = sorted(envelopes, key=lambda x:x[1], reverse=True)
        b = sorted(a, key=lambda x:x[0])
        c = [pair[1] for pair in b]
        return self.lengthOfLIS(c)

    def lengthOfLIS(self, nums):
        import bisect
        if(len(nums) < 2): return len(nums)
        res = [nums[0]]
        for num in nums[1:]:
            if(num == res[-1]):
                continue
            if(num > res[-1]):
                res.append(num)
            elif(num <= res[0]):
                res[0] = num
            else:
                loc = bisect.bisect_left(res, num)
                res[loc] = num
        return len(res)


def main():
	s = Solution()
	a = [[4,5],[4,6],[6,7],[2,3],[1,1]]
	print s.maxEnvelopes(a), 4
	b = [[5,4],[6,4],[6,7],[2,3]]
	print s.maxEnvelopes(b), 3
	c = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
	print s.maxEnvelopes(c), 7
	d = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
	print s.maxEnvelopes(d), 5
	e = [[30,50],[12,2],[3,4],[12,15]]
	print s.maxEnvelopes(e), 3
	f = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
	print s.maxEnvelopes(f), 3


if __name__ == "__main__":
	main()
