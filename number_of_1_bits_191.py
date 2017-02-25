class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return bin(n).count("1")
        
        # res = 0
        # while n:
        #     n = n & (n - 1)
        #     res += 1
        # return res
        
        res = 0
        while n:
            res += n&1
            n = n >> 1
        return res
