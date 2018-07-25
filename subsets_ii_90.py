class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        nums.sort()
        self.backtrack(res, [], nums, 0)
        return res
    
    def backtrack(self, res, path, nums, index):
        res.append([x for x in path])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtrack(res, path, nums, i+1)
            path.pop()
