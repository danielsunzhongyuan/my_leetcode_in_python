class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # import math
        # mid = int(math.sqrt(area))
        # for x in xrange(mid, area + 1):
        #     if area % x == 0 and x>=area/x:
        #         return [x, area/x]
        # return [area,1]

        # import math
        # mid = int(math.sqrt(area))
        # for x in xrange(mid, area+1):
        #     if area%x == 0:
        #         return sorted([x,area/x], reverse=True)
        # return [area,1]

        # import math
        # mid = int(math.sqrt(area))
        # while mid > 0:
        #     if area % mid == 0:
        #         return [area/mid, mid]
        #     mid -= 1

        import math
        mid = int(math.sqrt(area))
        while area%mid != 0:
            mid -= 1
        return [area/mid, mid]
