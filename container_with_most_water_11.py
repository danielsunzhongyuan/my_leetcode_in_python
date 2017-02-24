class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        x, y = 0, length - 1
        res = 0
        while x < y:
            if res < (y-x)*min(height[x], height[y]):
                res = (y-x)*min(height[x], height[y])
            if height[x] < height[y]:
                x += 1
            else:
                y -= 1
        return res
