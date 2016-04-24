class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        length = len(nums)
        if length < 2:
            return True
        return self.canJumpToX(nums, length - 1)

    def canJumpToX(self, nums, pos):
        if pos == 0:
            return True
        stack = []
        for i, num in enumerate(nums[0:pos]):
            if num >= pos - i:
                stack.append(i)
        ret = False
        if not stack:
            return False
        if stack[0] == 0:
            return True
        return self.canJumpToX(nums, stack[0])


class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        length = len(nums)
        if length < 2:
            return True
        lastIndex = length - 1
        while lastIndex:
            stack = []
            for i, num in enumerate(nums[0:lastIndex]):
                if num >= lastIndex - i:
                    stack.append(i)
            if not stack:
                return False
            else:
                lastIndex = stack[0]

        return True


class Solution3(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return True
        lastIndex = length - 1
        while lastIndex:
            tmp = lastIndex
            for i, num in enumerate(nums[lastIndex-1::-1]):
                if num > i:
                    tmp = lastIndex - 1 - i
            if tmp == lastIndex:
                return False
            else:
                lastIndex = tmp
        return True



class Solution4(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return True
        lastIndex = length - 1
        while lastIndex:
            finalStatus = False
            for i in xrange(lastIndex - 1, -1, -1):
                if nums[i] >= lastIndex - i:
                    lastIndex = i
                    break
            if i == 0 and nums[0] < lastIndex:
                return False
        return nums[0] >= lastIndex


class Solution5(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return True
        lastIndex = length - 1
        for i in xrange(length - 2, -1, -1):
            if nums[i] >= lastIndex - i:
                lastIndex = i
        return 0 == lastIndex
