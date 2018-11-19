"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


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
                self.backtrack(res, tmp_res, candidates, remain - candidates[i], i + 1)
                tmp_res.pop()
                i += 1


if __name__ == "__main__":
    a = Solution()
    nums = [10, 1, 2, 7, 6, 1, 5]
    print a.combinationSum2(nums, 8)
