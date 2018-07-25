class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.backtrack(res, [], candidates, target, 0)
        return res

    def backtrack(self, res, tmp_res, candidates, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            if tmp_res not in res:
                res.append([i for i in tmp_res])
        else:
            i = start
            while i < len(candidates):
                tmp_res.append(candidates[i])
                self.backtrack(res, tmp_res, candidates, remain - candidates[i], i+1)
                tmp_res.pop()
                i += 1

if __name__ == "__main__":
    a = Solution()
    nums = [10,1,2,7,6,1,5]
    print a.combinationSum2(nums, 8)

