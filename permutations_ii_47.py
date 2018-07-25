class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return list(set(itertools.permutations(nums)))
        if not nums:
            return []
        nums.sort()
        res = []
        self.backtrack(res, [], nums, [False]*len(nums))
        return res
    
    def backtrack(self, res, path, nums, used):
        if len(path) == len(nums):
            res.append([x for x in path])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and used[i-1]):
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(res, path, nums, used)
            used[i] = False
            path.pop()

