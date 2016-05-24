class Solution:
	# @param {integer[]} nums
	# @return {string}
	def largestNumber(self, nums):
		nums = sorted(nums, cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1)
		largest = ''.join([str(x) for x in nums])
		i, length = 0, len(nums)
		while i + 1 < length:
			if largest[i] != '0':
				break
			i += 1
		return largest[i:]
