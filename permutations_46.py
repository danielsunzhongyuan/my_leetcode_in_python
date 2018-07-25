class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # return list(itertools.permutations(nums))
        
        # Solution Two
        if not nums:
            return []
        res = []
        self.dp(res, [], nums)
        return res
        
    def dp(self, results, path, arr):
        if len(path) == len(arr):
            results.append([x for x in path])
            return
        for num in arr:
            if num not in path:
                path.append(num)
                self.dp(results, path, arr)
                path.pop()
            
