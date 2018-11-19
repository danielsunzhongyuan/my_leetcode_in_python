"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""
import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 == n:
            return 0
        res = int(math.sqrt(2*n))
        if res*(res+1)/2 < n:
            while not res*(res+1)/2 <= n < (res+1)*(res+2)/2:
                res += 1
        elif res*(res+1)/2 > n:
            while not res*(res+1)/2 <= n < (res+1)*(res+2)/2:
                res -= 1
        return res
