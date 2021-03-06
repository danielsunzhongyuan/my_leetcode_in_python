"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Solution one: DP, TLE
        # then continuously optimize it by stop the recurse earlier, for example:
        #   1. return [] if the target is too large or too small
        #   2. return if the length of paths is larger than four
        #   3. when length of paths equals three, just check remain in nums[start:] or not. (remove duplicate of course)
        #   4. since we have #3, the #2 can be ignored
        #   5. when already put some numbers into path, check the remain is too large or too small, just like #1
        length = len(nums)
        if length == 0:
            return []
        nums.sort()
        if nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        res = []
        self.dp(nums, res, [], target, 0, length)
        return res
        
    def dp(self, nums, res, paths, remain, start, length):
        if 3 == len(paths):
            if remain in nums[start:] and paths[:]+[remain] not in res:
                res.append(paths[:] + [remain])
            return
        # if 4 == len(paths):
        #     if remain == 0 and paths not in res:
        #         res.append(paths[:])
        #     return
        if nums[-1]*(4-len(paths)) < remain or (start < length and nums[start]*(4-len(paths)) > remain):
            return
        for i in range(start, length):
            if nums[-1]*(3-len(paths)) + nums[i] < remain:
                continue
            self.dp(nums, res, paths + [nums[i]], remain-nums[i], i+1, length)

#         nums.sort()
#         results = []
#         self.findNsum(nums, target, 4, [], results)
#         return results

#     def findNsum(self, nums, target, N, result, results):
#         if len(nums) < N or N < 2: return

#         # solve 2-sum
#         if N == 2:
#             l,r = 0,len(nums)-1
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                     while r > l and nums[r] == nums[r + 1]:
#                         r -= 1
#                 elif nums[l] + nums[r] < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else:
#             for i in range(0, len(nums)-N+1):   # careful about range
#                 if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
#                     break
#                 if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
#                     self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
#         return

if __name__ == "__main__":
    a = Solution()
    print a.fourSum([-1, 0, 1, 2, -1, -4], -1)
    b = [-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492]
    print a.fourSum(b, 1682)

    c = [91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245]
    print a.fourSum(c, -236727523)
