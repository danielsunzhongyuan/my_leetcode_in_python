class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum, max, maxIndex = 0, -1, -1

        for i, h in enumerate(height):
            if max < h:
                max = h
                maxIndex = i

        prev = 0
        for i in range(maxIndex):
            if height[i] > prev:
                sum += (height[i] - prev) * (maxIndex - i)
                prev = height[i]
            sum -= height[i]

        prev = 0
        for i in range(len(height) - 1, maxIndex, -1):
            if height[i] > prev:
                sum += (height[i] - prev) * (i - maxIndex)
                prev = height[i]
            sum -= height[i]

        return sum
