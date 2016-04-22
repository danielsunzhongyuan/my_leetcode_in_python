class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length <= 3:
            return sum(nums)
        nums.sort()
        print nums
        res = sum(nums[0:3])
        for i in range(0, length - 2):
            j, k = i + 1, length - 1
            while j < k:
                print j, k
                currentSum = nums[i] + nums[j] + nums[k]
                if abs(res - target) > abs(currentSum - target):
                    res = currentSum
                if res == target:
                    print i, j, k, nums[i], nums[j], nums[k]
                    return res
                if currentSum > target:
                    k -= 1
                else:
                    j += 1
        return res





class Solution2(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length <= 3:
            return sum(nums)
        nums.sort()
        res = sum(nums[0:3])
        diff = abs(res - target)
        for i in range(0, length-2):
            for j in range(i+1, length-1):
                d = dict([(key, 1) for key in nums[i+2:]])
                for dif in range(diff):
                    if d.has_key(target-nums[i]-nums[j]-dif):
                        res = target - dif
                        diff = dif
                    elif d.has_key(nums[i]+nums[j]-target-dif):
                        res = target + dif
                        diff = dif
        return res
