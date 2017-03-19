class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        try_count = minutesToTest / minutesToDie + 1
        res = 0
        while try_count ** res < buckets:
            res += 1
        return res
