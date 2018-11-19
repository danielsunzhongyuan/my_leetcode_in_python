"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


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
            if res < (y - x) * min(height[x], height[y]):
                res = (y - x) * min(height[x], height[y])
            if height[x] < height[y]:
                x += 1
            else:
                y -= 1
        return res
