# @question: 78. Subsets
# @author: Zhongyuan Sun

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return [list(y) for x in [list(itertools.combinations(nums, i)) for i in range(len(nums)+1)] for y in x]
        # return [list(y) for x in [list(itertools.combinations(nums, i)) for i in range(len(nums)+1)] for y in x] if len(nums) else [[]]
        # return reduce(lambda z,x: z+[y+[x] for y in z], nums, [[]]) # WONDERFUL
        ans = []
        path = []
        position = 0
        self.dfs(nums, position, path, ans)
        return ans

    def dfs(self, nums, position, path, ans):
        if position == len(nums):
            ans.append(path)
            return
        self.dfs(nums, position+1, path + [nums[position]], ans)
        self.dfs(nums, position+1, path, ans)

	def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        self.backtrack(res, [], nums, 0)
        return res
    
    def backtrack(self, res, path, nums, index):
        res.append([x for x in path])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(res, path, nums, i+1)
            path.pop()
