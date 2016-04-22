class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if 1 <= x <= 3:
            return 1
        if x in (4, 5):
            return 2
        start, end = 1, x
        while (start + 1 < end):
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start
